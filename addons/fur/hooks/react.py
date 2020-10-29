import re
import typing as t

from .. import api


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text=re.compile(r'Incoming Client: (?P<cmdr>[^-]+) - System:'),
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
@api.hooks.print(match_text='RATSIGNAL')
def handler(text: str, mode: str, **kwargs):
    num = ratsignal_casenum_matcher.search(
        text,
    ).groupdict()['num']
    cmdr = ratsignal_cmdr_matcher.search(text).groupdict()['cmdr']
    api.utils.print(str(api.cases.put(cmdr=cmdr, num=num)))


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text=re.compile(r'!(?:close|clear|md|trash)\s+(?P<query>[^\s]+)'),
)
def handler(matches: t.Match, **kwargs):
    query = matches['query']
    case = api.cases.get(num=query, nick=query, cmdr=query)
    if api.cases.delete(num=case.num):
        api.print(f'case #{case.num} nick association was removed')


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text=re.compile(r'!nick\s+(?P<query>[^\s]+)\s+(?P<nick>[^\s]+)'),
)
def handler(matches: t.Match, **kwargs):
    query = matches['query']
    nick = matches['nick']
    case = api.cases.get(num=query, nick=query, cmdr=query)
    if case:
        case.nick = nick
        api.print(f'case #{case.num} nick association was updated: {nick}')
    return


_list_item_rexp = re.compile(
    r'(\[(?P<num>\d+)] '
    r'(?P<cmdr>[^)]+) '
    r'\((?P<platform>[^)]+)\)) ?',
    flags=re.IGNORECASE,
)


# noinspection PyUnusedLocal
@api.hooks.print(
    match_text=re.compile(r'\d+ cases found'),
)
def handler(text: str, **kwargs):
    items = text.split(', ')
    if len(items) < 2:
        return

    items = items[1:]
    nums = []
    for item in items:
        matches: t.Dict = _list_item_rexp.match(item).groupdict()
        nums.append(matches.get('num'))
        api.cases.put(
            cmdr=matches.get('cmdr'),
            num=matches.get('num'),
        )
    for case in api.cases.get_all():
        if case.num not in nums:
            api.cases.delete(num=case.num)
