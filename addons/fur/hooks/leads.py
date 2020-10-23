from .. import api


# noinspection PyUnusedLocal
@api.hook_print(
    events=[
        api.types.Event.CHANNEL_MESSAGE,
        api.types.Event.CHANNEL_MSG_HILIGHT,
    ],
)
def handler(author: str, message: str, **kwargs):
    case = api.state.process_quote(f'{author} {message}')
    if case:
        api.print(
            f'{api.types.Color.LIGHT_GREEN.value}>'
            f'{api.types.Color.DEFAULT.value} {case}'
        )
        api.state.process_quote(case, f'<{author}> {message}')
