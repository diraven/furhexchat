import re
import typing as t

from .. import api


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(
        r'RATSIGNAL - '
        r'CMDR (?P<cmdr>.+) - '
        r'Reported System: (?P<system>.+) \((?P<landmark>.+)\) - '
        r'Platform: (?P<platform>.+) - '
        r'O2: (?P<o2>.+) '
        r'Language: (?P<language>.+) \((?P<language_code>.+)\) '
        r'\(Case #(?P<num>\d+)\) '
        r'\((?P<platform_signal>.+)\)',
        flags=re.IGNORECASE,
    ),
)
def mecha_announcement(
    matches: t.Dict[str, str],
    **kwargs,
):
    api.put_case(
        cmdr=matches.get('cmdr'),
        system=matches.get('system'),
        landmark=matches.get('landmark'),
        platform=matches.get('platform'),
        is_cr=matches.get('o2') != 'OK',
        language=matches.get('language_code'),
        num=int(matches.get('num')),
    )
