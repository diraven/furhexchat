# import typing as t

import hexchat


def command(text: str):
    hexchat.command(text)


def send_message(target: str, message: str):
    command(f'MSG {target} {message}')

# def reply(message: str):
#     context = hexchat.get_context()
#     send_message(context.get_info("channel"), message)
#
#
# def nicks_match(n1, n2) -> bool:
#     return hexchat.nickcmp(n1, n2) == 0
#
#
# def strip(text: str) -> str:
#     return hexchat.strip(text)
#
#
# # noinspection PyShadowingBuiltins
# def print(text: str):
#     hexchat.prnt(text)
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
