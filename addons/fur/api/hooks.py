import typing as t

import hexchat
from . import types, utils


def hook_print(
    *,
    match_author: t.Optional[t.Union[str, t.Pattern]] = None,
    match_message: t.Optional[t.Union[str, t.Pattern]] = None,
    events: t.Iterable[types.Event] = (
        types.Event.CHANNEL_MESSAGE,
        types.Event.CHANNEL_MSG_HILIGHT,
        types.Event.NOTICE,
        types.Event.PRIVATE_MESSAGE_TO_DIALOG,
    ),
):
    def factory(func: t.Callable):
        # noinspection PyUnusedLocal
        def wrapper(word: t.List[str], word_eol, userdata: t.Any):
            # Make sure message data is provided.
            if not word:
                return

            if match_author and word:
                if isinstance(match_author, str):
                    if not utils.nicks_match(word[0], match_author):
                        return
                else:
                    if not match_author.match(word[0]):
                        return

            # Match message.
            matches = None
            if match_message and len(word) > 1:
                if isinstance(match_message, str):
                    if not word[1].startswith(match_message):
                        return
                else:
                    matches = match_message.match(word[1])
                    if not matches:
                        return
                    matches = matches.groupdict()

            # Run the handler itself.
            return func(
                author=word[0],
                message=hexchat.strip(
                    word[1].strip(),
                ) if len(word) > 1 else None,
                mode=word[2] if len(word) > 2 else None,
                matches=matches,
                data=userdata,
            )

        # Register hooks with hexchat.
        for event in events:
            hexchat.hook_print(event.value, wrapper)
        return wrapper

    return factory


def hook_command(
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
        return wrapper

    return factory


def clean(text: str) -> str:
    return hexchat.strip(text.strip())
