import hexchat


# noinspection PyShadowingBuiltins
def _create(name: str) -> 'hexchat.Context':
    # noinspection SpellCheckingInspection
    hexchat.command(f'newserver -noconnect {name}')
    return hexchat.find_context(server=name)


def _get(name: str) -> 'hexchat.Context':
    ctx = hexchat.find_context(server=name)
    if not ctx:
        ctx = _create(name)
    return ctx


def clear(name: str):
    _get(name).command('clear')


# noinspection PyShadowingBuiltins
def print(name, text: str):
    _get(name).prnt(text)


def delete(name: str):
    ctx = hexchat.find_context(server=name)
    ctx.command(f'close')
