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

        is_active: typing.Optional[bool] = True,
        is_cr: typing.Optional[bool] = False,

        landmark: typing.Optional[str] = '',
        language: typing.Optional[str] = '',
        nick: typing.Optional[str] = '',
        num: typing.Optional[int] = None,
        platform_name: typing.Optional[str] = '',
        system: typing.Optional[str] = '',
    ):
        self.cmdr = utils.clean(cmdr)

        self.is_active = is_active
        self.is_cr = is_cr

        self.landmark = utils.clean(landmark)
        self.language = language
        if not nick:
            nick = self.cmdr.replace(' ', '_')
        self.nick = utils.clean(nick)
        self.num = num
        self.platform = _platforms[platform_name.lower()]
        self.system = utils.clean(system)

    def __str__(self) -> str:
        color = utils.Color.WARNING
        if self.is_cr:
            color = utils.Color.DANGER
        if not self.is_active:
            color = utils.Color.LIGHT_GRAY

        return f'{color.value}' \
               f'[ #{self.num} {self.nick or self.cmdr} ]' \
               f'{utils.Color.DEFAULT.value}'

    def format(self) -> str:
        return ' '.join(filter(lambda x: x is not None, [
            str(self),
            self.format_platform(),
            self.format_is_cr(),
            self.format_is_active(),
        ]))

    def format_is_cr(self) -> str:
        return f'({utils.Color.DANGER.value}CR{utils.Color.DEFAULT.value})' \
            if self.is_cr else None

    def format_is_active(self) -> str:
        return '(INACTIVE)' if not self.is_active else None

    def format_platform(self) -> str:
        color = utils.Color.LIGHT_GRAY
        if self.platform == utils.Platform.PLAYSTATION:
            color = utils.Color.ROYAL_BLUE
        if self.platform == utils.Platform.XBOX:
            color = utils.Color.GREEN
        return f'({color.value}{self.platform.name}' \
               f'{utils.Color.DEFAULT.value})'

    def update(self, case: 'Case'):
        for prop in (
            'cmdr',
            'is_cr',
            'landmark',
            'platform',
            'language',
            'nick',
            'num',
            'system',
        ):
            value = getattr(case, prop)
            original_value = getattr(self, prop)
            if value is not None and value != original_value:
                setattr(self, prop, value)
                utils.print(
                    f'{utils.Color.WARNING.value}{self}.{prop}: '
                    f'"{original_value}" -> "{value}"'
                )
