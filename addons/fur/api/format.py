import typing as t

from . import types


def dict_updates(dict1: t.Dict, dict2: t.Dict) -> str:
    return '\n'.join([
        f'{k}: {dict1[k]} -> {v}' for k, v in dict2.items() if dict1[k] != v
    ])


def platform(obj: types.Platform) -> str:
    color = types.Color.PURPLE
    if obj == types.Platform.PLAYSTATION:
        color = types.Color.ROYAL_BLUE
    if obj == types.Platform.XBOX:
        color = types.Color.GREEN
    return f'{color.value}{obj.name}{types.Color.DEFAULT.value}'


def case(obj: types.Case) -> str:
    color = types.Color.SUCCESS
    if obj['is_cr']:
        color = types.Color.ERROR
    if not obj['is_active']:
        color = types.Color.LIGHT_GRAY

    return f'{types.Color.DEFAULT.value}[' \
           f'{obj["language"]}' \
           f'|' \
           f'{platform(obj["platform"])}' \
           f'|' \
           f'{color.value}' \
           f'{obj["nick"] or obj["cmdr"]}#{obj["num"]}' \
           f'{types.Color.DEFAULT.value}]'


def case_detail(obj: types.Case) -> str:
    cr = f' {types.Color.Red}CR{types.Color.DEFAULT}' if obj['is_cr'] else ''
    active = f' {types.Color.LIGHT_GRAY}INACTIVE{types.Color.DEFAULT}' \
        if not obj['is_active'] else ''
    return f'{case(obj)}{cr}{active}'


def state(obj: types.State) -> str:
    return 'Current State:\n' + '\n'.join(
        map(lambda x: case(x), sorted(obj['cases'], key=lambda x: (
            not x['is_active'],
            x['is_cr'],
            x['num'],
        )))
    )
