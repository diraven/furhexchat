"""
print:
def hook(author: str, message: str, mode: str, data: typing.Any):
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

_ratmama_rexp = re.compile(
    r'Incoming Client: (?P<cmdr>.+) - '
    r'System: (?P<system>.+) - '
    r'Platform: ''(?P<platform>.+) - '
    'O2: (' r'?P<o2>.+) - '
    r'Language: (?P<language>.+) \((?P<language_code>.*)\)',
    flags=re.IGNORECASE,
)


@utils.hook_print(
    # author='RatMama[BOT]',
    prefix='Incoming Client',
)
def mama_announcement(message: str, **kwargs):
    matches: typing.Dict = _ratmama_rexp.match(message).groupdict()
    case = Case(
        cmdr=matches.get('cmdr'),
        system=matches.get('system'),
        platform_name=matches.get('platform'),
        is_cr=matches.get('o2') != 'OK',
        language=matches.get('language')
    )
    state.put_case(case)


_mecha_rexp = re.compile(
    r'RATSIGNAL - '
    r'CMDR (?P<cmdr>.+) - '
    r'Reported System: (?P<system>.+) \((?P<landmark>.+)\) - '
    r'Platform: (?P<platform>.+) - '
    r'O2: (?P<o2>.+) '
    r'Language: (?P<language>.+) \((?P<language_code>.+)\) '
    r'\(Case #(?P<num>\d+)\) '
    r'\((?P<platform_signal>.+)\)',
    flags=re.IGNORECASE,
)


@utils.hook_print(
    # author='MechaSqueak[BOT]',
    prefix='RATSIGNAL',
)
def mecha_announcement(message: str, **kwargs):
    matches: typing.Dict = _mecha_rexp.match(message).groupdict()
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
    # author='MechaSqueak[BOT]',
)
def mecha_list(message: str, **kwargs):
    if not ' '.join(message.split(' ')[1:]).startswith('cases found'):
        return

    state.clear()

    items = message.split(', ')
    if len(items) < 2:
        return
    items = items[1:]
    for item in items:
        print(f'"{item}"')
        matches: typing.Dict = _list_item_rexp.match(item).groupdict()
        case = Case(
            cmdr=matches.get('cmdr'),
            num=int(matches.get('num')),
            platform_name=matches.get('platform'),
            is_cr=matches.get('is_cr'),
            is_active=not matches.get('inactive'),
        )
        state.put_case(case)


@utils.hook_command(names=('state',))
def hook(**kwargs):
    utils.print(state)
