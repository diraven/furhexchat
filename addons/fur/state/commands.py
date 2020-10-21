from .state import state
from .. import utils


@utils.hook_command(names=('state', 'status'))
def print_state(**kwargs):
    utils.print(state)
