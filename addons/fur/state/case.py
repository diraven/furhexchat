import typing

from .. import utils


class Rat:
    pass


_platforms = {
    'pc': utils.Platform.PC,
    'playstation': utils.Platform.PLAYSTATION,
    'playstation4': utils.Platform.PLAYSTATION,
    'ps': utils.Platform.PLAYSTATION,
    'ps4': utils.Platform.PLAYSTATION,
    'xbox': utils.Platform.XBOX,
    'xb': utils.Platform.XBOX,
}


class Case:
    def __init__(
        self,
        cmdr: str,

        is_active: typing.Optional[bool] = None,
        is_cr: typing.Optional[bool] = None,

        landmark: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        nick: typing.Optional[str] = None,
        num: typing.Optional[int] = None,
        platform_name: typing.Optional[str] = None,
        system: typing.Optional[str] = None,
    ):
        self.cmdr = utils.clean(cmdr)

        self.is_active = is_active if is_active is not None else True
        self.is_cr = is_cr if is_cr is not None else False

        self.landmark = utils.clean(landmark or '')
        self.language = language or ''
        if not nick:
            nick = self.cmdr.replace(' ', '_')
        self.nick = utils.clean(nick or '')
        self.num = num
        self.platform = _platforms[utils.clean(platform_name or '').lower()]
        self.system = utils.clean(system or '')

    def __str__(self) -> str:
        color = utils.Color.SUCCESS
        if self.is_cr:
            color = utils.Color.ERROR
        if not self.is_active:
            color = utils.Color.LIGHT_GRAY

        return f'{utils.Color.DEFAULT.value}{self.format_language()}' \
               f'{utils.Color.DEFAULT.value}|' \
               f'{self.format_platform()}' \
               f'{utils.Color.DEFAULT.value}|' \
               f'{color.value}{self.nick or self.cmdr}|#{self.num}'

    def print(self):
        utils.print(
            ' '.join(filter(lambda x: x is not None, [
                self.format_platform(),
                self.format_is_cr(),
                self.format_is_active(),
            ])),
            str(self)
        )

    def format_is_cr(self) -> str:
        return f'{utils.Color.ERROR.value}CR{utils.Color.DEFAULT.value}' \
            if self.is_cr else None

    def format_is_active(self) -> str:
        return 'INACTIVE' if not self.is_active else None

    def format_platform(self) -> str:
        color = utils.Color.LIGHT_GRAY
        if self.platform == utils.Platform.PLAYSTATION:
            color = utils.Color.ROYAL_BLUE
        if self.platform == utils.Platform.XBOX:
            color = utils.Color.GREEN
        return f'{color.value}{self.platform.name}' \
               f'{utils.Color.DEFAULT.value}'

    def format_language(self) -> str:
        return f'{self.language}' if self.language else 'en'

    def update(self, case: 'Case'):
        for name in (
            'cmdr',
            'is_cr',
            'landmark',
            'platform',
            'language',
            'nick',
            'num',
            'system',
        ):
            self.set_prop(name, getattr(case, name))

    def set_prop(self, name: str, value: any):
        original_value = getattr(self, name)
        if value is not None and value != original_value:
            utils.print(
                f'{name}: "{original_value}" -> "{value}"',
                label=str(self),
            )
            setattr(self, name, value)
