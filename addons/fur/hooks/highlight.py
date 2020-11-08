import re
import typing as t

from .. import api
from ..api.const import Color, Priority

quote_matcher = re.compile(r'((?:#|case ?)(?P<query>\d+))', re.IGNORECASE)
command_matcher = re.compile(r'(![\w-]+\s+(?P<query>[\w_-]+))', re.IGNORECASE)
boundary = r'(?:[^\w]|$|^)'

raw_highlighters: t.Dict[str, Color] = {
    r'(?:#|case ?)\d+': Color.info,
    r'\w+\+': Color.success,
    r'\w+-': Color.danger,
    r'\w+conf': Color.success,
    r'\d+\s?k?ls': Color.warning,
    r'\d+\s*j(?:umps?)?': Color.warning,
    r'(?:open|pg|mm|ez|solo)': Color.warning,
    r'stdn': Color.danger,
    r'(?:RATSIGNAL|Incoming Client)': Color.royal_blue,
}

highlighters = {
    re.compile(
        r'(' + boundary + k + boundary + r')',
        re.IGNORECASE,
    ): v.value for k, v in raw_highlighters.items()
}


# noinspection PyUnusedLocal
@api.hooks.print(priority=Priority.lowest)
def handler(author: str, text: str, mode: str, **kwargs):
    original_text = text

    # Try to figure out case the line is relevant to.
    case = api.cases.get(nick=author, cmdr=author)
    if not case:
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
                c for c in cases if
                (c.nick or c.cmdr) in " ".join((author, text))))
        except StopIteration:
            pass

    # # Print resulting message as is into the respective context.
    # if all((
    #     case,
    #     'paperwork' not in text.lower(),
    #     'successfully closed case' not in text.lower(),
    #     'to the trash' not in text.lower(),
    # )):
    #     api.utils.emit_print(text, prefix=author, context=f'#{case.num}')

    # Set color for author.
    if mode:
        author = f'{Color.tailed}{author}{Color.default}'
    else:
        author = f'{Color.untailed}{author}{Color.default}'

    # Replace case and author references.
    if case:
        text = re.sub(f'(?:{case.nick}|#{case.num})', str(case), text)
        if api.utils.strip(author) == case.name:
            author = str(case)

    # Highlight whatever we can find.
    bits = []
    for highlighter, color in highlighters.items():
        text = highlighter.sub(f'{color}\\1{Color.default}', text)

    # Output processed text.
    api.utils.print(text, prefix=author)

    # Output original text.
    api.utils.emit_print(
        original_text, prefix=author, context=api.const.RAW_CONTEXT_NAME,
    )

    return api.const.Eat.all
