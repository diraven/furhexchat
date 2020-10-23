import re
import typing as t

from .. import api


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!cr (?P<query>[^\s]+)')
)
def cr_case(matches: t.Dict[str, str], **kwargs):
    query = matches.get('query')
    case = api.find_case(query)
    if not case:
        api.print(f'Case not found: {query}')
        return
    api.put_case(num=case['num'], is_cr=not case['is_cr'])
