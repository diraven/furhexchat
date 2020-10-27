import typing as t

from .const import COLOR


class Case:
    __slots__ = ['cmdr', 'num', 'nick']

    def __init__(
        self,
        cmdr: str,
        num: str = None,
        nick: str = None,
    ):
        self.cmdr = cmdr
        self.num = num
        self.nick = nick

    def __str__(self):
        return f'({self.nick or self.cmdr}#{self.num})'


_cases: t.List[Case] = []


def get(**kwargs) -> t.Optional[Case]:
    global _cases

    try:
        return next(
            case for case in _cases if any(
                getattr(
                    case, k,
                ) == v and v is not None for k, v in kwargs.items(),
            )
        )
    except StopIteration:
        return


def put(**kwargs):
    global _cases

    case = get(**kwargs)
    if case:
        for k, v in kwargs.items():
            if v is not None:
                setattr(case, k, v)
    else:
        case = Case(**kwargs)
        _cases.append(case)

    return case


def delete(**kwargs):
    global _cases

    case = get(**kwargs)
    if case:
        _cases.remove(case)
    return case


def get_all():
    global _cases

    return _cases
