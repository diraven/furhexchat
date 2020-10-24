import re
import typing as t

from . import api

COLOR_SUCCESS = api.const.COLOR.GREEN
COLOR_WARNING = api.const.COLOR.YELLOW
COLOR_DANGER = api.const.COLOR.RED
COLOR_INFO = api.const.COLOR.ROYAL_BLUE

COLOR_RAT = api.const.COLOR.ORANGE
COLOR_CLIENT = api.const.COLOR.TEAL

quote_matcher = re.compile(r'((?:#|case ?)(?P<case_id>\d+))', re.IGNORECASE)
highlighters: t.Dict[t.Pattern, str] = {
    quote_matcher: COLOR_INFO,
    re.compile(r'(\w+\+)', re.IGNORECASE): COLOR_SUCCESS,
    re.compile(r'(\w+conf)', re.IGNORECASE): COLOR_SUCCESS,
    re.compile(r'(\d+\s?k?ls)', re.IGNORECASE): COLOR_WARNING,
    re.compile(r'(\d+\s*j(?:umps?)?|$)', re.IGNORECASE): COLOR_WARNING,
    re.compile(r'(\sopen|pg|mm|ez(?:[^\w]|$))]', re.IGNORECASE): COLOR_WARNING,
    re.compile(r'(ratsignal|incoming client)', re.IGNORECASE): COLOR_WARNING,
    re.compile(r'(\w+-(?:[^\w]|$))', re.IGNORECASE): COLOR_DANGER,
}
close_matcher = re.compile(
    r'!(?:close|md|clear|trash) #?(?P<case_id>\d+)', re.IGNORECASE,
)

# DEBUG
# INBOUND_EVENT = api.const.EVENT.YOUR_MESSAGE
# OUTBOUND_EVENT = api.const.EVENT.CHANNEL_MESSAGE

# PROD
INBOUND_EVENT = api.const.EVENT.CHANNEL_MESSAGE
OUTBOUND_EVENT = api.const.EVENT.YOUR_MESSAGE

HIGHLIGHTED_EVENT = api.const.EVENT.CHANNEL_MSG_HILIGHT


# noinspection PyUnusedLocal
@api.hooks.print(
    match_events=[INBOUND_EVENT],
    priority=api.const.PRIORITY.LOWEST,
)
def handler(author: str, text: str, mode: str, **kwargs):
    outbound_event = OUTBOUND_EVENT
    if any((
        'ratsignal' in text.lower(),
        text.lower().startswith('incoming client:'),
    )):
        outbound_event = HIGHLIGHTED_EVENT

    for highlighter, color in highlighters.items():
        text = highlighter.sub(
            f'{color}\\1{api.const.COLOR.DEFAULT}',
            text,
        )

    api.utils.emit_print(
        f'{api.const.COLOR.DEFAULT}{text}',
        event=outbound_event,
        prefix=f'{COLOR_RAT if mode else COLOR_CLIENT}'
               f'{author}'
               f'{api.const.COLOR.DEFAULT}',
        mode=mode,
    )

    matches = quote_matcher.search(text)
    if matches:
        api.utils.emit_print(
            f'{api.const.COLOR.DEFAULT}{text}',
            event=OUTBOUND_EVENT,
            prefix=f'{COLOR_RAT if mode else COLOR_CLIENT}'
                   f'{author}'
                   f'{api.const.COLOR.DEFAULT}',
            mode=mode,
            context=f'#{matches["case_id"]}',
        )

    matches = close_matcher.match(text)
    if matches:
        api.close_context(f'#{matches["case_id"]}')

    return api.const.EAT.ALL
