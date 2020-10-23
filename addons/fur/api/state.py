import typing as t

from . import utils, types, format, gui

# -----------------------------------------------------------------------------
# Helper functions.

_state: types.State = {
    'cases': [],
    'rats': [],
}


def _add_case(case: types.Case) -> types.Case:
    global _state

    _state['cases'].append(case)
    gui.update_board()
    return case


def _update_case(case: types.Case, data: t.Dict) -> types.Case:
    case.update(data)
    print(data)
    gui.update_board()
    return case


def _delete_case(case: types.Case) -> types.Case:
    global _state

    _state['cases'].remove(case)
    gui.update_board()
    return case


def _get_free_case_num() -> int:
    global _state

    return max(max([c['num'] for c in _state['cases']] + [0]), 100) + 1


# -----------------------------------------------------------------------------
# Public API.

def clear() -> str:
    global _state

    _state['cases'] = []
    _state['rats'] = []

    return 'state cleared'


def put_case(
    num: int = None,
    cmdr: str = None,
    is_active: bool = None,
    is_cr: bool = None,

    nick: str = None,
    language: str = None,
    platform: types.Platform = None,

    landmark: str = None,
    system: str = None,
):
    global _state

    case_data = {
        'num': num,
        'cmdr': cmdr,
        'is_active': is_active,
        'is_cr': is_cr,

        'nick': nick,
        'language': language,
        'platform': platform,
        'landmark': landmark,
        'system': system,
    }
    # Remove None keys from the dict.
    bad_keys = [k for k, v in case_data.items() if v is None]
    list(map(lambda x: case_data.pop(x), bad_keys))

    # Try to find and update existing case.
    case = find_case(num) or find_case(cmdr) or find_case(nick)
    if case:
        updates = format.dict_updates(case, case_data)
        _update_case(case, case_data)
        return f'{format.case(case)} updated:\n{updates}'

    # Create new case.
    if num is None:
        num = _get_free_case_num()
    case_data = {
        'num': num,
        'cmdr': cmdr,
        'is_active': is_active if is_active is not None else True,
        'is_cr': is_cr if is_cr is not None else False,

        'nick': nick or '',
        'language': language or 'en',
        'platform': platform or types.Platform.DEFAULT,
        'landmark': landmark or '',
        'system': system or '',
    }
    case = _add_case(case_data)
    return f'{format.case(case)} created'


def find_case(query: t.Union[int, str]) -> t.Optional[types.Case]:
    global _state

    # Immediately return if query is empty.
    if query is None or query == '':
        return

    # Convert '#num' query to 'num' query.
    if isinstance(query, str) and query.startswith('#'):
        try:
            query = int(query[1:])
        except ValueError:
            pass

    # Try to find case by:
    # case number
    if isinstance(query, int):
        try:
            return next(c for c in _state['cases'] if c['num'] == query)
        except StopIteration:
            pass

    if isinstance(query, str):
        # case nick
        try:
            return next(c for c in _state['cases'] if utils.nicks_match(
                c['nick'], query,
            ))
        except StopIteration:
            pass

        # case cmdr
        try:
            return next(
                c for c in _state['cases'] if
                c['cmdr'].lower() == query.lower()
            )
        except StopIteration:
            pass

        # rat nick
        try:
            rat: types.Rat = next(
                r for r in _state['rats'] if utils.nicks_match(
                    r['nick'], query,
                )
            )
            return find_case(rat['case_num'])
        except StopIteration:
            pass

        # rat cmdr
        try:
            rat: types.Rat = next(
                r for r in _state['rats'] if
                r['cmdr'].lower() == query.lower()
            )
            return find_case(rat['case_num'])
        except StopIteration:
            pass


def delete_case(num: int):
    global _state

    case = find_case(num)
    _delete_case(case)


def get_state() -> types.State:
    global _state

    return _state
