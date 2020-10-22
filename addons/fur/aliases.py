from .api import register_alias

register_alias(
    name='prep', command='prep', translated=True,
)
register_alias(
    name='quit', command='quit', translated=True, platformed=True,
)
register_alias(
    name='modules', command='modules', translated=True, platformed=True,
)
register_alias(
    name='go', command='go', translated=True,
)
register_alias(
    name='fr', command='fr', translated=True, platformed=True,
)
register_alias(
    name='wr', command='wing', translated=True, platformed=True,
)
register_alias(
    name='bc', command='beacon', translated=True, platformed=True,
)

register_alias(name='hello', command='', messages=[{
    '': 'Welcome to the Fuel rats, {word[1]}. Please tell us once you\'ve '
        'powered down all of your modules EXCEPT life support, need help '
        'with it or if an "Oxygen depleted in:" timer appear in the upper '
        'right.',
    'de': 'Willkommen bei den Fuel Rats, {word[1]}. Bitte sage bescheid, '
          'wenn du alle Module AUßER der Lebenserhaltung ausgeschaltet hast, '
          'wenn du hilfe brauchst oder wenn ein "Sauerstoff aufgebraucht '
          'in:" Zähler in der oberen rechten Ecke auftaucht.',
    'ru': 'Добро пожаловать к Топливным крысам, {word[1]}. Пожалуйста '
          'сообщите нам, когда выключите все модули, кроме системы '
          'жизнеобеспечения, или если появится таймер отсчёта кислорода в '
          'правом верхнем углу экрана.',
    'es': 'Bienvenido/a a las Fuel Rats, {word[1]}. Por favor, dime cuando '
          'hayas desactivado todos los módulos EXCEPTO el Soporte Vital, '
          'o si necesitas ayuda para hacerlo. Si ves una cuenta "Oxígeno '
          'Agotado en: ", avísame immediatamente.',
    'fr': 'Bienvenue chez les Fuel rats, {word[1]}. Veuillez nous dire quand '
          'vous avez éteint tous vos modules SAUF les Systèmes de Survie, '
          'si vous avez besoin d\'aide pour le faire ou si un minuteur '
          '"Oxygène épuisé dans :" apparait en haut à droite.',
    'pt': 'Seja bem-vindo ao Fuel Rats, {word[1]}. Por favor, nos avise '
          'assim que você tiver desligado todos os seus modulos EXCETO o '
          'suporte de vida, se precisar de ajuda com isso ou se uma mensagem '
          'de "Oxigênio esgotado em:" com um temporizador aparecerem no '
          'canto superior direito.',
    'cn': '欢迎来到Fuel Rats，{word[1]}. 请在您关闭所有除Life '
          'Support的组件后通知我。如果您需要说明或者是您看到上右角有"Oxygen Depleted In:"的计时，请通知我。',
    'it': 'Benvenuto/a presso i Fuel Rats, {word[1]}. Per cortesia avvisaci '
          'non appena hai disattivato tutti i moduli ECCETTO il "Life '
          'Support", in caso tu abbia bisogno di aiuto o se un avviso con su '
          'scritto "Oxygen depleted in:" e un timer appare nell\'angolo in '
          'alto a destra.',
}], translated=True)
register_alias(name='qeng', command='', messages=[{
    '': '{word[1]}: Do you speak English?',
    'de': '{word[1]}: sprechen Sie Englisch?',
    'ru': '{word[1]}: ты говоришь по-английски',
    'es': '¿ {word[1]}: hablas inglés?',
    'fr': '{word[1]}: parlez-vous anglais?',
    'pt': '{word[1]}: fala inglês?',
    'cn': '{word[1]}: 你会说英语吗？',
    'it': '{word[1]}: lei parla inglese?',
}], translated=True)
register_alias(name='qmodules', messages=[
    '{word[1]}: how are those modules coming up? :) Would you like '
    'additional instructions?'
])
register_alias(name='qfr', messages=[
    '{word[1]}: how are those friend requests coming along? :) Would you '
    'like additional instructions?'
])
register_alias(name='open', messages=[
    '{word[1]}: please exit to the main menu and log back in to OPEN '
    'play, then re-disable your thrusters.'
])
register_alias(name='qwr', messages=[
    '{word[1]}: how are those wing requests coming along, are there any '
    'issues? :)'
])
register_alias(name='qbc', messages=[
    '{word[1]}: how is that wing beacon coming along, are there any '
    'issues? :)',
])
register_alias(name='qo2', messages=[
    '{word[1]}: do you see an "oxygen depleted in ..." timer in the top '
    'right of your HUD?',
])
register_alias(name='qsys', messages=[
    '{word[1]}: please, look in the left panel in the navigation tab and '
    'give me the full '
    'system name under "System" in the top left corner.',
])

register_alias(name='revwr', command='invite', messages=[
    '{word[2]} revwr pls.',
    '{word[1]}: one of your rat(s) will now send you wing invite, '
    'please accept.',
    '{cmd} {word[1]}',
], arguments=['ircname', 'ratname'], translated=True)
register_alias(name='bcalt', messages=[
    '{word[1]}: please go to the Comms Menu on the top left, and from the '
    'third tab (where you invited your rats to the wing) under Options use '
    '"Enable Wing Beacon".',
])

register_alias(name='mm', messages=[
    '{word[1]}: from THIS point onwards, remain logged out in the MAIN '
    'MENU please! '
    'Do NOT login until I give you the "GO GO GO" command.',
])
register_alias(name='qmm', messages=[
    '{word[1]}: please confirm that you\'ve quit to MAIN MENU where you '
    'can see your ship in the hangar.',
])
register_alias(name='qmmsys', messages=[
    '{word[1]}: staying in the MAIN MENU, can you confirm your full '
    'system name including any sector name? '
    'Look in the upper right below your CMDR name where it says / IDLE.',
])
register_alias(name='qmmo2', messages=[
    '{word[1]}: staying in the MAIN MENU, do you remember how much O2 '
    'you had left?',
])
register_alias(name='qmmo2alt', messages=[
    '{word[1]}: staying in the MAIN MENU, do you remember if the game '
    'asked you to wait for 15 seconds before '
    'letting you exit into main menu?',
])
register_alias(name='qmmpos', messages=[
    '{word[1]}: staying in the MAIN MENU, can you remember WHERE in the '
    'system you were? By the star, '
    'a planet or station or on the way to one?',
])
register_alias(name='mmfr', messages=[
    '{word[1]}: staying in the MAIN MENU, select SOCIAL, and search for '
    'a friend in the upper right. '
    'Click them, then click ADD FRIEND.?',
])
register_alias(name='crplan', messages=[
    '{word[1]}: please, STAY in the MAIN MENU. Overall plan will be: '
    '1. Login to OPEN - 2. light your beacon - 3. invite your rats to a '
    'wing - '
    '4. report your o2 time in this chat and be ready to logout if I '
    'tell you to.',
])
register_alias(name='crvideo', messages=[
    '{word[1]}: here is a short video on how to do it: '
    'https://fuelrats.cloud/s/YYzSy2K2QKPfr4X ю',
])
register_alias(name='gogogo', messages=[
    '{word[1]}: GO GO GO! 1. Login to OPEN - '
    '2. light your beacon - '
    '3. invite your rat(s) your wing: {word_eol[2]} - '
    '4. report your o2 time in this chat and be ready to logout if I '
    'tell you to.',
], arguments=['ircname', 'rats...'])

register_alias(name='ls', messages=[
    '{word[1]}: please turn your Life Support on immediately: go to the '
    'right menu -> '
    'Modules tab, select Life Support and select Activate',
])
register_alias(name='sr', messages=[
    '{word[1]}: please disable Silent Running Immediately!  Default key: '
    'Delete, or in the Right side Holo Panel > SHIP tab > Functions '
    'Screen - Middle Right',
])
register_alias(name='sc', messages=[
    '{word[1]}: looks like you\'re too close to a stellar body or a '
    'fleet carrier. '
    'Please, reactivate your thrusters and Frameshift drive, '
    'then un-target everything and jump to supercruise. '
    'Fly away from the stellar body or fleet carrier for about 5 light '
    'seconds, '
    'then drop back down into normal space.',
])
register_alias(name='eta', messages=[
    '{word[1]}: your rats will be with you in about {word_eol[2]}, '
    'if you see a blue oxygen timer pop up at any time tell me '
    'immediately.',
], arguments=['client', 'time'])
register_alias(name='scdrop', messages=[
    '{word[1]}: to drop from supercruise slow down to 30km/s, open your '
    'left menu, '
    'navigation tab and select the main star in your current system ('
    'will be the first '
    'entry in the list), then press the jump button.',
])
register_alias(name='bounce', messages=[
    '{word[1]}: if you are using a mobile device or table for this chat, '
    'could you try and make sure the screen stays on so that you do not get '
    'disconnected?',
])
register_alias(name='sorry', command='clear', messages=[
    '{word[1]}: sorry we couldn\'t get to you in time today, your rats '
    'will be there for you after you respawn to help you with some tips '
    'and tricks, so please stick with them for a bit.',
    '{cmd} {word[1]}',
])
register_alias(name='clear', command='clear', messages=[
    '{word[1]}: you should be receiving fuel now. Please remain with '
    'your rats for '
    'some quick and helpful tips on fuel management.',
    '{cmd} {word_eol[1]}',
], arguments=['ircname', 'rat'])

for cmd_name in [
    'pc',
    'xb',
    'ps',
    'quote',
    'active',
    'grab',
    'cr',
    'multi',
    'md',
    'pg',
    'tweetc',
]:
    register_alias(name=cmd_name, command=cmd_name)

register_alias(
    name='sys', command='sys', arguments=['casenum', 'system_name'],
)
register_alias(
    name='cmdr', command='cmdr', arguments=['casenum', 'new_cmdr_name'],
)
register_alias(
    name='ircnick', command='ircnick', arguments=['casenum', 'new_nick'],
)
register_alias(
    name='inject', command='inject', arguments=['casenum', 'text'],
)
register_alias(
    name='sub', command='sub', arguments=['casenum', 'linenum [text]'],
)
