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

    return f'' \
           f'{color.value}' \
           f'#{obj["num"]}' \
           f'{types.Color.DEFAULT.value}-' \
           f'[' \
           f'{obj["language"]}' \
           f'|' \
           f'{platform(obj["platform"])}' \
           f'|' \
           f'{obj["nick"] or obj["cmdr"]}' \
           f']' \
           f''


def case_detail(obj: types.Case) -> str:
    cr = f' {types.Color.RED.value}CR{types.Color.DEFAULT.value}' \
        if obj['is_cr'] else ''
    active = f' {types.Color.LIGHT_GRAY.value}' \
             f'INACTIVE' \
             f'{types.Color.DEFAULT.value}' \
        if not obj['is_active'] else ''
    return f'{case(obj)}{cr}{active}'


def state(obj: types.State) -> str:
    return '\n'.join(
        map(lambda x: case_detail(x), sorted(obj['cases'], key=lambda x: (
            not x['is_active'],
            x['is_cr'],
            x['num'],
        )))
    )
