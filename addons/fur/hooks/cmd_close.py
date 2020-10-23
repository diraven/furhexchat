import re
import typing as t

from .. import api


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'^!(?:close|clear|md|trash) (?P<query>[^\s]+)')
)
def delete_case(matches: t.Dict[str, str], **kwargs):
    query = matches.get('query')
    case = api.find_case(query)
    if not case:
        api.print(f'Case not found: {query}')
        return
    api.delete_case(num=int(case['num']))
