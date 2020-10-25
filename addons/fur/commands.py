import typing as t

from . import api


# noinspection PyUnusedLocal
@api.hooks.command(names=('c', 'case'))
def handler(args: t.List[str], **kwargs) -> t.Optional[int]:
    api.cases.put(*args)
    api.print(f'case #{args[0]} was associated with nick {args[1]}')
    return api.const.EAT.ALL


# noinspection PyUnusedLocal
@api.hooks.command(names=('cd', 'casedelete'))
def handler(args: t.List[str], **kwargs) -> t.Optional[int]:
    if api.cases.delete(*args):
        api.print(f'case #{args[0]} nick association was removed')
    return api.const.EAT.ALL


# noinspection PyUnusedLocal
@api.hooks.command(names=('cc', 'cases'))
def handler(args: t.List[str], **kwargs) -> t.Optional[int]:
    for case in api.cases.get_all():
        api.print(str(case))
    return api.const.EAT.ALL
