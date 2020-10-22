import typing as t

from . import api


# noinspection PyUnusedLocal
@api.hook_command(names=('state', 'status'))
def print_state(**kwargs) -> t.Optional[api.types.Eat]:
    api.print(api.format.state(api.get_state()))
    return api.types.Eat.ALL
