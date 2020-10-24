# import typing as t

import hexchat


# noinspection PyShadowingBuiltins
def print(text: str):
    hexchat.prnt(text)


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

# def strip(text: str) -> str:
#     return hexchat.strip(text)
#
#

# def show_message(*, msg: str, author: str = '', mode: str = ''):
#     hexchat.emit_print("Custom Message", author, msg, mode)

# noinspection PyShadowingBuiltins
# def print(what: t.Any, label: str = types.Label.INFO.value):
# for line in str(what).splitlines():
#     hexchat.emit_print(
#         types.Event.CHANNEL_MESSAGE.value,
#         f'{label} {types.Color.LIGHT_GREEN.value}>',
#         line,
#     )
