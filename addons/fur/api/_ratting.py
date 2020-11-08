# __module_name__ = "Ratting Assist"
# __module_version__ = "1.0"
# __module_description__ = "Is supposed to help out with ratting."
#
# import functools
# import typing
#
# import winsound
#
# import hexchat
#
#
# # HOOKS
# def hook_print(event_name: str):
#     def decorator(func: typing.Any):
#         @functools.wraps(func)
#         def wrapper(*args):
#             return func(
#                 context=hexchat.get_context(),
#                 author=args[0][0],
#                 message=args[0][1],
#             )
#
#         hexchat.hook_print(name=event_name, callback=wrapper)
#         return wrapper
#
#     return decorator
#
#
# def hook_command(name: str, description: str):
#     def decorator(func: typing.Any):
#         @functools.wraps(func)
#         def wrapper(*args):
#             return func(
#                 context=hexchat.get_context(),
#                 word=args[0] or [],
#                 word_eol=args[1] or [],
#                 userdata=args[2],
#             )
#
#         hexchat.hook_command(name=name, callback=wrapper, help=description)
#
#     return decorator
#
#
# # UTILS
# def highlight(text: str):
#     hexchat.prnt(f'\002\00304 {text}')
#
#
# def beep():
#     winsound.MessageBeep()
#
#
# def set_active_case_id(case_id: typing.Optional[str] = None):
#     global _active_case_id
#     _active_case_id = case_id or ''
#     highlight(f'Active case set to #{get_active_case_id() or "None"}')
#
#
# def get_active_case_id() -> str:
#     global _active_case_id
#     return _active_case_id
#
#
# def send_message(context: 'hexchat.Context', message: str):
#     context.command(
#         f'MSG {context.get_info("channel")} #{get_active_case_id()}
#         {message}'
#     )
#
#
# # STATE
# _active_case_id = ''
#
#
# # INIT
# # noinspection PyUnusedLocal
# @hook_command(name='c', description='/c <message_id>')
# def case_message_cmd(
#         context: 'hexchat.Context', word_eol: typing.List[str], **kwargs,
# ):
#     try:
#         args = word_eol[1]
#         try:
#             int(args)
#             set_active_case_id(word_eol[1])
#         except ValueError:
#             if get_active_case_id():
#                 send_message(context, word_eol[1])
#     except IndexError:
#         set_active_case_id()
#     return hexchat.EAT_ALL
#
#
# # noinspection PyUnusedLocal
# @hook_print(event_name='Channel Message')
# def process_messages(author, message, **kwargs):
#     active_case_id = get_active_case_id()
#
#     if active_case_id:
#         if '!close' in message and active_case_id in message:
#             set_active_case_id()
#
#         if f'#{active_case_id}' in message:
#             hexchat.prnt(f'\002\00304 {author}: {message}')
#             beep()
#             return hexchat.EAT_ALL
