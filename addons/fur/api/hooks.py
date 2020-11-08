import typing as t

import hexchat
from . import const, utils


# noinspection PyShadowingBuiltins
def print(
    *,
    match_author: t.Optional[t.Union[str, t.Pattern]] = None,
    match_text: t.Optional[t.Union[str, t.Pattern]] = None,
    match_events: t.Iterable[const.Event] = const.DEFAULT_EVENTS,
    priority=const.Priority.normal,
):
    def factory(func: t.Callable):
        # noinspection PyUnusedLocal
        def wrapper(word: t.List[str], word_eol: t.List[str], userdata: t.Any):
            # Make srue we are not processing log.

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
            text = utils.strip(word[1]) if len(word) > 1 else ''
            author = utils.strip(word[0]) if word[0] else ''
            if text and not text.endswith(utils.strip(const.TERMINATOR)):
                result = func(
                    author=author,
                    text=text,
                    mode=word[2] if len(word) > 2 else '',
                    matches=matches,
                    event=const.Event(userdata['event']),
                    channel=hexchat.get_info(const.Info.channel.value),
                    server=hexchat.get_info(const.Info.server.value),
                    data=userdata,
                )
                if result:
                    return result.value

        # Register hooks with hexchat.
        for event in match_events:
            hexchat.hook_print(
                event.value,
                wrapper,
                userdata={'event': event},
                priority=priority.value,
            )
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
            eat = func(args=word[1:], data=provided_userdata)
            if eat:
                return eat.value

        for name in names:
            hexchat.hook_command(
                name=name,
                callback=wrapper,
                userdata=userdata,
                help=description,
            )

    return factory
