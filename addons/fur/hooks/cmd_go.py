import re

from .. import api


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!(?:go|assign) [^\s]+ [^\s]+'),
)
def handler(message: str, **kwargs):
    args = message.split()
    case = api.state.find_case(args[1])
    if not case:
        api.print(f'Case not found: {args[1]}')

    for rat_nick in args[2:]:
        case.put_rat(nick=rat_nick)
