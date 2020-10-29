import enum

import hexchat as _hexchat


class StrEnum(enum.Enum):
    def __str__(self):
        return str(self.value)


@enum.unique
class Priority(enum.Enum):
    highest = _hexchat.PRI_HIGHEST
    high = _hexchat.PRI_HIGH
    normal = _hexchat.PRI_NORM
    low = _hexchat.PRI_LOW
    lowest = _hexchat.PRI_LOWEST


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


DEFAULT_EVENTS = [
    Event.channel_message,
    Event.channel_msg_hilight,
    Event.your_message,
    Event.notice,
    Event.private_message,
    Event.private_message_to_dialog,
]


class Color(StrEnum):
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
class Eat(enum.Enum):
    all = _hexchat.EAT_ALL
    hexchat = _hexchat.EAT_HEXCHAT
    none = _hexchat.EAT_NONE
    plugin = _hexchat.EAT_PLUGIN


@enum.unique
class Format(StrEnum):
    default = '\017'

    bold = '\002'
    italics = '\035'
    underline = '\037'

    hidden = '\010'
    beep = '\007'


NOOP = ' ..'
