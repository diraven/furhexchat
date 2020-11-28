from . import _aliases, _hooks, _commands
from ._api import API


# noinspection PyShadowingNames
def init(api):
    _aliases.init(api)
    _hooks.init(api)
    _commands.init(api)

    api.send_command('furcasesync')  # aytosync cases on plugin load
