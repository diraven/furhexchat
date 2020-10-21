import typing

from .case import Case
from .. import utils


class State:
    def __init__(self):
        self.cases: typing.List[Case] = []

    def __str__(self) -> str:
        if self.cases:
            return '\n'.join(
                case.format() for case in self.cases,
            )
        return 'No cases.'

    def get_free_case_num(self):
        return max(max([case.num for case in self.cases] + [0]), 100) + 1

    def clear(self):
        utils.print('Cleared all cases')
        self.cases = []

    def sort(self):
        self.cases.sort(
            key=lambda x: (not x.is_active, x.num),
        )

    def find_case(
        self,
        *,
        case_num: typing.Optional[int] = None,
        nick: typing.Optional[str] = None,
        cmdr: typing.Optional[str] = None,
    ) -> typing.Optional[Case]:

        if case_num:
            try:
                return next(c for c in self.cases if c.num == case_num)
            except StopIteration:
                pass
        if nick:
            try:
                return next(
                    c for c in self.cases if utils.nicks_match(c.nick, nick),
                )
            except StopIteration:
                pass
        if cmdr:
            try:
                return next(c for c in self.cases if c.cmdr == cmdr)
            except StopIteration:
                pass

    def put_case(self, case: Case):
        stored_case = self.find_case(
            case_num=case.num,
            nick=case.nick,
            cmdr=case.cmdr,
        )
        if stored_case:
            stored_case.update(case)
        else:
            if case.num is None:
                case.num = self.get_free_case_num()
            self.cases.append(case)
            utils.print(f'New case: {case.format()}')
        self.sort()

    def delete_case(self, num: int):
        stored_case = self.find_case(case_num=num)
        if stored_case:
            utils.print(f'Cleared case: {stored_case}')
            self.cases.remove(stored_case)
            return
        utils.print(f'Case not found: #{num}', utils.Color.DANGER)
        self.sort()


state = State()
