import typing as t
from dataclasses import dataclass, field

from . import utils, types, context, config


@dataclass
class Rat:
    case: 'Case'

    _nick: str
    _cmdr: str = ''
    _fr: t.Optional[bool] = None
    _prep: t.Optional[bool] = None
    _pos: t.Optional[bool] = None
    _wr: t.Optional[bool] = None
    _bc: t.Optional[bool] = None
    _fuel: t.Optional[bool] = None

    def __str__(self) -> str:
        return self._cmdr or self._nick

    def details(self) -> str:
        value_to_char = {
            None: '?',
            True: '+',
            False: '-',
        }
        value_to_color = {
            None: types.Color.GRAY,
            True: types.Color.GREEN,
            False: types.Color.RED,
        }
        data = ''
        if self.case.is_cr:
            bits = ['fr', 'prep', 'pos', 'wr', 'bc', 'fuel']
        else:
            bits = ['fr', 'prep', 'wr', 'bc', 'fuel']
        for bit in bits:
            val = getattr(self, f'_{bit}')
            char = value_to_char[val]
            color = value_to_color[val].value
            no_color = types.Color.DEFAULT.value
            data = data + f' [{color}{bit}{char}{no_color}]'
        return f'{data} - {self}'

    @property
    def nick(self):
        return self._nick

    @property
    def cmdr(self):
        return self._cmdr

    @property
    def fr(self):
        return self._fr

    @property
    def wr(self):
        return self._wr

    @property
    def bc(self):
        return self._bc

    def delete(self):
        return self.case.delete_rat(self)


_platform_color = {
    'ps': types.Color.ROYAL_BLUE.value,
    'ps4': types.Color.ROYAL_BLUE.value,
    'playstation': types.Color.ROYAL_BLUE.value,
    'playstation4': types.Color.ROYAL_BLUE.value,
    'x': types.Color.GREEN.value,
    'xb': types.Color.GREEN.value,
    'xbox': types.Color.GREEN.value,
    'pc': types.Color.PURPLE.value,
}


@dataclass
class Case:
    _state: 'State'

    _num: str
    _cmdr: str = ''
    _is_active: bool = True
    _is_cr: bool = False

    _nick: str = ''
    _language: str = 'en'
    _platform: str = ''

    _system: str = ''
    _landmark: str = ''

    _last_quote: str = ''

    _rats: t.List[Rat] = field(default_factory=list)
    _jump_calls: t.List[str] = field(default_factory=list)

    def __str__(self):
        color = types.Color.SUCCESS
        if self.is_cr:
            color = types.Color.ERROR
        if not self.is_active:
            color = types.Color.LIGHT_GRAY

        return f'' \
               f'{color.value}' \
               f'#{self.num}' \
               f'{types.Color.DEFAULT.value}-' \
               f'[' \
               f'{_platform_color[self.platform.lower()]}' \
               f'{self.platform}' \
               f'{types.Color.DEFAULT.value}' \
               f'|' \
               f'{self.language}' \
               f'|' \
               f'{self.nick or self.cmdr}' \
               f']' \
               f''

    @property
    def details(self) -> str:
        cr = f' {types.Color.RED.value}CR{types.Color.DEFAULT.value}' \
            if self.is_cr else ''
        active = f' {types.Color.LIGHT_GRAY.value}' \
                 f'INACTIVE' \
                 f'{types.Color.DEFAULT.value}' \
            if not self.is_active else ''
        result = f'{self}{cr}{active}'

        if self.rats:
            result += f'\n' + '\n'.join(rat.details() for rat in self.rats)
        elif self.jump_calls:
            result += f'\n' + '\n'.join(self.jump_calls)

        result += f'{types.Color.LIGHT_GRAY.value}\n' \
                  f'{self._last_quote}' if self._last_quote else ''

        result += '\n'
        return result

    @property
    def state(self):
        return self._state

    @property
    def num(self):
        return self._num

    @property
    def cmdr(self):
        return self._cmdr

    @property
    def is_active(self):
        return self._is_active

    @property
    def is_cr(self):
        return self._is_cr

    @property
    def nick(self):
        return self._nick

    @property
    def language(self):
        return self._language

    @property
    def platform(self):
        return self._platform

    @property
    def system(self):
        return self._system

    @property
    def landmark(self):
        return self._landmark

    @property
    def last_quote(self):
        return self._last_quote

    @property
    def rats(self):
        return tuple(self._rats)

    @property
    def jump_calls(self):
        return tuple(self._jump_calls)

    def delete(self):
        self._state.delete_case(self)

    def find_rat(self, query: str) -> t.Optional[Rat]:
        # Immediately return if query is empty.
        if not query:
            return

        try:
            return next(
                r for r in self.rats if utils.nicks_match(
                    r.nick, query,
                ) or r.cmdr.lower == query.lower()
            )
        except StopIteration:
            pass

    def put_rat(self, **kwargs):
        # Strip all formatting from input.
        for k, v in kwargs.items():
            if isinstance(v, str):
                kwargs[k] = utils.strip(v)

        print(kwargs)
        # Try to find and update existing rat.
        rat = self.find_rat(
            kwargs.get('nick'),
        ) or self.find_rat(kwargs.get('cmdr'))
        if rat:
            for k, v in kwargs.items():
                setattr(rat, f'_{k}', v)
            self.state.updated()
            return rat

        # Create new rat.
        kwargs = {
            f'_{k}': v for k, v in kwargs.items()
        }
        rat = Rat(case=self, **kwargs)
        self._rats.append(rat)
        self.state.updated()
        return rat

    def jumps_called(self, text):
        self._jump_calls.append(text)
        self.state.updated()

    def delete_rat(self, rat: Rat):
        self._rats.remove(rat)
        self.state.updated()


@dataclass
class State:
    _cases: t.List[Case] = field(default_factory=list)
    _leads: t.Dict[str, Case] = field(default_factory=dict)

    def __str__(self):
        return f'State: {len(self._cases)} cases, {len(self._leads)} leads'

    @property
    def details(self) -> str:
        return '\n'.join(x.details for x in self.cases)

    @property
    def cases(self):
        return tuple(sorted(self._cases, key=lambda x: (
            not x.is_active,
            x.is_cr,
            x.num,
        )))

    @property
    def leads(self):
        return tuple(self._leads)

    @property
    def _free_case_num(self) -> int:
        return max(max([int(c.num) for c in self.cases] + [0]), 100) + 1

    def _build_leads(self):
        self._leads = {}

        for case in self.cases:
            self._leads[case.cmdr] = case
            self._leads[case.nick] = case
            self._leads[f' {case.num}'] = case
            self._leads[f'#{case.num}'] = case
            self._leads[f'case{case.num}'] = case
            self._leads[f'case {case.num}'] = case
            for rat in case.rats:
                self._leads[rat.cmdr] = case
                self._leads[rat.nick] = case

        # Remove None and empty keys from the dict.
        bad_keys = [k for k in self._leads if k is None or k == '']
        list(map(lambda x: self._leads.pop(x), bad_keys))

    def _render(self):
        context.clear(config.CASES_WINDOW_NAME)
        context.print(config.CASES_WINDOW_NAME, self.details)

    def updated(self):
        self._build_leads()
        self._render()

    def put_case(self, **kwargs):
        # Strip all formatting from input.
        for k, v in kwargs.items():
            if isinstance(v, str):
                kwargs[k] = utils.strip(v)

        # Try to find and update existing case.
        case = self.find_case(kwargs.get('num')) or \
               self.find_case(kwargs.get('cmdr')) or \
               self.find_case(kwargs.get('nick'))
        if case:
            for k, v in kwargs.items():
                setattr(case, f'_{k}', v)
            self.updated()
            return case

        # Create new case.
        # Fix case num.
        if kwargs.get('num') is None:
            kwargs['num'] = str(self._free_case_num)
        # Create cmdr irc nick.
        if 'nick' not in kwargs:
            kwargs['nick'] = kwargs['cmdr'].replace(' ', '_')
        kwargs = {
            f'_{k}': v for k, v in kwargs.items()
        }
        case = Case(_state=self, **kwargs)
        self._cases.append(case)
        self.updated()
        return case

    def find_case(self, query: str) -> t.Optional[Case]:
        # Immediately return if query is empty.
        if not query:
            return

        # Convert '#num' query to 'num' query.
        query = query.lstrip('#')

        # Try to find case by:
        # case number
        try:
            return next(
                c for c in self.cases if c.num == query
            )
        except StopIteration:
            pass

        # case nick
        try:
            return next(
                c for c in self.cases if utils.nicks_match(c.nick, query)
            )
        except StopIteration:
            pass

        # case cmdr
        try:
            return next(
                c for c in self.cases if c.cmdr.lower() == query.lower()
            )
        except StopIteration:
            pass

        # # rat nick
        # try:
        #     for case in self.cases:
        #         next(
        #             r for r in case.rats if utils.nicks_match(
        #                 r.nick, query,
        #             )
        #         )
        #         return case
        # except StopIteration:
        #     pass
        #
        # # rat cmdr
        # try:
        #     for case in self.cases:
        #         next(
        #             r for r in case.rats if r.cmdr.lower() == query.lower()
        #         )
        #         return case
        # except StopIteration:
        #     pass

    def delete_case(self, case: Case):
        self._cases.remove(case)
        self.updated()

    def process_quote(self, msg: str):
        try:
            case = next(
                case for lead, case in self._leads.items(
                ) if lead.lower() in msg.lower()
            )
            context.print(f'#{case.num}', msg)
            return case
        except StopIteration:
            pass


state = State()
