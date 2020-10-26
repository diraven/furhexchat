import re
import typing as t

from .. import api
from ..api.const import COLOR

quote_matcher = re.compile(r'((?:#|case ?)(?P<query>\d+))', re.IGNORECASE)
command_matcher = re.compile(r'(![\w-]+\s+(?P<query>[\w_-]+))', re.IGNORECASE)

highlighters: t.Dict[t.Pattern, str] = {
    re.compile(
        r'((?:#|case ?)(?P<case_num>\d+)(?:[^\w]|$))',
        re.IGNORECASE): COLOR.INFO,
    re.compile(r'(\w+\+(?:[^\w]|$))', re.IGNORECASE): COLOR.SUCCESS,
    re.compile(r'(\w+-(?:[^\w]|$))', re.IGNORECASE): COLOR.DANGER,
    re.compile(r'(\w+conf(?:[^\w]|$))', re.IGNORECASE): COLOR.SUCCESS,
    re.compile(r'(\d+\s?k?ls(?:[^\w]|$))', re.IGNORECASE): COLOR.WARNING,
    re.compile(
        r'(\d+\s*j(?:umps?)?(?:[^\w]|$))', re.IGNORECASE): COLOR.WARNING,
    re.compile(
        r'(\s(?:open|pg|mm|ez)(?:[^\w]|$))', re.IGNORECASE): COLOR.WARNING,
    re.compile(r'(stdn(?:[^\w]|$))', re.IGNORECASE): COLOR.DANGER,
}


# noinspection PyUnusedLocal
@api.hooks.print(
    match_events=[
        api.const.EVENT.CHANNEL_MESSAGE,
        api.const.EVENT.CHANNEL_MSG_HILIGHT,
        api.const.EVENT.PRIVATE_MESSAGE_TO_DIALOG,
        api.const.EVENT.PRIVATE_MESSAGE,
    ],
    priority=api.const.PRIORITY.LOWEST,
)
def handler(author: str, text: str, mode: str, **kwargs):
    # Strip formatting.
    author = api.utils.strip(author)
    text = api.utils.strip(text)

    # Get case by nick.
    case = api.cases.get(nick=author, cmdr=author)
    if case:
        author += f'{COLOR.INFO}#{case.num}{COLOR.DEFAULT}'
    else:
        # Get case by number or from command.
        matches = quote_matcher.search(text) or command_matcher.match(text)
        if matches:
            case = api.cases.get(
                cmdr=matches.groupdict()['query'],
                num=matches.groupdict()['query'],
                nick=matches.groupdict()['query'],
            )
    if not case:
        # Try reverse match by nick.
        cases = api.cases.get_all()
        try:
            case = next((
                c for c in cases if (c.nick or c.cmdr) in text
            ))
        except StopIteration:
            pass

    # If case found - replace all case num mentions with the case info.
    if case:
        text = text.replace(f'#{case.num}', str(case))

    # Highlight whatever we can find.
    for highlighter, color in highlighters.items():
        text = highlighter.sub(
            f'{color}\\1{COLOR.DEFAULT}',
            text,
        )

    # Emit resulting message as an output print.
    api.utils.emit_print(
        f'{COLOR.WHITE}{text}',
        event=api.const.EVENT.YOUR_MESSAGE,
        prefix=f'{COLOR.RAT if mode else COLOR.CLIENT}'
               f'{author}'
               f'{COLOR.DEFAULT}',
        mode=mode,
    )

    # Emit resulting message into the respective context if available.
    if all((
        case,
        'paperwork' not in text.lower(),
        'successfully closed case' not in text.lower(),
        'to the trash' not in text.lower(),
    )):
        api.utils.emit_print(
            f'{COLOR.WHITE}{text}',
            event=api.const.EVENT.YOUR_MESSAGE,
            prefix=f'{COLOR.RAT if mode else COLOR.CLIENT}'
                   f'{author}'
                   f'{COLOR.DEFAULT}',
            mode=mode,
            context=f'#{case.num}',
        )

    return api.const.EAT.ALL
