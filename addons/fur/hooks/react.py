import re

from .. import api

simple_casenum_matcher = re.compile(r'(#(?P<num>\d+))', re.IGNORECASE)
cmdr_matcher = re.compile(r'Incoming Client: (?P<cmdr>[^-]+) - System:')
ratsignal_casenum_matcher = re.compile(r'Case #(?P<num>\d+)')
ratsignal_cmdr_matcher = re.compile(r'CMDR (?P<cmdr>.*) - Reported System:')
close_matcher = re.compile(r'!(?:close|clear|md|trash)\s+(?P<query>[^\s]+)')
nick_matcher = re.compile(r'!(?:nick)\s+(?P<query>[^\s]+)\s+(?P<nick>[^\s]+)')


# noinspection PyUnusedLocal
@api.hooks.print(
    match_events=[api.const.EVENT.YOUR_MESSAGE],
    priority=api.const.PRIORITY.LOWEST,
)
def handler(author: str, text: str, mode: str, **kwargs):
    author = api.utils.strip(author)
    text = api.utils.strip(text)

    if text.startswith('Incoming Client:'):
        cmdr = cmdr_matcher.match(text).groupdict()['cmdr']
        nick = None
        if 'IRC Nickname' in text:
            nick = text.split()[-1]
        api.utils.print(str(api.cases.put(cmdr=cmdr, nick=nick)))
        return

    if text.startswith('RATSIGNAL'):
        num = ratsignal_casenum_matcher.search(
            text,
        ).groupdict()['num']
        cmdr = ratsignal_cmdr_matcher.search(text).groupdict()['cmdr']

        api.utils.print(str(api.cases.put(cmdr=cmdr, num=num)))
        return

    matches = close_matcher.match(text)
    if matches:
        query = matches.groupdict()['query']
        case = api.cases.get(num=query, nick=query, cmdr=query)
        if case:
            api.close_context(f'#{case.num}')
            if api.cases.delete(num=case.num):
                api.print(f'case #{case.num} nick association was removed')
        return

    matches = nick_matcher.match(text)
    if matches:
        query = matches.groupdict()['query']
        nick = matches.groupdict()['nick']
        case = api.cases.get(num=query, nick=query, cmdr=query)
        if case:
            case.nick = nick
            api.print(f'case #{case.num} nick association was updated: {nick}')
        return

    matches = simple_casenum_matcher.search(text)
    if not matches:
        return

    num = matches.groupdict()['num']
    case = api.cases.get(num=num)
    if not case:
        return
