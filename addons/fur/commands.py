import typing as t

from . import api


# noinspection PyUnusedLocal
@api.hook_command(names=('render',))
def render(**kwargs) -> t.Optional[api.types.Eat]:
    api.gui.render_dashboard()
    return api.types.Eat.ALL
