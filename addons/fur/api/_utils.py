# import typing as t
import winsound

import hexchat
from ._const import Event, TERMINATOR, Color


# noinspection PyShadowingBuiltins
def print(text: str, prefix: str = '*', context: 'hexchat.Context' = None):
    text = f'{prefix}\t{text}' if prefix else text
    context.prnt(text) if context else hexchat.prnt(text)


def log(
    text: str, *,
    prefix: str = '',
    event: Event = Event.channel_message,
    mode: str = '',
):
    text = f'{text}{Color.gray.value}{TERMINATOR}'
    ctx_name = 'log'
    ctx = hexchat.find_context(server=ctx_name)
    if not ctx:
        hexchat.command(f'newserver -noconnect {ctx_name}')
    ctx = hexchat.find_context(server=ctx_name)
    ctx.emit_print(event.value, prefix, text, mode)


# noinspection PyShadowingBuiltins
def print_error(text: str):
    ctx = hexchat.get_context()
    ctx.prnt(f'{Color.red}{text}')


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


def beep():
    winsound.PlaySound(
        '.\\config\\addons\\fur\\notification.wav',
        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT,
    )
