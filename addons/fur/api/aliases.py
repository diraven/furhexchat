"""
Cheat sheet:
/command 1 2 3 "4 5"
word: ['command', '1', '2', '3']
word_eol: ['command 1 2 3', '1 2 3', '2 3', '3']
"""

import typing as t

from . import utils, const, hooks

LANGUAGES = ['', 'de', 'ru', 'es', 'fr', 'pt', 'cn', 'it']
PLATFORMS = {
    '': 'pc',
    'pc': 'pc',
    'x': 'x',
    'ps': 'ps',
}


def _handler(args: t.List[str], data):
    (name, command, template, arguments) = data

    # Enforce correct command usage.
    if len(args) < len(arguments):
        utils.print(
            f'\00304Usage: {name}'
            f'{" ".join(a.upper() for a in arguments)}',
        )

    message = template.format(
        first_arg=args[0],
        rest_args=' '.join(args[1:]) if len(args) > 0 else '',
        command=command,
    )

    # Send the message.
    for line in message.splitlines():
        utils.reply(line)

    return const.EAT.ALL


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

    for alias_platform, command_platform in platforms.items():
        for language in languages:
            # Get message template.
            if isinstance(template, dict):
                template = template.get(language) or template.get('')

            userdata = (
                name,
                f'{command_platform}{command or name}'
                f'{f"-{language}" if language else ""}',
                template or '!{command} {first_arg} {rest_args}',
                arguments or ['nick'],
            )

            hooks.command(
                names=[
                    f'{alias_platform}{name}'
                    f'{f"-{language}" if language else ""}',
                ],
                description=f'{name} '
                            f'{" ".join(a for a in arguments or ["nick"])}',
                userdata=userdata,
            )(_handler)
