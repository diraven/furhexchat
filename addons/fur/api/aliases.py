import typing as t

import hexchat
from . import types, utils


def _handler(word: t.List[str], word_eol: t.List[str],
             userdata: t.Dict):
    alias = userdata['alias']
    command = userdata['command']
    arguments = userdata['arguments']
    messages = userdata['messages']
    language = userdata['language']
    platform = userdata['platform']

    if len(word) < len(arguments) + 1:
        print(
            f'{types.Color.ERROR.value}{alias} '
            f'{" ".join(a.upper() for a in arguments)}',
        )
        return hexchat.EAT_ALL

    for message in messages:
        if isinstance(message, dict):
            message = message.get(language.value.id) or message.get('')
        cmd_prefix = platform.value.prefix
        cmd_postfix = f'-{language.value.postfix}' if \
            language.value.postfix else ''
        cmd = f'!{cmd_prefix}{command}{cmd_postfix}'
        utils.reply(message.format(
            cmd=cmd,
            word=word,
            word_eol=word_eol,
        ))

    return hexchat.EAT_ALL


def register_alias(
    *,
    name: str,
    messages: t.List[t.Union[str, t.Dict[str, str]]] = None,
    arguments: t.List[str] = None,
    command: str = '',
    translated=False,
    platformed=False,
):
    if not arguments:
        arguments = ['ircname']

    if messages is None and command:
        messages = ['{cmd} {word_eol[1]}']

    languages = types.Language if translated else types.NoLanguage
    platforms = types.Platform if platformed else types.NoPlatform

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
