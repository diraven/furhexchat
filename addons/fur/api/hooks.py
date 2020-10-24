import typing as t

import hexchat
from . import const, utils


# noinspection PyShadowingBuiltins
def print(
    *,
    match_author: t.Optional[t.Union[str, t.Pattern]] = None,
    match_text: t.Optional[t.Union[str, t.Pattern]] = None,
    match_events: t.Iterable[str] = const.COMMAND_EVENTS,
    priority=const.PRIORITY.NORM,
):
    def factory(func: t.Callable):
        # noinspection PyUnusedLocal
        def wrapper(word: t.List[str], word_eol: t.List[str], userdata: t.Any):
            # Make sure text data is provided.
            if not word:
                return

            if match_author and word:
                if isinstance(match_author, str):
                    if not utils.nicks_match(word[0], match_author):
                        return
                else:
                    if not match_author.match(word[0]):
                        return

            # Match text.
            matches = None
            if match_text and len(word) > 1:
                if isinstance(match_text, str):
                    if not word[1].startswith(match_text):
                        return
                else:
                    matches = match_text.match(word[1])
                    if not matches:
                        return
                    matches = matches.groupdict()

            # Run the handler itself.
            text = word[1].strip() if len(word) > 1 else ''
            if text:
                return func(
                    author=word[0],
                    text=text,
                    mode=word[2] if len(word) > 2 else '',
                    matches=matches,
                    data=userdata,
                )

        # Register hooks with hexchat.
        for event in match_events:
            hexchat.hook_print(event, wrapper, priority=priority)
        return wrapper

    return factory


def command(
    *,
    names: t.Iterable[str],
    description: t.Optional[str] = None,
    userdata: t.Optional[t.Any] = None,
):
    def factory(func: t.Callable):
        # noinspection PyUnusedLocal
        def wrapper(word, word_eol, provided_userdata):
            return func(args=word[1:], data=provided_userdata)

        for name in names:
            hexchat.hook_command(
                name=name,
                callback=wrapper,
                userdata=userdata,
                help=description,
            )

    return factory
