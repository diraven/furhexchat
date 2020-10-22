from . import api


# noinspection PyUnusedLocal
@api.hook_command(names=('state', 'status'))
def print_state(**kwargs):
    api.reply(api.format.state(api.get_state()))
    return api.types.Eat.ALL
