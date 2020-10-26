import re
import typing as t

from .. import api


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text=re.compile(r'Incoming Client: (?P<cmdr>[^-]+) - System:'),
    match_events=[api.const.EVENT.YOUR_MESSAGE],
    priority=api.const.PRIORITY.LOWEST,
)
def handler(text: str, matches: t.Dict, **kwargs):
    cmdr = matches['cmdr']
    nick = None
    if 'IRC Nickname' in text:
        nick = text.split()[-1]
    api.utils.print(str(api.cases.put(cmdr=cmdr, nick=nick)))


ratsignal_casenum_matcher = re.compile(r'Case #(?P<num>\d+)')
ratsignal_cmdr_matcher = re.compile(r'CMDR (?P<cmdr>.*) - Reported System:')


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text='RATSIGNAL',
    match_events=[api.const.EVENT.YOUR_MESSAGE],
    priority=api.const.PRIORITY.LOWEST,
)
def handler(text: str, mode: str, **kwargs):
    num = ratsignal_casenum_matcher.search(
        text,
    ).groupdict()['num']
    cmdr = ratsignal_cmdr_matcher.search(text).groupdict()['cmdr']
    api.utils.print(str(api.cases.put(cmdr=cmdr, num=num)))


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text=re.compile(r'!(?:close|clear|md|trash)\s+(?P<query>[^\s]+)'),
    match_events=[
        api.const.EVENT.YOUR_MESSAGE,
        api.const.EVENT.CHANNEL_MESSAGE,
        api.const.EVENT.CHANNEL_MSG_HILIGHT,
        api.const.EVENT.PRIVATE_MESSAGE_TO_DIALOG,
        api.const.EVENT.PRIVATE_MESSAGE,
    ],
    priority=api.const.PRIORITY.LOWEST,
)
def handler(matches: t.Match, **kwargs):
    query = matches['query']
    case = api.cases.get(num=query, nick=query, cmdr=query)
    if case:
        api.close_context(f'#{case.num}')
        if api.cases.delete(num=case.num):
            api.print(f'case #{case.num} nick association was removed')


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text=re.compile(r'!(?:nick)\s+(?P<query>[^\s]+)\s+(?P<nick>[^\s]+)'),
    match_events=[api.const.EVENT.YOUR_MESSAGE],
    priority=api.const.PRIORITY.LOWEST,
)
def handler(matches: t.Match, **kwargs):
    query = matches['query']
    nick = matches['nick']
    case = api.cases.get(num=query, nick=query, cmdr=query)
    if case:
        case.nick = nick
        api.print(f'case #{case.num} nick association was updated: {nick}')
    return
