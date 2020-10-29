import typing as t

from . import utils
from .const import Color


class Case:
    __slots__ = ['cmdr', 'num', 'nick']

    def __init__(
        self,
        cmdr: str,
        num: str = None,
        nick: str = None,
    ):
        self.cmdr = utils.strip(cmdr)
        self.num = utils.strip(num)
        self.nick = utils.strip(nick)

    @property
    def name(self):
        return self.nick or self.cmdr

    def __str__(self):
        return f'{Color.default}({Color.client}{self.name}' \
               f'{Color.info}#{self.num}{Color.default})'


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
