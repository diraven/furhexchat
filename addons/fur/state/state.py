import typing

from .case import Case
from .. import utils


class State:
    def __init__(self):
        self._cases: typing.List[Case] = []

    def __str__(self) -> str:
        if self._cases:
            return ' '.join(
                str(case) for case in self.cases,
            )
        return 'No cases.'

    @property
    def cases(self):
        return sorted(
            self._cases, key=lambda x: (
                not x.is_active,
                x.is_cr,
                x.num,
            ),
        )

    def print(self):
        if self.cases:
            for case in self.cases:
                case.print()
            return
        utils.print('No cases.')

    def get_free_case_num(self):
        return max(max([case.num for case in self._cases] + [0]), 100) + 1

    def clear(self):
        utils.print('Cleared all cases')
        self._cases = []

    def find_case(
        self,
        *,
        num: typing.Optional[int] = None,
        nick: typing.Optional[str] = None,
        cmdr: typing.Optional[str] = None,
    ) -> typing.Optional[Case]:

        if num is not None:
            try:
                return next(c for c in self._cases if c.num == num)
            except StopIteration:
                pass
        if nick:
            try:
                return next(
                    c for c in self._cases if utils.nicks_match(c.nick, nick),
                )
            except StopIteration:
                pass
        if cmdr:
            try:
                return next(c for c in self._cases if c.cmdr == cmdr)
            except StopIteration:
                pass
        utils.print(
            f'Case not found: #{num} {cmdr} {nick}', utils.Label.WARNING.value,
        )

    def put_case(self, case: Case):
        stored_case = self.find_case(
            num=case.num,
            nick=case.nick,
            cmdr=case.cmdr,
        )
        if stored_case:
            stored_case.update(case)
        else:
            if case.num is None:
                case.num = self.get_free_case_num()
            self._cases.append(case)
            utils.print(f'New case:', utils.Label.SUCCESS.value)
            case.print()

    def delete_case(self, num: int):
        stored_case = self.find_case(num=num)
        if stored_case:
            utils.print(f'Deleted case: {stored_case}')
            self._cases.remove(stored_case)
            return


state = State()
