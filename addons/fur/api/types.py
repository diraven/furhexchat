import collections
import enum
import typing as t

import hexchat

Alias = collections.namedtuple('Alias', [
    'name',
    'command',
    'arguments',
    'preamble',
    'translated',
    'platformed',
])

LanguageData = collections.namedtuple('LanguageData', ['id', 'postfix'])


@enum.unique
class Language(enum.Enum):
    DEFAULT = LanguageData('', '')
    DE = LanguageData('de', 'de')
    RU = LanguageData('ru', 'ru')
    ES = LanguageData('es', 'es')
    FR = LanguageData('fr', 'fr')
    PT = LanguageData('pt', 'pt')
    CN = LanguageData('cn', 'cn')
    IT = LanguageData('it', 'it')


@enum.unique
class NoLanguage(enum.Enum):
    DEFAULT = LanguageData('', '')


PlatformData = collections.namedtuple('PlatformData', ['id', 'prefix'])


@enum.unique
class Platform(enum.Enum):
    DEFAULT = PlatformData('', 'pc')
    PC = PlatformData('pc', 'pc')
    XBOX = PlatformData('x', 'x')
    PLAYSTATION = PlatformData('ps', 'ps')


@enum.unique
class NoPlatform(enum.Enum):
    DEFAULT = PlatformData('', '')


@enum.unique
class Event(enum.Enum):
    ADD_NOTIFY = 'Add Notify'
    BAN_LIST = 'Ban List'
    BANNED = 'Banned'
    BEEP = 'Beep'
    CAPABILITY_ACKNOWLEDGEMENT = 'Capability Acknowledgement'
    CAPABILITY_DELETED = 'Capability Deleted'
    CAPABILITY_LIST = 'Capability List'
    CAPABILITY_REQUEST = 'Capability Request'
    CHANGE_NICK = 'Change Nick'
    CHANNEL_ACTION = 'Channel Action'
    CHANNEL_ACTION_HILIGHT = 'Channel Action Hilight'
    CHANNEL_BAN = 'Channel Ban'
    CHANNEL_CREATION = 'Channel Creation'
    CHANNEL_DEHALFOP = 'Channel DeHalfOp'
    CHANNEL_DEOP = 'Channel DeOp'
    CHANNEL_DEVOICE = 'Channel DeVoice'
    CHANNEL_EXEMPT = 'Channel Exempt'
    CHANNEL_HALF_OPERATOR = 'Channel Half-Operator'
    CHANNEL_INVITE = 'Channel INVITE'
    CHANNEL_LIST = 'Channel List'
    CHANNEL_MESSAGE = 'Channel Message'
    CHANNEL_MODE_GENERIC = 'Channel Mode Generic'
    CHANNEL_MODES = 'Channel Modes'
    CHANNEL_MSG_HILIGHT = 'Channel Msg Hilight'
    CHANNEL_NOTICE = 'Channel Notice'
    CHANNEL_OPERATOR = 'Channel Operator'
    CHANNEL_QUIET = 'Channel Quiet'
    CHANNEL_REMOVE_EXEMPT = 'Channel Remove Exempt'
    CHANNEL_REMOVE_INVITE = 'Channel Remove Invite'
    CHANNEL_REMOVE_KEYWORD = 'Channel Remove Keyword'
    CHANNEL_REMOVE_LIMIT = 'Channel Remove Limit'
    CHANNEL_SET_KEY = 'Channel Set Key'
    CHANNEL_SET_LIMIT = 'Channel Set Limit'
    CHANNEL_UNBAN = 'Channel UnBan'
    CHANNEL_UNQUIET = 'Channel UnQuiet'
    CHANNEL_URL = 'Channel Url'
    CHANNEL_VOICE = 'Channel Voice'
    CONNECTED = 'Connected'
    CONNECTING = 'Connecting'
    CONNECTION_FAILED = 'Connection Failed'
    CTCP_GENERIC = 'CTCP Generic'
    CTCP_GENERIC_TO_CHANNEL = 'CTCP Generic to Channel'
    CTCP_SEND = 'CTCP Send'
    CTCP_SOUND = 'CTCP Sound'
    CTCP_SOUND_TO_CHANNEL = 'CTCP Sound to Channel'
    DCC_CHAT_ABORT = 'DCC CHAT Abort'
    DCC_CHAT_CONNECT = 'DCC CHAT Connect'
    DCC_CHAT_FAILED = 'DCC CHAT Failed'
    DCC_CHAT_OFFER = 'DCC CHAT Offer'
    DCC_CHAT_OFFERING = 'DCC CHAT Offering'
    DCC_CHAT_REOFFER = 'DCC CHAT Reoffer'
    DCC_CONECTION_FAILED = 'DCC Conection Failed'
    DCC_GENERIC_OFFER = 'DCC Generic Offer'
    DCC_HEADER = 'DCC Header'
    DCC_MALFORMED = 'DCC Malformed'
    DCC_OFFER = 'DCC Offer'
    DCC_OFFER_NOT_VALID = 'DCC Offer Not Valid'
    DCC_RECV_ABORT = 'DCC RECV Abort'
    DCC_RECV_COMPLETE = 'DCC RECV Complete'
    DCC_RECV_CONNECT = 'DCC RECV Connect'
    DCC_RECV_FAILED = 'DCC RECV Failed'
    DCC_RECV_FILE_OPEN_ERROR = 'DCC RECV File Open Error'
    DCC_RENAME = 'DCC Rename'
    DCC_RESUME_REQUEST = 'DCC RESUME Request'
    DCC_SEND_ABORT = 'DCC SEND Abort'
    DCC_SEND_COMPLETE = 'DCC SEND Complete'
    DCC_SEND_CONNECT = 'DCC SEND Connect'
    DCC_SEND_FAILED = 'DCC SEND Failed'
    DCC_SEND_OFFER = 'DCC SEND Offer'
    DCC_STALL = 'DCC Stall'
    DCC_TIMEOUT = 'DCC Timeout'
    DELETE_NOTIFY = 'Delete Notify'
    DISCONNECTED = 'Disconnected'
    FOUND_IP = 'Found IP'
    GENERIC_MESSAGE = 'Generic Message'
    IGNORE_ADD = 'Ignore Add'
    IGNORE_CHANGED = 'Ignore Changed'
    IGNORE_FOOTER = 'Ignore Footer'
    IGNORE_HEADER = 'Ignore Header'
    IGNORE_REMOVE = 'Ignore Remove'
    IGNORELIST_EMPTY = 'Ignorelist Empty'
    INVITE = 'Invite'
    INVITED = 'Invited'
    JOIN = 'Join'
    KEYWORD = 'Keyword'
    KICK = 'Kick'
    KILLED = 'Killed'
    MESSAGE_SEND = 'Message Send'
    MOTD = 'Motd'
    MOTD_SKIPPED = 'MOTD Skipped'
    NICK_CLASH = 'Nick Clash'
    NICK_ERRONEOUS = 'Nick Erroneous'
    NICK_FAILED = 'Nick Failed'
    NO_DCC = 'No DCC'
    NO_RUNNING_PROCESS = 'No Running Process'
    NOTICE = 'Notice'
    NOTICE_SEND = 'Notice Send'
    NOTIFY_AWAY = 'Notify Away'
    NOTIFY_BACK = 'Notify Back'
    NOTIFY_EMPTY = 'Notify Empty'
    NOTIFY_HEADER = 'Notify Header'
    NOTIFY_NUMBER = 'Notify Number'
    NOTIFY_OFFLINE = 'Notify Offline'
    NOTIFY_ONLINE = 'Notify Online'
    OPEN_DIALOG = 'Open Dialog'
    PART = 'Part'
    PART_WITH_REASON = 'Part with Reason'
    PING_REPLY = 'Ping Reply'
    PING_TIMEOUT = 'Ping Timeout'
    PRIVATE_ACTION = 'Private Action'
    PRIVATE_ACTION_TO_DIALOG = 'Private Action to Dialog'
    PRIVATE_MESSAGE = 'Private Message'
    PRIVATE_MESSAGE_TO_DIALOG = 'Private Message to Dialog'
    PROCESS_ALREADY_RUNNING = 'Process Already Running'
    QUIT = 'Quit'
    RAW_MODES = 'Raw Modes'
    RECEIVE_WALLOPS = 'Receive Wallops'
    RESOLVING_USER = 'Resolving User'
    SASL_AUTHENTICATING = 'SASL Authenticating'
    SASL_RESPONSE = 'SASL Response'
    SERVER_CONNECTED = 'Server Connected'
    SERVER_ERROR = 'Server Error'
    SERVER_LOOKUP = 'Server Lookup'
    SERVER_NOTICE = 'Server Notice'
    SERVER_TEXT = 'Server Text'
    SSL_MESSAGE = 'SSL Message'
    STOP_CONNECTION = 'Stop Connection'
    TOPIC = 'Topic'
    TOPIC_CHANGE = 'Topic Change'
    TOPIC_CREATION = 'Topic Creation'
    UNKNOWN_HOST = 'Unknown Host'
    USER_LIMIT = 'User Limit'
    USERS_ON_CHANNEL = 'Users On Channel'
    WHOIS_AUTHENTICATED = 'WhoIs Authenticated'
    WHOIS_AWAY_LINE = 'WhoIs Away Line'
    WHOIS_CHANNEL_OPER_LINE = 'WhoIs Channel/Oper Line'
    WHOIS_END = 'WhoIs End'
    WHOIS_IDENTIFIED = 'WhoIs Identified'
    WHOIS_IDLE_LINE = 'WhoIs Idle Line'
    WHOIS_IDLE_LINE_WITH_SIGNON = 'WhoIs Idle Line with Signon'
    WHOIS_NAME_LINE = 'WhoIs Name Line'
    WHOIS_REAL_HOST = 'WhoIs Real Host'
    WHOIS_SERVER_LINE = 'WhoIs Server Line'
    WHOIS_SPECIAL = 'WhoIs Special'
    YOU_JOIN = 'You Join'
    YOU_KICKED = 'You Kicked'
    YOU_PART = 'You Part'
    YOU_PART_WITH_REASON = 'You Part with Reason'
    YOUR_ACTION = 'Your Action'
    YOUR_INVITATION = 'Your Invitation'
    YOUR_MESSAGE = 'Your Message'
    YOUR_NICK_CHANGING = 'Your Nick Changing'


class Color(enum.Enum):
    DEFAULT = '\003'
    WHITE = '\00300'
    BLACK = '\00301'
    NAVY = '\00302'
    GREEN = '\00303'
    RED = '\00304'
    MAROON = '\00305'
    PURPLE = '\00306'
    ORANGE = '\00307'
    YELLOW = '\00308'
    LIGHT_GREEN = '\00309'
    TEAL = '\00310'
    CYAN = '\00311'
    ROYAL_BLUE = '\00312'
    MAGENTA = '\00313'
    GRAY = '\00314'
    LIGHT_GRAY = '\00315'

    INFO = NAVY
    SUCCESS = GREEN
    WARNING = YELLOW
    ERROR = RED


@enum.unique
class Label(enum.Enum):
    INFO = f'{Color.INFO.value}info{Color.DEFAULT.value}'
    SUCCESS = f'{Color.SUCCESS.value}success{Color.DEFAULT.value}'
    WARNING = f'{Color.WARNING.value}warning{Color.DEFAULT.value}'
    ERROR = f'{Color.ERROR.value}error{Color.DEFAULT.value}'


@enum.unique
class Eat(enum.Enum):
    ALL = hexchat.EAT_ALL
    NONE = hexchat.EAT_NONE
    PLUGIN = hexchat.EAT_PLUGIN
    HEXCHAT = hexchat.EAT_HEXCHAT


class Rat(t.TypedDict):
    case_num: int
    cmdr: str
    nick: str
    fr: t.Optional[bool]
    wr: t.Optional[bool]
    bc: t.Optional[bool]
    fuel: t.Optional[bool]


class Case(t.TypedDict):
    num: int
    cmdr: str
    is_active: bool
    is_cr: bool

    nick: str
    language: str
    platform: Platform

    system: str
    landmark: str


class State(t.TypedDict):
    cases: t.List[Case]
    rats: t.List[Rat]