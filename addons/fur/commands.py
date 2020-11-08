import typing as t

from . import api


# noinspection PyUnusedLocal
@api.hook_command(names=('c', 'case'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
    api.put_case(num=args[0], nick=args[1], cmdr=args[1])
    api.print(f'case #{args[0]} was associated with nick {args[1]}')
    return api.Eat.all


# noinspection PyUnusedLocal
@api.hook_command(names=('cd', 'casedelete'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
    query = args[0]
    case = api.get_case(cmdr=query, num=query, nick=query)
    if not case:
        api.print_error(f'case "{query}" was not found')
    if api.delete_case(num=case.num):
        api.print(f'case {query} was removed')
    return api.Eat.all


# noinspection PyUnusedLocal
@api.hook_command(names=('cc', 'cases'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
    for case in api.get_all_cases():
        api.print(str(case))
    return api.Eat.all


# noinspection PyUnusedLocal
@api.hook_command(names=('cs', 'casesync'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
    api.message('MechaSqueak[BOT]', '!list')
    return api.Eat.all
