import collections
import enum
import typing

import winsound

import hexchat


def beep():
    winsound.MessageBeep()


def send_message(context: 'hexchat.Context', message: str):
    context.command(f'MSG {context.get_info("channel")} {message}')


def show_error(text: str):
    hexchat.prnt(f'\00304 {text}')


