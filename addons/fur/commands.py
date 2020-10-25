import typing as t

from . import api


# noinspection PyUnusedLocal
@api.hooks.command(names=('c', 'case'))
def handler(args: t.List[str], **kwargs) -> t.Optional[int]:
    if len(args) != 2:
        api.print_error('Usage: /c case_num nick')
    api.cases.put(*args)
    return api.const.EAT.ALL


# noinspection PyUnusedLocal
@api.hooks.command(names=('cd', 'casedelete'))
def handler(args: t.List[str], **kwargs) -> t.Optional[int]:
    if len(args) != 1:
        api.print_error('Usage: /c case_num')
    api.cases.delete(*args)
    return api.const.EAT.ALL
