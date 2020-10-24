# import typing as t
import hexchat
from . import const


# noinspection PyShadowingBuiltins
def print(text: str):
    hexchat.prnt(text)


def emit_print(
    text: str, *,
    event: str = const.EVENT.YOUR_MESSAGE,
    prefix: str = '',
    mode: str = '',
    context: str = None,
):
    if context is None:
        hexchat.emit_print(event, prefix, text, mode)
    else:
        ctx = hexchat.find_context(server=context)
        if not ctx:
            hexchat.command(f'newserver -noconnect {context}')
        ctx = hexchat.find_context(server=context)
        ctx.emit_print(event, prefix, text, mode)


def command(text: str):
    hexchat.command(text)


def message(target: str, text: str):
    command(f'MSG {target} {text}')


def reply(text: str):
    ctx = hexchat.get_context()
    message(ctx.get_info("channel"), text)


def nicks_match(n1, n2) -> bool:
    return hexchat.nickcmp(n1, n2) == 0


def strip(text: str) -> str:
    return hexchat.strip(text.strip())


def close_context(name: str):
    ctx = hexchat.find_context(server=name)
    if ctx:
        ctx.command(f'close')
