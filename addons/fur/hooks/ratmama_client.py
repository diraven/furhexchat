import re
import typing as t

from .. import api


@api.hook_print(
    match_message=re.compile(
        r'Incoming Client: (?P<cmdr>.+) - '
        r'System: (?P<system>.+) - '
        r'Platform: ''(?P<platform>.+) - '
        'O2: (' r'?P<o2>.+) - '
        r'Language: (?P<language>.+) \((?P<language_code>.*)\)',
        flags=re.IGNORECASE,
    ),
    events=api.types.COMMAND_EVENTS,
)
def handler(
    matches: t.Dict[str, str],
    **kwargs,
):
    api.state.put_case(
        cmdr=matches.get('cmdr'),
        system=matches.get('system'),
        platform=matches.get('platform'),
        is_cr=matches.get('o2') != 'OK',
        language=matches.get('language')
    )
