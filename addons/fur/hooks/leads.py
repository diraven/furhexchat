from .. import api


# noinspection PyUnusedLocal
@api.hook_print()
def handler(author: str, message: str, **kwargs):
    case = api.state.process_quote(f'{author} {message}')
    if case:
        api.print(
            f'{api.types.Color.LIGHT_GREEN.value}>'
            f'{api.types.Color.DEFAULT.value} {case}'
        )

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

        rat = case.put_rat(nick=author, **calls)
