from . import _aliases, _hooks, _commands
from ._api import API


# noinspection PyShadowingNames
def init(api):
    _aliases.init(api)
    _hooks.init(api)
    _commands.init(api)

# ctx = hexchat.find_context(server=api.LOG_CONTEXT_NAME)
# if ctx:
#     api.message('MechaSqueak[BOT]', '!list')
#
#
# # Sync cases with bot on #fuelrats join.
# # noinspection PyUnusedLocal
# @api.hook_print(match_events=[api.Event.you_join])
# def get_cases_list(message, **kwargs):
#     if message == '#fuelrats':
#         api.message('MechaSqueak[BOT]', '!list')
