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


# context
#
# The context object returned by the functions listed above has these methods:
#
# context.set()
#
# Changes the current context to be the one represented by this context object.
#
# context.prnt(string)
#
# Does the same as the prnt() function but in the given context.
#
# context.emit_print(event_name, *args)
#
# Does the same as the emit_print() function but in the given context.
#
# context.command(string)
#
# Does the same as the command() function but in the given context
#
# context.get_info(type)
#
# Does the same as the get_info() function but in the given context.
#
# context.get_list(type)
#
# Does the same as the get_list() function but in the given context.
#


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
    items = message.split(', ')
    if len(items) < 2:
        return
    items = items[1:]
    nums = []
    for item in items:
        matches: typing.Dict = _list_item_rexp.match(item).groupdict()
        nums.append(int(matches.get('num')))
        case = Case(
            cmdr=matches.get('cmdr'),
            num=int(matches.get('num')),
            platform_name=matches.get('platform'),
            is_cr='cr' in matches,
            is_active=not matches.get('inactive'),
        )
        state.put_case(case)
    for case in state.cases[:]:
        if case.num not in nums:
            state.delete_case(case)


@utils.hook_print(
    match_message=re.compile(r'^!(?:close|clear|md) (?P<num>\d+)')
)
def delete_case(
    matches: typing.Dict[str, str],
    **kwargs,
):
    state.delete_case(num=int(matches['num']))


@utils.hook_print(
    match_message=re.compile(r'^!cr (?P<num>\d+)')
)
def cr_case(
    matches: typing.Dict[str, str],
    **kwargs,
):
    case = state.find_case(num=int(matches['num']))
    if case:
        case.set_prop('is_cr', not case.is_cr)


@utils.hook_print(
    match_message=re.compile(r'^!active (?P<num>\d+)')
)
def activate_case(
    matches: typing.Dict[str, str],
    **kwargs,
):
    case = state.find_case(num=int(matches['num']))
    if case:
        case.set_prop('is_active', not case.is_active)
