import collections
import enum
import typing

import hexchat
from .utils import send_message, show_error

Alias = collections.namedtuple('Alias', [
    'name',
    'command',
    'arguments',
    'preamble',
    'translated',
    'platformed',
])

LanguageData = collections.namedtuple('LanguageData', ['id', 'postfix'])


@enum.unique
class Language(enum.Enum):
    DEFAULT = LanguageData('', '')
    DE = LanguageData('de', 'de')
    RU = LanguageData('ru', 'ru')
    ES = LanguageData('es', 'es')
    FR = LanguageData('fr', 'fr')
    PT = LanguageData('pt', 'pt')
    CN = LanguageData('cn', 'cn')
    IT = LanguageData('it', 'it')


@enum.unique
class NoLanguage(enum.Enum):
    DEFAULT = LanguageData('', '')


PlatformData = collections.namedtuple('PlatformData', ['id', 'prefix'])


@enum.unique
class Platform(enum.Enum):
    DEFAULT = PlatformData('', 'pc')
    PC = PlatformData('pc', 'pc')
    XBOX = PlatformData('x', 'x')
    PLAYSTATION = PlatformData('ps', 'ps')


@enum.unique
class NoPlatform(enum.Enum):
    DEFAULT = PlatformData('', '')


def _handler(word: typing.List[str], word_eol: typing.List[str],
             userdata: typing.Dict):
    alias = userdata['alias']
    command = userdata['command']
    arguments = userdata['arguments']
    messages = userdata['messages']
    language = userdata['language']
    platform = userdata['platform']

    if len(word) < len(arguments) + 1:
        show_error(f'{alias} {" ".join(a.upper() for a in arguments)}')
        return hexchat.EAT_ALL

    context = hexchat.get_context()
    for message in messages:
        if isinstance(message, dict):
            message = message.get(language.value.id) or message.get('')
        cmd_prefix = platform.value.prefix
        cmd_postfix = f'-{language.value.postfix}' if \
            language.value.postfix else ''
        cmd = f'!{cmd_prefix}{command}{cmd_postfix}'
        send_message(context, message.format(
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

    languages = Language if translated else NoLanguage
    platforms = Platform if platformed else NoPlatform

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
