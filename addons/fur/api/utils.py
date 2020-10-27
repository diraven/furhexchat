# import typing as t
import winsound

import hexchat
from . import const


# noinspection PyShadowingBuiltins
def print(text: str, prefix: str = '*', context: str = None):
    if prefix:
        text = f'{prefix}\t{text}'
    if context is None:
        hexchat.prnt(text)
    else:
        ctx = hexchat.find_context(server=context)
        if not ctx:
            hexchat.command(f'newserver -noconnect {context}')
        ctx = hexchat.find_context(server=context)
        ctx.prnt(text)


# noinspection PyShadowingBuiltins
def print_error(text: str):
    ctx = hexchat.get_context()
    ctx.prnt(f'{const.COLOR.RED}{text}')


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


def beep():
    winsound.PlaySound(
        '.\\config\\addons\\fur\\notification.wav',
        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT,
    )
