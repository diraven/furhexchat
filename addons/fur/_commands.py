import typing as t

from ._api import API


def init(api: API):
    # noinspection PyUnusedLocal
    @api.hook_command(names=('c', 'case'))
    def case(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
        api.put_case(num=args[0], nick=args[1], cmdr=args[1])
        api.print_info(f'case #{args[0]} was associated with nick {args[1]}')
        return api.Eat.all

    # noinspection PyUnusedLocal
    @api.hook_command(names=('cd', 'casedelete'))
    def delete_case(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
        query = args[0]
        case = api.get_case(cmdr=query, num=query, nick=query)
        if not case:
            api.print_error(f'case "{query}" was not found')
        if api.delete_case(num=case.num):
            api.print_info(f'case {query} was removed')
        return api.Eat.all

    # noinspection PyUnusedLocal
    @api.hook_command(names=('cc', 'cases'))
    def cases(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
        for case in api.get_all_cases():
            api.print_info(str(case))
        return api.Eat.all

    # noinspection PyUnusedLocal
    @api.hook_command(names=('cs', 'casesync'))
    def sync_cases(args: t.List[str], **kwargs) -> t.Optional[api.Eat]:
        api.send_command('MSG MechaSqueak[BOT] !list')
        return api.Eat.all
