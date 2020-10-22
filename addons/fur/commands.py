from . import api


# noinspection PyUnusedLocal
@api.hook_command(names=('state', 'status'))
def print_state(**kwargs):
    api.format.state(api.get_state())
