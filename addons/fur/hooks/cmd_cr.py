import re
import typing as t

from .. import api


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!cr (?P<query>[^\s]+)'),
)
def handler(matches: t.Dict[str, str], **kwargs):
    query = matches.get('query')
    case = api.state.find_case(query)
    if not case:
        api.print(f'Case not found: {query}')
        return
    api.state.put_case(num=case.num, is_cr=not case.is_cr)
