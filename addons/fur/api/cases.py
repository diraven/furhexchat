import collections
import typing as t

Case = collections.namedtuple('Case', [
    'num',
    'nick',
])

_cases: t.List[Case] = []


def get(*, num: str = None, nick: str = None) -> t.Optional[Case]:
    global _cases
    nick = nick.lower() if nick else None

    try:
        return next(
            case for case in _cases if case.num == num or case.nick == nick
        )
    except StopIteration:
        return


def put(num: str, nick: str):
    global _cases
    nick = nick.lower()

    case = get(num=num)
    if case:
        _cases.remove(case)

    case = get(nick=nick)
    if case:
        _cases.remove(case)

    _cases.append(Case(num, nick))


def delete(num):
    global _cases

    case = get(num=num)
    if case:
        _cases.remove(case)
