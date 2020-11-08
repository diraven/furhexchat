import re
import typing as t

from .. import api

quote_matcher = re.compile(r'((?:#|case ?)(?P<query>\d+))', re.IGNORECASE)
command_matcher = re.compile(r'(![\w-]+\s+(?P<query>[\w_-]+))', re.IGNORECASE)
boundary = r'(?:[^\w]|$|^)'

raw_highlighters: t.Dict[str, api.Color] = {
    r'(?:#|case ?)\d+': api.Color.info,
    r'\w+\+': api.Color.success,
    r'\w+-': api.Color.danger,
    r'\w+conf': api.Color.success,
    r'\d+\s?k?ls': api.Color.warning,
    r'\d+\s*j(?:umps?)?': api.Color.warning,
    r'(?:open|pg|mm|ez|solo)': api.Color.warning,
    r'stdn': api.Color.danger,
    r'(?:RATSIGNAL|Incoming Client)': api.Color.royal_blue,
}

highlighters = {
    re.compile(
        r'(' + boundary + k + boundary + r')',
        re.IGNORECASE,
    ): v.value for k, v in raw_highlighters.items()
}


# noinspection PyUnusedLocal
@api.hook_print(priority=api.Priority.lowest)
def handler(
    author: str, text: str, mode: str, event: api.Event, **kwargs,
):
    original_text = text
    original_author = author

    # Try to figure out case the line is relevant to.
    case = api.get_case(nick=author, cmdr=author)
    if not case:
        # Get case by number or from command.
        matches = quote_matcher.search(text) or command_matcher.match(text)
        if matches:
            case = api.get_case(
                cmdr=matches.groupdict()['query'],
                num=matches.groupdict()['query'],
                nick=matches.groupdict()['query'],
            )
    if not case:
        # Try reverse match by nick.
        cases = api.get_all_cases()
        try:
            case = next((
                c for c in cases if
                (c.nick or c.cmdr) in " ".join((author, text))))
        except StopIteration:
            pass

    # Set color for author.
    if mode:
        author = f'{api.Color.tailed}{author}{api.Color.default}'
    else:
        author = f'{api.Color.untailed}{author}{api.Color.default}'

    # Replace case and author references.
    if case:
        text = re.sub(f'(?:{case.nick}|#{case.num})', str(case), text)
        if api.strip(author) == case.name:
            author = str(case)

    # Highlight whatever we can find.
    bits = []
    for highlighter, color in highlighters.items():
        text = highlighter.sub(f'{color}\\1{api.Color.default}', text)

    # Output processed text.
    api.print(text, prefix=author)

    # Output original text.
    api.log(original_text, prefix=original_author, event=event)

    return api.Eat.all
