import re
import typing as t

from ._api import API


def init(api: API):
    quote_matcher = re.compile(r'((?:#|case ?)(?P<query>\d+))', re.IGNORECASE)
    command_matcher = re.compile(
        r'(![\w-]+\s+(?P<query>[\w_-]+))', re.IGNORECASE,
    )
    boundary = r'([^\w]|$|^)'

    raw_highlighters: t.Dict[str, api.Color] = {
        r'(?:#|case ?)\d+': api.Color.case,
        r'\w+\+': api.Color.success,
        r'\w+-': api.Color.danger,
        r'O2: NOT OK': api.Color.danger,
        r'\(not in galaxy database\)': api.Color.warning,
        r'\w+conf': api.Color.success,
        r'\d+\s?k?ls': api.Color.warning,
        r'\d+\s*j(?:umps?)?': api.Color.warning,
        r'(?:open|pg|mm|ez|solo)': api.Color.warning,
        r'stdn': api.Color.danger,
        r'(?:RATSIGNAL|Incoming Client)': api.Color.case,
        r'(?:Language: [^\s]+)': api.Color.info,
    }

    highlighters = {
        re.compile(
            boundary + r'(' + k + r')' + boundary,
            re.IGNORECASE,
        ): v.value for k, v in raw_highlighters.items()
    }

    # noinspection PyUnusedLocal
    @api.hook_print(priority=api.Priority.lowest)
    def process_case(
        author: str, text: str, mode: str, event: api.Event, **kwargs,
    ):
        # For original message. Otherwise context gets switched.
        original_text = text
        original_author = author

        # Try to figure out case the line is relevant to.
        case = api.get_case(nick=author, cmdr=author)
        if not case:
            # Get case by number or from command.
            matches = quote_matcher.search(text) or command_matcher.match(text)
            if matches:
                case = api.get_case(
                    cmdr=matches.groupdict()['query'],
                    num=matches.groupdict()['query'],
                    nick=matches.groupdict()['query'],
                )
        if not case:
            # Try reverse match by nick.
            cases = api.get_all_cases()
            try:
                case = next((
                    c for c in cases if
                    (c.nick or c.cmdr) in " ".join((author, text))))
            except StopIteration:
                pass

        # Set color for author.
        if mode:
            author = f'{api.Color.tailed}{author}{api.Color.default}'
        else:
            author = f'{api.Color.untailed}{author}{api.Color.default}'

        if case:
            # Provide case info.
            text = f'{str(case)}> {text}'
            # Also in author if they are the author.
            author = author.replace(
                case.nick,
                f'{api.Color.client}{case.nick}{api.Color.default}',
            )
        else:
            text = f'{text}'

        # Highlight whatever we can find.
        bits = []
        for highlighter, color in highlighters.items():
            text = highlighter.sub(
                f'\\1{color}\\2{api.Color.default}\\3',
                text,
            )

        # Output processed text.
        api.print_info(text, prefix=author)

        api.log(original_text, prefix=original_author, event=event)
        return api.Eat.all

    # noinspection PyUnusedLocal
    @api.hook_print(
        match_text=re.compile(r'Incoming Client: (?P<cmdr>[^-]+) - System:'),
    )
    def incoming_client(text: str, matches: t.Dict, **kwargs):
        cmdr = matches['cmdr']
        nick = None
        if 'IRC Nickname' in text:
            nick = text.split()[-1]
        api.print_info(
            f'Case update: {str(api.put_case(cmdr=cmdr, nick=nick))}',
        )

    ratsignal_casenum_matcher = re.compile(r'Case #(?P<num>\d+)')
    ratsignal_cmdr_matcher = re.compile(
        r'CMDR (?P<cmdr>.*) - Reported System:')

    # noinspection PyUnusedLocal
    @api.hook_print(match_text='RATSIGNAL')
    def ratsignal(text: str, mode: str, **kwargs):
        num = ratsignal_casenum_matcher.search(
            text,
        ).groupdict()['num']
        cmdr = ratsignal_cmdr_matcher.search(text).groupdict()['cmdr']
        api.print_info(f'Case update: {str(api.put_case(cmdr=cmdr, num=num))}')

    # noinspection PyUnusedLocal
    @api.hook_print(
        match_text=re.compile(
            r'!(?:close|clear|md|trash)\s+#?(?P<query>[^\s]+)'),
    )
    def delete_case(matches: t.Match, **kwargs):
        query = matches['query']
        case = api.get_case(num=query, nick=query, cmdr=query)
        if case and api.delete_case(num=case.num):
            api.print_info(f'case #{case.num} was closed')

    # noinspection PyUnusedLocal
    @api.hook_print(
        match_text=re.compile(
            r'!nick\s+#?(?P<query>[^\s]+)\s+(?P<nick>[^\s]+)',
        ),
    )
    def change_nick(matches: t.Match, **kwargs):
        query = matches['query']
        nick = matches['nick']
        case = api.get_case(num=query, nick=query, cmdr=query)
        if case:
            case.nick = nick
            api.print_info(
                f'case #{case.num} nick association was updated: {nick}',
            )
        return

    _list_item_rexp = re.compile(
        r'(\[(?P<num>\d+)] '
        r'\(?(?P<cmdr>[^()]+)\)? '
        r'\((?P<platform>[^()]+)\)) ?',
        flags=re.IGNORECASE,
    )

    # noinspection PyUnusedLocal
    @api.hook_print(
        match_text=re.compile(r'\d+ cases found'),
    )
    def mecha_list_cases(text: str, **kwargs):
        items = text.split(', ')
        if len(items) < 2:
            return

        items = items[1:]
        nums = []
        for item in items:
            try:
                matches: t.Dict = _list_item_rexp.match(item).groupdict()
            except AttributeError:
                continue
            nums.append(matches.get('num'))
            api.put_case(
                cmdr=matches.get('cmdr'),
                num=matches.get('num'),
            )
        for case in api.get_all_cases():
            if case.num not in nums:
                api.delete_case(num=case.num)

    # noinspection PyUnusedLocal
    @api.hook_print(match_events=[api.Event.change_nick])
    def on_nick_changed(text: str, author: str, **kwargs):
        old_nick = author
        new_nick = text
        case = api.get_case(nick=old_nick)
        if case:
            case.nick = new_nick
            api.print_info(
                f'case #{case.num} nick association was updated: '
                f'{old_nick} -> {new_nick}',
            )
