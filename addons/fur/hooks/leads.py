from .. import api


# noinspection PyUnusedLocal
@api.hook_print()
def leads(author: str, message: str, **kwargs):
    case = api.check_leads(f'{author} {message}')
    if case:
        api.print(
            f'{api.types.Color.LIGHT_GREEN.value}>'
            f'{api.types.Color.DEFAULT.value} {api.fmt.case(case)}'
        )
        api.add_quote(case, f'<{author}> {message}')
