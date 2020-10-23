import re

from .. import api

_jumps_rexp = re.compile(r'(?P<count>\d+)\s*j(?:ump)?s?')


# noinspection PyUnusedLocal
@api.hook_print()
def handler(author: str, message: str, **kwargs):
    case = api.state.process_quote(f'<{author}> {message}')
    if case:
        # api.print(
        #     f'{api.types.Color.LIGHT_GREEN.value}>'
        #     f'{api.types.Color.DEFAULT.value} {case}'
        # )

        api.state.put_case(num=case.num, last_quote=f'<{author}> {message}')

        if _jumps_rexp.search(message):
            case.jumps_called(f'<{author}> {message}')

        rat = case.find_rat(author)
        if rat:
            calls = {}
            for call in [
                'fr',
                'prep',
                'pos',
                'wr',
                'bc',
                'fuel',
            ]:
                if f'{call}+' in message.lower():
                    calls[call] = True
                if f'{call}-' in message.lower():
                    calls[call] = False
            if calls:
                case.put_rat(nick=author, **calls)
