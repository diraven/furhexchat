import typing as t

import hexchat
from . import utils, types, format, gui

# -----------------------------------------------------------------------------
# Helper functions.


_state: types.State = {
    'cases': [],
    'leads': {},
}


def _add_case(case: types.Case) -> types.Case:
    global _state

    _state['cases'].append(case)
    _on_state_updated()
    return case


def _update_case(case: types.Case, data: t.Dict) -> types.Case:
    case.update(data)
    _on_state_updated()
    return case


def _delete_case(case: types.Case) -> types.Case:
    global _state

    _state['cases'].remove(case)
    _on_state_updated()
    return case


def _get_free_case_num() -> int:
    global _state

    return max(max([c['num'] for c in _state['cases']] + [0]), 100) + 1


def _rebuild_leads():
    global _state

    _state['leads'] = {}

    for case in _state['cases']:
        _state['leads'][case['cmdr'].lower()] = case
        _state['leads'][case['nick'].lower()] = case
        _state['leads'][f'#{case["num"]}'] = case
        _state['leads'][f'case{case["num"]}'] = case
        _state['leads'][f'case {case["num"]}'] = case
        for rat in case['rats']:
            _state['leads'][rat['cmdr'].lower()] = case
            _state['leads'][rat['nick'].lower()] = case

    # Remove None and empty keys from the dict.
    bad_keys = [k for k in _state['leads'] if k is None or k == '']
    list(map(lambda x: _state['leads'].pop(x), bad_keys))


def _on_state_updated():
    gui.render()
    _rebuild_leads()


# -----------------------------------------------------------------------------
# Public API.

def clear_state() -> str:
    global _state

    _state['cases'] = []
    _state['jump_calls'] = []

    gui.render()
    _rebuild_leads()
    return 'state cleared'


def get_state() -> types.State:
    global _state

    return _state


_platforms = {
    '': types.Platform.PC,
    'pc': types.Platform.PC,
    'playstation': types.Platform.PS,
    'playstation4': types.Platform.PS,
    'ps': types.Platform.PS,
    'ps4': types.Platform.PS,
    'xbox': types.Platform.XB,
    'xb': types.Platform.XB,
}


def put_case(
    num: int = None,
    cmdr: str = None,
    is_active: bool = None,
    is_cr: bool = None,

    nick: str = None,
    language: str = None,
    platform: str = None,

    landmark: str = None,
    system: str = None,
):
    global _state

    if platform is not None:
        platform = _platforms[hexchat.strip(platform).lower()]

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

        'rats': [],
        'jumps': [],
    }
    case = _add_case(case_data)
    return f'{format.case(case)} created'


def delete_case(num: int):
    global _state

    case = find_case(num)
    _delete_case(case)


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

    # Convert to num directly if possible.
    try:
        query = int(query)
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
            for case in _state['cases']:
                rat: types.Rat = next(
                    r for r in case['rats'] if utils.nicks_match(
                        r['nick'], query,
                    )
                )
                return find_case(rat['case_num'])
        except StopIteration:
            pass

        # rat cmdr
        try:
            for case in _state['cases']:
                rat: types.Rat = next(
                    r for r in case['rats'] if
                    r['cmdr'].lower() == query.lower()
                )
                return find_case(rat['case_num'])
        except StopIteration:
            pass


def check_leads(msg: str) -> t.Optional[types.Case]:
    global _state

    try:
        return next(
            case for lead, case in _state['leads'].items()
            if lead in msg.lower()
        )
    except StopIteration:
        pass
