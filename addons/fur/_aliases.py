from ._api import API


def init(api: API):
    # Regular
    for alias in [
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
        api.register_alias(alias)

    # Translated only.
    for alias in [
        'prep',
    ]:
        api.register_alias(alias, translated=True)

    # Translated and platformed.
    for alias in [
        'quit',
        'modules',
        'fr',
    ]:
        api.register_alias(alias, translated=True, platformed=True)

    api.register_alias(
        'go', translated=True, arguments=['nick', 'rat1 [rat2...]'],
    )
    api.register_alias('cmdr', arguments=['case', 'cmdr'])
    api.register_alias('sys', arguments=['case', 'system'])
    api.register_alias('ircnick', arguments=['case', 'nick'])
    api.register_alias('inject', arguments=['case', 'text'])
    api.register_alias('sub', arguments=['case', 'line [text]'])

    api.register_alias('wr', command='wing', translated=True, platformed=True)
    api.register_alias('revwr', command='invite', translated=True)
    api.register_alias(
        'bc', command='beacon', translated=True, platformed=True,
    )
    api.register_alias('i', command='inject', arguments=['case', 'text'])

    api.register_alias('hello', template={
        '': 'Welcome to the Fuel rats, {first_arg}. Please tell us once '
            'you\'ve '
            'powered down all of your modules EXCEPT life support, need help '
            'with it or if an "Oxygen depleted in:" timer appear in the upper '
            'right.',
        'de': 'Willkommen bei den Fuel Rats, {first_arg}. Bitte sage '
              'bescheid, '
              'wenn du alle Module AUßER der Lebenserhaltung ausgeschaltet '
              'hast, '
              'wenn du hilfe brauchst oder wenn ein "Sauerstoff aufgebraucht '
              'in:" Zähler in der oberen rechten Ecke auftaucht.',
        'ru': 'Добро пожаловать к Топливным крысам, {first_arg}. Пожалуйста '
              'сообщите нам, когда выключите все модули, кроме системы '
              'жизнеобеспечения, или если появится таймер отсчёта кислорода в '
              'правом верхнем углу экрана.',
        'es': 'Bienvenido/a a las Fuel Rats, {first_arg}. Por favor, '
              'dime cuando '
              'hayas desactivado todos los módulos EXCEPTO el Soporte Vital, '
              'o si necesitas ayuda para hacerlo. Si ves una cuenta "Oxígeno '
              'Agotado en: ", avísame immediatamente.',
        'fr': 'Bienvenue chez les Fuel rats, {first_arg}. Veuillez nous dire '
              'quand '
              'vous avez éteint tous vos modules SAUF les Systèmes de Survie, '
              'si vous avez besoin d\'aide pour le faire ou si un minuteur '
              '"Oxygène épuisé dans :" apparait en haut à droite.',
        'pt': 'Seja bem-vindo ao Fuel Rats, {first_arg}. Por favor, nos avise '
              'assim que você tiver desligado todos os seus modulos EXCETO o '
              'suporte de vida, se precisar de ajuda com isso ou se uma '
              'mensagem '
              'de "Oxigênio esgotado em:" com um temporizador aparecerem no '
              'canto superior direito.',
        'cn': '欢迎来到Fuel Rats，{first_arg}. 请在您关闭所有除Life '
              'Support的组件后通知我。如果您需要说明或者是您看到上右角有"Oxygen Depleted In:"的计时，请通知我。',
        'it': 'Benvenuto/a presso i Fuel Rats, {first_arg}. Per cortesia '
              'avvisaci '
              'non appena hai disattivato tutti i moduli ECCETTO il "Life '
              'Support", in caso tu abbia bisogno di aiuto o se un avviso '
              'con su '
              'scritto "Oxygen depleted in:" e un timer appare nell\'angolo '
              'in '
              'alto a destra.',
    }, translated=True)
    api.register_alias(
        'qeng',
        template={
            '': '{first_arg}: Do you speak English?',
            'de': '{first_arg}: sprechen Sie Englisch?',
            'ru': '{first_arg}: ты говоришь по-английски',
            'es': '¿ {first_arg}: hablas inglés?',
            'fr': '{first_arg}: parlez-vous anglais?',
            'pt': '{first_arg}: fala inglês?',
            'cn': '{first_arg}: 你会说英语吗？',
            'it': '{first_arg}: lei parla inglese?',
        },
        translated=True,
    )
    api.register_alias(
        'qmodules',
        template='{first_arg}: how are those modules coming up? :) Would you '
                 'like '
                 'additional instructions?'
    )
    api.register_alias(
        'qfr',
        template='{first_arg}: how are those friend requests coming along? :) '
                 'Would '
                 'you like additional instructions?'
    )
    api.register_alias(
        'open',
        template='{first_arg}: please exit to the main menu and log back in '
                 'to '
                 'OPEN '
                 'play, then re-disable your thrusters.'
    )
    api.register_alias(
        'qwr',
        template='{first_arg}: how are those wing requests coming along, '
                 'are there '
                 'any issues? :)'
    )
    api.register_alias(
        'qbc',
        template='{first_arg}: how is that wing beacon coming along, '
                 'are there '
                 'any '
                 'issues? :)',
    )
    api.register_alias(
        'qo2',
        template='{first_arg}: do you see an "oxygen depleted in ..." timer '
                 'in '
                 'the '
                 'top right of your HUD?',
    )
    api.register_alias(
        'qsys',
        template='{first_arg}: please, look in the left panel in the '
                 'navigation '
                 'tab '
                 'and give me the full system name under "System" in the top '
                 'left '
                 'corner.',
    )

    api.register_alias(
        'bcalt',
        template='{first_arg}: please go to the Comms Menu on the top left, '
                 'and from the third tab (where you invited your rats to the '
                 'wing) under Options use "Enable Wing Beacon".',
    )

    api.register_alias(
        'mm',
        template='{first_arg}: from THIS point onwards, remain logged out in '
                 'the '
                 'MAIN MENU please! Do NOT login until I give you the "GO GO '
                 'GO" '
                 'command.',
    )
    api.register_alias(
        'qmm',
        template='{first_arg}: please confirm that you\'ve quit to MAIN MENU '
                 'where '
                 'you can see your ship in the hangar.',
    )
    api.register_alias(
        'qmmsys',
        template='{first_arg}: staying in the MAIN MENU, can you confirm your '
                 'full '
                 'system name including any sector name? Look in the upper '
                 'right '
                 'below your commander name where it says / IDLE.',
    )
    api.register_alias(
        'qmmo2',
        template='{first_arg}: staying in the MAIN MENU, do you remember how '
                 'much '
                 'O2 you had left?',
    )
    api.register_alias(
        'qmmo2alt',
        template='{first_arg}: staying in the MAIN MENU, do you remember if '
                 'the '
                 'game asked you to wait for 15 seconds before letting you '
                 'exit '
                 'into main menu?',
    )
    api.register_alias(
        'qmmpos',
        template='{first_arg}: staying in the MAIN MENU, can you remember '
                 'WHERE '
                 'in '
                 'the system you were? By the star, a planet or station or '
                 'on the '
                 'way to one?',
    )
    api.register_alias(
        'mmfr',
        template='{first_arg}: staying in the MAIN MENU, select SOCIAL, '
                 'and search '
                 'for a friend in the upper right. Click them, then click ADD '
                 'FRIEND.?',
    )
    api.register_alias(
        'crplan',
        template='{first_arg}: please, STAY in the MAIN MENU. Overall plan '
                 'will '
                 'be: '
                 '1. Login to OPEN - 2. light your beacon - 3. invite your '
                 'rats '
                 'to a wing - 4. report your o2 time in this chat and be '
                 'ready to '
                 'logout if I tell you to.',
    )
    api.register_alias(
        'crvideo',
        template='{first_arg}: here is a short video on how to do it: '
                 'https://fuelrats.cloud/s/YYzSy2K2QKPfr4X',
    )
    api.register_alias(
        'gogogo',
        template='{first_arg}: GO GO GO! 1. Login to OPEN - 2. light your '
                 'beacon '
                 '- '
                 '3. invite your rat(s) your wing: {rest_args} - 4. report '
                 'your '
                 'o2 time in this chat and be ready to logout if I tell you '
                 'to.',
        arguments=['nick', 'rats...'],
    )

    api.register_alias(
        'ls',
        template='{first_arg}: please turn your Life Support on immediately: '
                 'go '
                 'to '
                 'the right menu -> Modules tab, select Life Support and '
                 'select '
                 'Activate',
    )
    api.register_alias(
        'sr',
        template='{first_arg}: please disable Silent Running Immediately!  '
                 'Default '
                 'key: Delete, or in the Right side Holo Panel > SHIP tab > '
                 'Functions Screen - Middle Right',
    )
    api.register_alias(
        'sc',
        template='{first_arg}: looks like you\'re too close to a stellar '
                 'body or '
                 'a '
                 'fleet carrier. Please, reactivate your thrusters and '
                 'Frameshift '
                 'drive, then un-target everything and jump to supercruise. '
                 'Fly '
                 'away from the stellar body or fleet carrier for about 5 '
                 'light '
                 'seconds, then drop back down into normal space.',
    )
    api.register_alias(
        'eta',
        template='{first_arg}: your rats will be with you in about {'
                 'rest_args}, '
                 'if you see a blue oxygen timer pop up at any time tell me '
                 'immediately.',
        arguments=['client', 'time']
    )
    api.register_alias(
        'scdrop',
        template='{first_arg}: to drop from supercruise slow down to 30km/s, '
                 'open your left menu, navigation tab and select the main '
                 'star in '
                 'your current system (will be the first entry in the list), '
                 'then press the jump button.',
    )
    api.register_alias(
        'bounce',
        template='{first_arg}: if you are using a mobile device or table for '
                 'this '
                 'chat, could you try and make sure the screen stays on so '
                 'that '
                 'you do not get disconnected?',
    )
    api.register_alias(
        'sorry',
        template='{first_arg}: sorry we couldn\'t get to you in time today, '
                 'your rats will be there for you after you respawn to help '
                 'you '
                 'with some tips and tricks, so please stick with them for a '
                 'bit.',
    )
    api.register_alias(
        'fuel',
        template='{first_arg}: you should be receiving fuel now. Please '
                 'remain '
                 'with '
                 'your rats for some quick and helpful tips on fuel '
                 'management.',
    )
    api.register_alias(
        'welcome',
        template='You are most welcome, {first_arg}! Thank you for calling '
                 'us. '
                 'Let the fuel be with you and fly safe, commander! o7',
    )
