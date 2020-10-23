from . import api
from .aliases import *
from .commands import *
from .hooks import *

# Sync cases with bot on plugin reload.
fr_ctx: 'api.hexchat.Context' = api.hexchat.find_context(channel='#fuelrats')
if fr_ctx:
    api.send_message('MechaSqueak[BOT]', '!list')


# Sync cases with bot on #fuelrats join.
# noinspection PyUnusedLocal
@api.hook_print(events=[api.types.Event.YOU_JOIN])
def get_cases_list(message, **kwargs):
    if message == '#fuelrats':
        api.state.updated()
        api.send_message('MechaSqueak[BOT]', '!list')
