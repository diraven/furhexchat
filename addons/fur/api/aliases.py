"""
Cheat sheet:
/command 1 2 3 "4 5"
word: ['command', '1', '2', '3']
word_eol: ['command 1 2 3', '1 2 3', '2 3', '3']
"""

import typing as t

import hexchat

LANGUAGES = ['', 'de', 'ru', 'es', 'fr', 'pt', 'cn', 'it']
PLATFORMS = {
    '': 'pc',
    'pc': 'pc',
    'x': 'x',
    'ps': 'ps',
}


def _handler(word: t.List[str], word_eol: t.List[str], userdata):
    (name, command, template, arguments) = userdata

    # Enforce correct command usage.
    if len(word) < len(arguments) + 1:
        hexchat.prnt(
            f'\00304Usage: {name}'
            f'{" ".join(a.upper() for a in arguments)}',
        )

    message = template.format(
        word=word,
        word_eol=word_eol,
        command=command,
    )

    # Send the message.
    ctx = hexchat.get_context()
    for line in message.splitlines():
        ctx.command(f'MSG {ctx.get_info("channel")} {line}')

    return hexchat.EAT_ALL


def register_alias(
    name: str,
    *,
    command: str = None,
    template: t.Union[str, t.Dict[str, str]] = None,
    arguments: t.List[str] = None,
    translated=False,
    platformed=False,
):
    languages = LANGUAGES if translated else ['']
    platforms = PLATFORMS if platformed else {'': ''}

    for platform in platforms:
        for language in languages:
            # Get message template.
            if isinstance(template, dict):
                template = template.get(language) or template.get('')

            userdata = (
                name,
                f'{platform}{command or name}'
                f'{f"-{language}" if language else ""}',
                template or '!{command} {word_eol[1]}',
                arguments or ['nick'],
            )

            hexchat.hook_command(
                name=f'{platform}{name}{f"-{language}" if language else ""}',
                callback=_handler,
                help=f'{name} '
                     f'{" ".join(a.upper() for a in arguments or ["nick"])}',
                userdata=userdata,
            )
