import typing as t

from . import api


# noinspection PyUnusedLocal
@api.hook_command(names=('state', 'status'))
def print_state(**kwargs) -> t.Optional[api.types.Eat]:
    api.gui.update_board()
    return api.types.Eat.ALL
