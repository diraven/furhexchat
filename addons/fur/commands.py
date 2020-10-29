import typing as t

from . import api


# noinspection PyUnusedLocal
@api.hooks.command(names=('c', 'case'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.const.Eat]:
    api.cases.put(num=args[0], nick=args[1], cmdr=args[1])
    api.print(f'case #{args[0]} was associated with nick {args[1]}')
    return api.const.Eat.all


# noinspection PyUnusedLocal
@api.hooks.command(names=('cd', 'casedelete'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.const.Eat]:
    query = args[0]
    case = api.cases.get(cmdr=query, num=query, nick=query)
    if not case:
        api.print_error(f'case "{query}" was not found')
    api.close_context(f'#{case.num}')
    if api.cases.delete(num=case.num):
        api.print(f'case {query} was removed')
    return api.const.Eat.all


# noinspection PyUnusedLocal
@api.hooks.command(names=('cc', 'cases'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.const.Eat]:
    for case in api.cases.get_all():
        api.print(str(case))
    return api.const.Eat.all


# noinspection PyUnusedLocal
@api.hooks.command(names=('cs', 'casesync'))
def handler(args: t.List[str], **kwargs) -> t.Optional[api.const.Eat]:
    api.message('MechaSqueak[BOT]', '!list')
    return api.const.Eat.all
