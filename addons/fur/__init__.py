from . import api
from .aliases import *
from .commands import *

# Sync cases with bot on plugin reload.
fr_ctx: 'api.hexchat.Context' = api.hexchat.find_context(channel='#fuelrats')
if fr_ctx:
    api.send_message('MechaSqueak[BOT]', '!list')


# Sync cases with bot on #fuelrats join.
# noinspection PyUnusedLocal
@api.hook_print(events=[api.types.Event.YOU_JOIN])
def get_cases_list(message, **kwargs):
    if message == '#fuelrats':
        api.send_message('MechaSqueak[BOT]', '!list')

# def youpart_cb(word, word_eol, userdata, attributes):
#     print(dir(attributes.time))
#     return hexchat.EAT_HEXCHAT
#
#
# ctx: 'hexchat.Context' = hexchat.find_context(server='FurBoard')
# ctx.prnt('asdf')
#
# hexchat.hook_print_attrs(utils.Event.PRIVATE_MESSAGE_TO_DIALOG.value,
#     youpart_cb)
# attrs->server_time_utc = 1342224702;
# hexchat_emit_print (ph, attrs, "Channel Message", "John", "Hi there", "@",
# NULL);
# hexchat_event_attrs_free (ph, attrs);

# %C18%H<%H$4$3$1%H>%H%O$t$2
# %C18%H<%H$3$1%H>%H%O$t$2
