from . import api
from .aliases import *
from .commands import *
from .hooks import *

ctx = api.utils.get_context(api.const.MAIN_CONTEXT_NAME)
if ctx:
    api.message('MechaSqueak[BOT]', '!list')


# Sync cases with bot on #fuelrats join.
# noinspection PyUnusedLocal
@api.hooks.print(match_events=(api.const.Event.you_join,))
def get_cases_list(message, **kwargs):
    if message == '#fuelrats':
        api.message('MechaSqueak[BOT]', '!list')
