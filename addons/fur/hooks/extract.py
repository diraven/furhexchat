import re
import typing as t

from .. import api
from ..api.const import COLOR

quote_matcher = re.compile(r'((?:#|case ?)(?P<query>\d+))', re.IGNORECASE)
command_matcher = re.compile(r'(![\w-]+\s+(?P<query>[\w_-]+))', re.IGNORECASE)

extractors: t.Dict[t.Pattern, str] = {
    re.compile(
        r'((?:#|case ?)\d+)(?:[^\w]|$)',
        re.IGNORECASE): COLOR.INFO,
    re.compile(r'(\w+\+)(?:[^\w]|$)', re.IGNORECASE): COLOR.SUCCESS,
    re.compile(r'(\w+-)(?:[^\w]|$)', re.IGNORECASE): COLOR.DANGER,
    re.compile(r'(\w+conf)(?:[^\w]|$)', re.IGNORECASE): COLOR.SUCCESS,
    re.compile(r'(\d+\s?k?ls)(?:[^\w]|$)', re.IGNORECASE): COLOR.WARNING,
    re.compile(
        r'(\d+\s*j(?:umps?)?)(?:[^\w]|$)', re.IGNORECASE): COLOR.WARNING,
    re.compile(
        r'(\s(?:open|pg|mm|ez))(?:[^\w]|$)', re.IGNORECASE): COLOR.WARNING,
    re.compile(r'(stdn)(?:[^\w]|$)', re.IGNORECASE): COLOR.DANGER,
}


# noinspection PyUnusedLocal
@api.hooks.print()
def handler(author: str, text: str, mode: str, **kwargs):
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

    # Extract whatever we can find.
    bits = []
    for extractor, color in extractors.items():
        matches = extractor.findall(text)
        for match in matches:
            bits.append(f'{color}{match}{COLOR.DEFAULT}')

    api.utils.print(" ".join(bits), case if case else '')

    # Print resulting message into the respective context if available.
    if all((
        case,
        'paperwork' not in text.lower(),
        'successfully closed case' not in text.lower(),
        'to the trash' not in text.lower(),
    )):
        api.utils.print(
            " ".join(bits),
            case if case else '',
            context=f'#{case.num}',
        )
        api.utils.print(text, author, context=f'#{case.num}')
