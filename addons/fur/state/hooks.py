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

from .case import Case
from .state import state
from .. import utils


@utils.hook_print(
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
    case = Case(
        cmdr=matches.get('cmdr'),
        system=matches.get('system'),
        platform_name=matches.get('platform'),
        is_cr=matches.get('o2') != 'OK',
        language=matches.get('language')
    )
    state.put_case(case)


@utils.hook_print(
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
    case = Case(
        cmdr=matches.get('cmdr'),
        system=matches.get('system'),
        landmark=matches.get('landmark'),
        platform_name=matches.get('platform'),
        is_cr=matches.get('o2') != 'OK',
        language=matches.get('language_code'),
        num=int(matches.get('num')),
    )
    state.put_case(case)


_list_item_rexp = re.compile(
    r'(\[(?P<num>\d+)] '
    r'(?P<cmdr>[^)]+) '
    r'\((?P<platform>[^)]+)\)) ?'
    r'(?:\((?P<cr>CR)\))? ?'
    r'(?:\((?P<inactive>Inactive)\))?',
    flags=re.IGNORECASE,
)


@utils.hook_print(
    match_author='MechaSqueak[BOT]',
    match_message=re.compile(r'\d+ cases found')
)
def mecha_list(message: str, **kwargs):
    state.clear()

    items = message.split(', ')
    if len(items) < 2:
        return
    items = items[1:]
    for item in items:
        matches: typing.Dict = _list_item_rexp.match(item).groupdict()
        case = Case(
            cmdr=matches.get('cmdr'),
            num=int(matches.get('num')),
            platform_name=matches.get('platform'),
            is_cr=matches.get('is_cr'),
            is_active=not matches.get('inactive'),
        )
        state.put_case(case)


_mecha_close = re.compile(
    r'Successfully closed case #(?P<num>\d+).*',
    flags=re.IGNORECASE,
)


@utils.hook_print(
    match_author='MechaSqueak[BOT]',
    match_message='Successfully closed case'
)
def mecha_close(message: str, **kwargs):
    matches: typing.Dict = _mecha_close.match(message).groupdict()
    state.delete_case(num=int(matches['num']))


@utils.hook_command(names=('state', 'status'))
def hook(**kwargs):
    utils.print(state)