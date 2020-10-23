import hexchat

from . import config, format, state, types


def open_window(name: str) -> 'hexchat.Context':
    hexchat.command(f'newserver -noconnect {name}')
    return hexchat.find_context(server=name)


def get_window_context(name: str) -> 'hexchat.Context':
    ctx = hexchat.find_context(server=name)
    if not ctx:
        ctx = open_window(name)
    return ctx


def render():
    ctx = get_window_context(config.CASES_WINDOW_NAME)
    data = format.state(state.get_state())
    ctx.command('clear')
    ctx.emit_print(types.Event.GENERIC_MESSAGE.value, data)
