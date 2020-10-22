"""
print:
def hook(author: str, message: str, matches: typing.Dict[str, str] mode:
str, data: typing.Any):
    pass

command:
def hook(args: typing.List[str], data: typing.Any):
    pass

"""
import re
import typing

from . import api

_platforms = {
    'pc': api.types.Platform.PC,
    'playstation': api.types.Platform.PLAYSTATION,
    'playstation4': api.types.Platform.PLAYSTATION,
    'ps': api.types.Platform.PLAYSTATION,
    'ps4': api.types.Platform.PLAYSTATION,
    'xbox': api.types.Platform.XBOX,
    'xb': api.types.Platform.XBOX,
}


# noinspection PyUnusedLocal
@api.hook_print(
    match_author='RatMama[BOT]',
    match_message=re.compile(
        r'Incoming Client: (?P<cmdr>.+) - '
        r'System: (?P<system>.+) - '
        r'Platform: ''(?P<platform>.+) - '
        'O2: (' r'?P<o2>.+) - '
        r'Language: (?P<language>.+) \((?P<language_code>.*)\)',
        flags=re.IGNORECASE,
    ),
)
def mama_announcement(
    matches: typing.Dict[str, str],
    **kwargs,
):
    platform = _platforms[matches.get('platform').lower()]
    api.put_case(
        cmdr=matches.get('cmdr'),
        system=matches.get('system'),
        platform=platform,
        is_cr=matches.get('o2') != 'OK',
        language=matches.get('language')
    )


# noinspection PyUnusedLocal
@api.hook_print(
    match_author='MechaSqueak[BOT]',
    match_message=re.compile(
        r'RATSIGNAL - '
        r'CMDR (?P<cmdr>.+) - '
        r'Reported System: (?P<system>.+) \((?P<landmark>.+)\) - '
        r'Platform: (?P<platform>.+) - '
        r'O2: (?P<o2>.+) '
        r'Language: (?P<language>.+) \((?P<language_code>.+)\) '
        r'\(Case #(?P<num>\d+)\) '
        r'\((?P<platform_signal>.+)\)',
        flags=re.IGNORECASE,
    ),
)
def mecha_announcement(
    matches: typing.Dict[str, str],
    **kwargs,
):
    platform = _platforms[matches.get('platform').lower()]
    api.put_case(
        cmdr=matches.get('cmdr'),
        system=matches.get('system'),
        landmark=matches.get('landmark'),
        platform=platform,
        is_cr=matches.get('o2') != 'OK',
        language=matches.get('language_code'),
        num=int(matches.get('num')),
    )


_list_item_rexp = re.compile(
    r'(\[(?P<num>\d+)] '
    r'(?P<cmdr>[^)]+) '
    r'\((?P<platform>[^)]+)\)) ?',
    flags=re.IGNORECASE,
)


# noinspection PyUnusedLocal
@api.hook_print(
    match_author='MechaSqueak[BOT]',
    match_message=re.compile(r'\d+ cases found')
)
def mecha_list(message: str, **kwargs):
    items = message.split(', ')
    if len(items) < 2:
        return
    items = items[1:]
    nums = []
    for item in items:
        matches: typing.Dict = _list_item_rexp.match(item).groupdict()
        nums.append(int(matches.get('num')))
        platform = _platforms[matches.get('platform').lower()]
        api.put_case(
            cmdr=matches.get('cmdr'),
            num=int(matches.get('num')),
            platform=platform,
            is_cr='(cr)' in item.lower(),
            is_active='(inactive)' not in item.lower(),
        )
    print(list(map(lambda c: c['num'], api.get_state()['cases'])))
    for case_num in map(lambda c: c['num'], api.get_state()['cases']):
        if case_num not in nums:
            api.delete_case(case_num)


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!(?:close|clear|md|trash) (?P<query>.+)')
)
def delete_case(matches: typing.Dict[str, str], **kwargs):
    query = matches['query'].strip()
    case = api.find_case(query)
    if not case:
        api.print(f'Case not found: {query}')
        return
    api.delete_case(num=int(case['num']))


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!cr (?P<query>.+)')
)
def cr_case(matches: typing.Dict[str, str], **kwargs):
    query = matches['query'].strip()
    case = api.find_case(query)
    if not case:
        api.print(f'Case not found: {query}')
        return
    api.put_case(num=case['num'], is_cr=not case['is_cr'])


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!active (?P<num>\d+)')
)
def activate_case(
    matches: typing.Dict[str, str],
    **kwargs,
):
    query = matches['query'].strip()
    case = api.find_case(query)
    if not case:
        api.print(f'Case not found: {query}')
        return
    api.put_case(num=case['num'], is_active=not case['is_active'])
