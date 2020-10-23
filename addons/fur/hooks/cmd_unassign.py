import re

from .. import api


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!unassign [^\s]+ [^\s]+'),
)
def handler(message: str, **kwargs):
    args = message.split()
    case = api.state.find_case(args[1])
    if not case:
        return

    for rat_nick in args[2:]:
        rat = case.find_rat(rat_nick)
        if rat:
            rat.delete()
