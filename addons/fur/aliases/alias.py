import collections
import typing

import hexchat
from .. import utils

Alias = collections.namedtuple('Alias', [
    'name',
    'command',
    'arguments',
    'preamble',
    'translated',
    'platformed',
])


def _handler(word: typing.List[str], word_eol: typing.List[str],
             userdata: typing.Dict):
    alias = userdata['alias']
    command = userdata['command']
    arguments = userdata['arguments']
    messages = userdata['messages']
    language = userdata['language']
    platform = userdata['platform']

    if len(word) < len(arguments) + 1:
        utils.print(
            f'{utils.Color.DANGER.value}{alias} '
            f'{" ".join(a.upper() for a in arguments)}',
        )
        return hexchat.EAT_ALL

    context = hexchat.get_context()
    for message in messages:
        if isinstance(message, dict):
            message = message.get(language.value.id) or message.get('')
        cmd_prefix = platform.value.prefix
        cmd_postfix = f'-{language.value.postfix}' if \
            language.value.postfix else ''
        cmd = f'!{cmd_prefix}{command}{cmd_postfix}'
        utils.send_message(context, message.format(
            cmd=cmd,
            word=word,
            word_eol=word_eol,
        ))

    return hexchat.EAT_ALL


def register_alias(
    *,
    name: str,
    messages: typing.List[typing.Union[str, typing.Dict[str, str]]] = None,
    arguments: typing.List[str] = None,
    command: str = '',
    translated=False,
    platformed=False,
):
    if not arguments:
        arguments = ['ircname']

    if messages is None and command:
        messages = ['{cmd} {word_eol[1]}']

    languages = utils.Language if translated else utils.NoLanguage
    platforms = utils.Platform if platformed else utils.NoPlatform

    for platform in platforms:
        for language in languages:
            prefix = platform.value.id
            postfix = f'-{language.value.id}' if language.value.id else ''
            alias = f'{prefix}{name}{postfix}'
            hexchat.hook_command(
                name=alias,
                callback=_handler,
                userdata={
                    'alias': alias,
                    'command': command,
                    'arguments': arguments,
                    'messages': messages,
                    'language': language,
                    'platform': platform,
                },
                help=f'{alias} {" ".join(a.upper() for a in arguments)}',
            )
