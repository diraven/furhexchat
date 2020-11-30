from . import _hooks, _commands
from ._api import API


# noinspection PyShadowingNames
def init(api):
    _hooks.init(api)
    _commands.init(api)

    api.send_command('furcasesync')  # aytosync cases on plugin load
