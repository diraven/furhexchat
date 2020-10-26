import re
import typing as t

from .. import api
from ..api.const import COLOR

quote_matcher = re.compile(
    r'((?:#|case ?|go |assign |unassign |nick )(?P<case_num>\d+))',
    re.IGNORECASE,
)
highlighters: t.Dict[t.Pattern, str] = {
    re.compile(
        r'((?:#|case ?)(?P<case_num>\d+)(?:[^\d]|$))', re.IGNORECASE): COLOR.INFO,
    re.compile(r'(\w+\+(?:[^\d]|$))', re.IGNORECASE): COLOR.SUCCESS,
    re.compile(r'(\w+-(?:[^\d]|$))', re.IGNORECASE): COLOR.DANGER,
    re.compile(r'(\w+conf(?:[^\d]|$))', re.IGNORECASE): COLOR.SUCCESS,
    re.compile(r'(\d+\s?k?ls(?:[^\d]|$))', re.IGNORECASE): COLOR.WARNING,
    re.compile(
        r'(\d+\s*j(?:umps?)?(?:[^\d]|$))', re.IGNORECASE): COLOR.WARNING,
    re.compile(
        r'(\s(?:open|pg|mm|ez)(?:[^\d]|$))', re.IGNORECASE): COLOR.WARNING,
    re.compile(r'(stdn(?:[^\d]|$))', re.IGNORECASE): COLOR.DANGER,
}


# noinspection PyUnusedLocal
@api.hooks.print(match_events=[
    api.const.EVENT.CHANNEL_MESSAGE,
    api.const.EVENT.CHANNEL_MSG_HILIGHT,
    api.const.EVENT.PRIVATE_MESSAGE_TO_DIALOG,
    api.const.EVENT.PRIVATE_MESSAGE,
])
def handler(author: str, text: str, mode: str, **kwargs):
    # Strip formatting.
    author = api.utils.strip(author)
    text = api.utils.strip(text)

    # Get case by nick.
    case = api.cases.get(nick=author, cmdr=author)
    if case:
        author += f'{COLOR.INFO}#{case.num}{COLOR.DEFAULT}'
    else:
        # Get case by number.
        matches = quote_matcher.search(text)
        if matches:
            case = api.cases.get(num=matches.groupdict()['case_num'])

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
            f'{COLOR.DEFAULT} {text}',
            event=api.const.EVENT.YOUR_MESSAGE,
            prefix=f'{COLOR.RAT if mode else COLOR.CLIENT}'
                   f'{author}'
                   f'{COLOR.DEFAULT}',
            mode=mode,
            context=f'#{case.num}',
        )

    return api.const.EAT.ALL
