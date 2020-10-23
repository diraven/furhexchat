import re
import typing as t

from .. import api

_list_item_rexp = re.compile(
    r'(\[(?P<num>\d+)] '
    r'(?P<cmdr>[^)]+) '
    r'\((?P<platform>[^)]+)\)) ?',
    flags=re.IGNORECASE,
)


# noinspection PyUnusedLocal
@api.hook_print(
    match_message=re.compile(r'\d+ cases found')
)
def mecha_list(message: str, **kwargs):
    items = message.split(', ')
    if len(items) < 2:
        return

    items = items[1:]
    nums = []
    for item in items:
        matches: t.Dict = _list_item_rexp.match(item).groupdict()
        nums.append(int(matches.get('num')))
        api.put_case(
            cmdr=matches.get('cmdr'),
            num=int(matches.get('num')),
            platform=matches.get('platform'),
            is_cr='(cr)' in item.lower(),
            is_active='(inactive)' not in item.lower(),
        )
    for case_num in map(lambda c: c['num'], api.get()['cases']):
        if case_num not in nums:
            api.delete_case(case_num)
