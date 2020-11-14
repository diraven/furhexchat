import enum
import typing as t

import winsound


class _StrEnum(enum.Enum):
    def __str__(self):
        return str(self.value)


class _Case:
    __slots__ = ['cmdr', 'num', '_nick', '_rats', '_calls']

    @enum.unique
    class CallType(_StrEnum):
        FR = 'fr'
        WR = 'wr'
        BC = 'bc'

    def __init__(
        self,
        api: 'API',
        cmdr: str,
        num: str = None,
        nick: str = None,
    ):
        self.cmdr = api.strip(cmdr) if cmdr else cmdr
        self.num = api.strip(num) if num else num
        self._nick = api.strip(nick) if nick else nick
        self._calls = {}
        self._rats = set()

        self.reset_calls()

    @property
    def nick(self):
        if self._nick:
            return self._nick
        else:
            nick = self.cmdr.replace(' ', '_').replace('.', '')
            return f'c_{nick}' if nick[0].isdigit() else nick

    @nick.setter
    def nick(self, v):
        self._nick = v

    def put_rat(self, nick):
        self._rats.add(nick)

    def get_rats(self):
        return self._rats

    def __str__(self):
        state = ''
        # for call_type in self.CallType:
        #     if self._calls[call_type]:
        #         state = f'|{call_type.value.upper()}' \
        #                 f'({len(self._calls[call_type])}/' \
        #                 f'{len(self._rats)})'

        return f'({self.nick} #{self.num}{state})'

    def called(self, *, caller: str, call_type: CallType, state: bool):
        if state:
            self._calls[call_type].add(caller)
        else:
            try:
                self._calls[call_type].remove(caller)
            except KeyError:
                pass

    def reset_calls(self):
        for call_type in self.CallType:
            self._calls[call_type] = set()


class API:
    @enum.unique
    class Eat(enum.Enum):
        none = 0
        hexchat = 1
        plugin = 2
        all = hexchat | plugin

    @enum.unique
    class Priority(enum.Enum):
        highest = 127
        high = 64
        normal = 0
        low = -64
        lowest = -128

    @enum.unique
    class Event(enum.Enum):
        add_notify = 'Add Notify'
        ban_list = 'Ban List'
        banned = 'Banned'
        beep = 'Beep'
        capability_acknowledgement = 'Capability Acknowledgement'
        capability_deleted = 'Capability Deleted'
        capability_list = 'Capability List'
        capability_request = 'Capability Request'
        change_nick = 'Change Nick'
        channel_action = 'Channel Action'
        channel_action_hilight = 'Channel Action Hilight'
        channel_ban = 'Channel Ban'
        channel_creation = 'Channel Creation'
        channel_dehalfop = 'Channel DeHalfOp'
        channel_deop = 'Channel DeOp'
        channel_devoice = 'Channel DeVoice'
        channel_exempt = 'Channel Exempt'
        channel_half_operator = 'Channel Half-Operator'
        channel_invite = 'Channel INVITE'
        channel_list = 'Channel List'
        channel_message = 'Channel Message'
        channel_mode_generic = 'Channel Mode Generic'
        channel_modes = 'Channel Modes'
        channel_msg_hilight = 'Channel Msg Hilight'
        channel_notice = 'Channel Notice'
        channel_operator = 'Channel Operator'
        channel_quiet = 'Channel Quiet'
        channel_remove_exempt = 'Channel Remove Exempt'
        channel_remove_invite = 'Channel Remove Invite'
        channel_remove_keyword = 'Channel Remove Keyword'
        channel_remove_limit = 'Channel Remove Limit'
        channel_set_key = 'Channel Set Key'
        channel_set_limit = 'Channel Set Limit'
        channel_unban = 'Channel UnBan'
        channel_unquiet = 'Channel UnQuiet'
        channel_url = 'Channel Url'
        channel_voice = 'Channel Voice'
        connected = 'Connected'
        connecting = 'Connecting'
        connection_failed = 'Connection Failed'
        ctcp_generic = 'CTCP Generic'
        ctcp_generic_to_channel = 'CTCP Generic to Channel'
        ctcp_send = 'CTCP Send'
        ctcp_sound = 'CTCP Sound'
        ctcp_sound_to_channel = 'CTCP Sound to Channel'
        dcc_chat_abort = 'DCC CHAT Abort'
        dcc_chat_connect = 'DCC CHAT Connect'
        dcc_chat_failed = 'DCC CHAT Failed'
        dcc_chat_offer = 'DCC CHAT Offer'
        dcc_chat_offering = 'DCC CHAT Offering'
        dcc_chat_reoffer = 'DCC CHAT Reoffer'
        dcc_conection_failed = 'DCC Conection Failed'
        dcc_generic_offer = 'DCC Generic Offer'
        dcc_header = 'DCC Header'
        dcc_malformed = 'DCC Malformed'
        dcc_offer = 'DCC Offer'
        dcc_offer_not_valid = 'DCC Offer Not Valid'
        dcc_recv_abort = 'DCC RECV Abort'
        dcc_recv_complete = 'DCC RECV Complete'
        dcc_recv_connect = 'DCC RECV Connect'
        dcc_recv_failed = 'DCC RECV Failed'
        dcc_recv_file_open_error = 'DCC RECV File Open Error'
        dcc_rename = 'DCC Rename'
        dcc_resume_request = 'DCC RESUME Request'
        dcc_send_abort = 'DCC SEND Abort'
        dcc_send_complete = 'DCC SEND Complete'
        dcc_send_connect = 'DCC SEND Connect'
        dcc_send_failed = 'DCC SEND Failed'
        dcc_send_offer = 'DCC SEND Offer'
        dcc_stall = 'DCC Stall'
        dcc_timeout = 'DCC Timeout'
        delete_notify = 'Delete Notify'
        disconnected = 'Disconnected'
        found_ip = 'Found IP'
        generic_message = 'Generic Message'
        ignore_add = 'Ignore Add'
        ignore_changed = 'Ignore Changed'
        ignore_footer = 'Ignore Footer'
        ignore_header = 'Ignore Header'
        ignore_remove = 'Ignore Remove'
        ignorelist_empty = 'Ignorelist Empty'
        invite = 'Invite'
        invited = 'Invited'
        join = 'Join'
        keyword = 'Keyword'
        kick = 'Kick'
        killed = 'Killed'
        message_send = 'Message Send'
        motd = 'Motd'
        motd_skipped = 'MOTD Skipped'
        nick_clash = 'Nick Clash'
        nick_erroneous = 'Nick Erroneous'
        nick_failed = 'Nick Failed'
        no_dcc = 'No DCC'
        no_running_process = 'No Running Process'
        notice = 'Notice'
        notice_send = 'Notice Send'
        notify_away = 'Notify Away'
        notify_back = 'Notify Back'
        notify_empty = 'Notify Empty'
        notify_header = 'Notify Header'
        notify_number = 'Notify Number'
        notify_offline = 'Notify Offline'
        notify_online = 'Notify Online'
        open_dialog = 'Open Dialog'
        part = 'Part'
        part_with_reason = 'Part with Reason'
        ping_reply = 'Ping Reply'
        ping_timeout = 'Ping Timeout'
        private_action = 'Private Action'
        private_action_to_dialog = 'Private Action to Dialog'
        private_message = 'Private Message'
        private_message_to_dialog = 'Private Message to Dialog'
        process_already_running = 'Process Already Running'
        quit = 'Quit'
        raw_modes = 'Raw Modes'
        receive_wallops = 'Receive Wallops'
        resolving_user = 'Resolving User'
        sasl_authenticating = 'SASL Authenticating'
        sasl_response = 'SASL Response'
        server_connected = 'Server Connected'
        server_error = 'Server Error'
        server_lookup = 'Server Lookup'
        server_notice = 'Server Notice'
        server_text = 'Server Text'
        ssl_message = 'SSL Message'
        stop_connection = 'Stop Connection'
        topic = 'Topic'
        topic_change = 'Topic Change'
        topic_creation = 'Topic Creation'
        unknown_host = 'Unknown Host'
        user_limit = 'User Limit'
        users_on_channel = 'Users On Channel'
        whois_authenticated = 'WhoIs Authenticated'
        whois_away_line = 'WhoIs Away Line'
        whois_channel_oper_line = 'WhoIs Channel/Oper Line'
        whois_end = 'WhoIs End'
        whois_identified = 'WhoIs Identified'
        whois_idle_line = 'WhoIs Idle Line'
        whois_idle_line_with_signon = 'WhoIs Idle Line with Signon'
        whois_name_line = 'WhoIs Name Line'
        whois_real_host = 'WhoIs Real Host'
        whois_server_line = 'WhoIs Server Line'
        whois_special = 'WhoIs Special'
        you_join = 'You Join'
        you_kicked = 'You Kicked'
        you_part = 'You Part'
        you_part_with_reason = 'You Part with Reason'
        your_action = 'Your Action'
        your_invitation = 'Your Invitation'
        your_message = 'Your Message'
        your_nick_changing = 'Your Nick Changing'

    @enum.unique
    class Info(_StrEnum):
        away = 'away'
        channel = 'channel'
        charset = 'charset'
        configdir = 'configdir'
        event_text = 'event_text'
        gtkwin_ptr = 'gtkwin_ptr'
        host = 'host'
        inputbox = 'inputbox'
        network = 'network'
        nick = 'nick'
        nickserv = 'nickserv'
        modes = 'modes'
        password = 'password'
        server = 'server'
        topic = 'topic'
        version = 'version'
        win_status = 'win_status'

    class Color(_StrEnum):
        default = '\017'

        white = '\00300'
        black = '\00301'
        navy = '\00302'
        green = '\00303'
        red = '\00304'
        maroon = '\00305'
        purple = '\00306'
        orange = '\00307'
        yellow = '\00308'
        light_green = '\00309'
        teal = '\00310'
        cyan = '\00311'
        royal_blue = '\00312'
        magenta = '\00313'
        gray = '\00314'
        light_gray = '\00315'

        reversed = '\017'

        info = navy
        success = green
        warning = yellow
        danger = red
        error = red

        tailed = orange
        untailed = yellow
        client = teal

    @enum.unique
    class Format(_StrEnum):
        default = '\017'

        bold = '\002'
        italics = '\035'
        underline = '\037'

        hidden = '\010'
        beep = '\007'

    DEFAULT_EVENTS = (
        Event.channel_message,
        Event.channel_msg_hilight,
        Event.notice,
        Event.private_message,
        Event.private_message_to_dialog,
        Event.your_message,
    )
    LOG_CONTEXT_NAME = 'log'
    LANGUAGES = ['', 'de', 'ru', 'es', 'fr', 'pt', 'cn', 'it']
    PLATFORMS = {'': 'pc', 'pc': 'pc', 'x': 'x', 'ps': 'ps'}

    def __init__(self, hexchat):
        self.hc = hexchat
        self._cases: t.List[_Case] = []

    def print_info(self, text: str, *, prefix: str = '*', context=None):
        text = f'{prefix}\t{text}' if prefix else text
        context.prnt(text) if context else self.hc.prnt(text)

    def print_error(self, text: str):
        ctx = self.hc.get_context()
        ctx.prnt(f'{self.Color.red}{text}')

    def log(
        self,
        text: str, *,
        prefix: str = '*',
        event: Event = Event.channel_message,
        mode: str = '',
    ):
        ctx = self.hc.find_context(server=self.LOG_CONTEXT_NAME)
        if not ctx:
            self.hc.command(f'newserver -noconnect {self.LOG_CONTEXT_NAME}')
        ctx = self.hc.find_context(server=self.LOG_CONTEXT_NAME)
        ctx.emit_print(event.value, prefix, text, mode)

    def send_command(self, text: str):
        self.hc.command(text)

    def send_message(self, text: str, *, target: str):
        self.send_command(f'MSG {target} {text}')

    def send_reply(self, text: str):
        ctx = self.hc.get_context()
        self.send_message(text, target=ctx.get_info("channel"))

    def match_nicks(self, n1, n2) -> bool:
        return self.hc.nickcmp(n1, n2) == 0

    def strip(self, text: str) -> str:
        return self.hc.strip(text.strip())

    @staticmethod
    def beep():
        winsound.PlaySound(
            '.\\config\\addons\\fur\\assets\\notification.wav',
            winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT,
        )

    def hook_print(
        self, *,
        match_author: t.Optional[t.Union[str, t.Pattern]] = None,
        match_text: t.Optional[t.Union[str, t.Pattern]] = None,
        match_events: t.Iterable['API.Event'] = DEFAULT_EVENTS,
        priority=Priority.normal,
    ):
        def factory(func: t.Callable):
            # noinspection PyUnusedLocal
            def wrapper(word: t.List[str], word_eol: t.List[str],
                        userdata: t.Any):
                channel = self.hc.get_info(self.Info.channel.value)
                server = self.hc.get_info(self.Info.server.value)
                # Make sure we have valid server.
                if not server:
                    return

                # Make sure text data is provided.
                if not word:
                    return

                if match_author and word:
                    if isinstance(match_author, str):
                        if not self.match_nicks(word[0], match_author):
                            return
                    else:
                        if not match_author.match(word[0]):
                            return

                # Match text.
                matches = None
                if match_text and len(word) > 1:
                    if isinstance(match_text, str):
                        if not word[1].startswith(match_text):
                            return
                    else:
                        matches = match_text.match(word[1])
                        if not matches:
                            return
                        matches = matches.groupdict()

                # Run the handler itself.
                text = self.strip(word[1]) if len(word) > 1 else ''
                author = self.strip(word[0]) if word[0] else ''
                if text:
                    # noinspection PyArgumentList
                    result = func(
                        author=author,
                        text=text,
                        mode=word[2] if len(word) > 2 else '',
                        matches=matches,
                        event=self.Event(userdata['event']),
                        channel=channel,
                        server=server,
                        data=userdata,
                    )
                    if result:
                        return result.value

            # Register hooks with hexchat.
            for event in match_events:
                self.hc.hook_print(
                    event.value,
                    wrapper,
                    userdata={'event': event},
                    priority=priority.value,
                )
            return wrapper

        return factory

    def hook_command(
        self, *,
        names: t.Iterable[str],
        description: t.Optional[str] = None,
        userdata: t.Optional[t.Any] = None,
    ):
        def factory(func: t.Callable):
            # noinspection PyUnusedLocal
            def wrapper(word, word_eol, provided_userdata):
                eat = func(args=word[1:], data=provided_userdata)
                if eat:
                    return eat.value

            for name in names:
                self.hc.hook_command(
                    name=name,
                    callback=wrapper,
                    userdata=userdata,
                    help=description,
                )

        return factory

    def _alias_handler(self, args: t.List[str], data):
        (name, command, template, arguments) = data

        # Enforce correct command usage.
        if len(args) < len(arguments):
            self.print_error(
                f'\00304Usage: {name}'
                f'{" ".join(a.upper() for a in arguments)}',
            )

        message = template.format(
            first_arg=args[0],
            rest_args=' '.join(args[1:]) if len(args) > 0 else '',
            command=command,
        )

        # Send the message.
        for line in message.splitlines():
            self.send_reply(line.strip())

        return self.Eat.all

    def register_alias(
        self,
        name: str, *,
        command: str = None,
        template: t.Union[str, t.Dict[str, str]] = None,
        arguments: t.List[str] = None,
        translated=False,
    ):
        languages = self.LANGUAGES if translated else ['']

        for language in languages:
            # Get message template.
            if isinstance(template, dict):
                template = template.get(language) or template.get('')

            userdata = (
                name,
                f'{command or name}{f"-{language}" if language else ""}',
                template or '!{command} {first_arg} {rest_args}',
                arguments or ['nick'],
            )

            description = f'{name} '
            f'{" ".join(a for a in arguments or ["nick"])}'
            self.hook_command(
                names=[
                    f'{name}{f"-{language}" if language else ""}',
                ],
                description=description,
                userdata=userdata,
            )(self._alias_handler)

    def get_case(self, **kwargs) -> t.Optional[_Case]:
        try:
            return next(
                case for case in self._cases if any(
                    getattr(
                        case, k,
                    ) == v and v is not None for k, v in kwargs.items(),
                )
            )
        except StopIteration:
            return

    def get_case_by_rat(self, nick):
        for case in self.get_all_cases():
            for rat in case.get_rats():
                if self.match_nicks(nick, rat):
                    return case

    def put_case(self, **kwargs):
        case = self.get_case(**kwargs)
        if case:
            for k, v in kwargs.items():
                if v is not None:
                    setattr(case, k, v)
        else:
            case = _Case(self, **kwargs)
            self._cases.append(case)

        return case

    def delete_case(self, **kwargs):
        case = self.get_case(**kwargs)
        if case:
            self._cases.remove(case)
            # _utils.close_context(f'#{case.num}')
        return case

    def get_all_cases(self):
        return self._cases[:]
