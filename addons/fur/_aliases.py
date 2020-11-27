from ._api import API


def init(api: API):
    # Regular
    for alias in [
        'pc', 'xb', 'ps',
        'multi',
        'go', 'gofr',
        'grab', 'active', 'cr', 'cmdr', 'sys', 'ircnick', 'inject', 'sub',
        'clear',
        'pg', 'invite',
    ]:
        api.register_alias(alias)

    # Translated only.
    for alias in [
        'prep',
        'quit',
        'modules',
        'fr',
        'crinst',
    ]:
        api.register_alias(alias, translated=True)

    api.register_alias('wr', command='wing', translated=True)
    api.register_alias('bc', command='beacon', translated=True)
    api.register_alias('i', command='inject', arguments=['case', 'text'])

    api.register_alias('hello', templates={
        '': 'Welcome to the Fuel rats, {first_arg}. Please tell us once '
            'you\'ve powered down all of your modules EXCEPT life support, '
            'need help with it or if an "Oxygen depleted in:" timer appear '
            'in the upper right.',
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
    })
    api.register_alias('qeng', templates={
        '': '{first_arg}: Do you speak English?',
        'de': '{first_arg}: sprechen Sie Englisch?',
        'ru': '{first_arg}: вы понимаете английский?',
        'es': '¿ {first_arg}: hablas inglés?',
        'fr': '{first_arg}: parlez-vous anglais?',
        'pt': '{first_arg}: fala inglês?',
        'cn': '{first_arg}: 你会说英语吗？',
        'it': '{first_arg}: lei parla inglese?',
    })
    api.register_alias('qmodules', templates={
        '': '{first_arg}: how are those modules coming up?',
        'ru': '{first_arg}: как там с модулями, получается отключить?',
    })
    api.register_alias('qfr', templates={
        '': '{first_arg}: how are those friend requests coming along?',
        'ru': '{first_arg}: получается добавить крыс в друзья?',
    })
    api.register_alias('open', templates={
        '': '{first_arg}: please exit to the main menu and log back in '
            'to OPEN play, then re-disable your thrusters.',
        'ru': '{first_arg}: выйдите в главное меню и перезайдите в '
              'ОТКРЫТУЮ ИГРУ, пожалуйста. И снова отключите двигатели.',
    })
    api.register_alias('qwr', templates={
        '': '{first_arg}: how are those wing requests coming along?',
        'ru': '{first_arg}: получается пригласить крыс в крыло?',
    })
    api.register_alias('qbc', templates={
        '': '{first_arg}: how is that wing beacon coming along?',
        'ru': '{first_arg}: получается включить маяк?',
    })
    api.register_alias('qo2', templates={
        '': '{first_arg}: do you see an "oxygen depleted in ..." timer in '
            'the top right of your HUD?',
        'ru': '{first_arg}: вы видите таймер "кислород закончится через..." '
              'в правом верхнем углу экрана?',
    })
    api.register_alias('qsys', templates={
        '': '{first_arg}: please, look in the left panel in the navigation '
            'tab and give me the full system name under "System" in the top '
            'left corner.',
        'ru': '{first_arg}: пожалуйста, посмотрите в левой панели на закладке '
              '"навигация" и скажите пожалуйста полное имя системы под '
              'надписью "Система:" в левом верхнем углу.',
    })
    api.register_alias('bcalt', templates={
        '': '{first_arg}: please go to the Comms Menu on the top left, '
            'and from the third tab (where you invited your rats to the '
            'wing) under Options use "Enable Wing Beacon".',
        'ru': '{first_arg}: пожалуйста, воспользуйтесь меню коммуникаций '
              '(верхним), и в третьей вкладке (где вы приглашали крыс в крыло '
              'в "опциях" выберите "Включить Маяк Крыла".',
    })
    api.register_alias('mm', templates={
        '': '{first_arg}: from THIS point onwards, remain logged out in '
            'the MAIN MENU please! Do NOT login until I give you the "GO '
            'GO GO" command.',
        'ru': '{first_arg}: теперь, пожалуйста, что бы ни происходило - '
              'оставайтесь в главном меню и не заходите в игру пока не '
              'увидите команду "ВПЕРЁД!".',
    })
    api.register_alias('qmm', templates={
        '': '{first_arg}: please confirm that you\'ve quit to MAIN MENU '
            'where you can see your ship in the hangar.',
        'ru': '{first_arg}: пожалуйста, подтвердите что находитесь в главном '
              'меню и можете видеть свой корабль в ангаре.',
    })
    api.register_alias('qmmsys', templates={
        '': '{first_arg}: staying in the MAIN MENU, can you confirm your '
            'full system name including any sector name? Look in the upper '
            'right below your commander name where it says / IDLE.',
        'ru': '{first_arg}: оставаясь в главном меню, сообщите пожалуйста '
              'название системы, включая название сектора, если оно есть - '
              'ищите в правом верхнем углу экрана где написано имя вашего '
              'коммандера.',
    })
    api.register_alias('qmmo2', templates={
        '': '{first_arg}: staying in the MAIN MENU, do you remember how '
            'much O2 you had left?',
        'ru': '{first_arg}: оставаясь в главном меню, попробуйте вспомнить'
              'сколько времени у вас оставалось на таймере кислорода?',
    })
    api.register_alias('qmmo2alt', templates={
        '': '{first_arg}: staying in the MAIN MENU, do you remember if the '
            'game asked you to wait for 15 seconds before letting you exit '
            'into main menu?',
        'ru': '{first_arg}: оставаясь в главном меню, попробуйте вспомнить, '
              'перед тем как позволить вам выйти в главное меню, игра '
              'заставляла вас подождать 15 секунд?',
    })
    api.register_alias('qmmpos', templates={
        '': '{first_arg}: staying in the MAIN MENU, can you remember WHERE '
            'in the system you were? By the star, a planet or station or '
            'on the way to one?',
        'ru': '{first_arg}: оставаясь в главном меню, попробуйте вспомнить, '
              'где вы находились в системе, у звезды, планеты, или на пути '
              'куда-нибудь?',
    })
    api.register_alias('crplan', templates={
        '': '{first_arg}: please, STAY in the MAIN MENU. Overall plan will '
            'be: 1. Login to OPEN | 2. light your BEACON | 3. invite your '
            'rats to a WING | 4. REPORT O2 time in this chat and be '
            'ready to logout if I tell you to.',
        'ru': '{first_arg}: пожалуйста, ОСТАВАЙТЕСЬ в ГЛАВНОМ МЕНЮ. В целом, '
              'план будет такой: 1. войти в ОТКРЫТУЮ ИГРУ | 2. включить МАЯК '
              '| 3. пригласить крыс КРЫЛО | 4. сообщить время на таймере '
              'кислорода и быть готовым выйти в главное меню если я об этом '
              'попрошу.',
    })
    api.register_alias('crvideo', templates={
        '': '{first_arg}: here is a short video on how to do it: '
            'https://fuelrats.cloud/s/YYzSy2K2QKPfr4X',
        'ru': '{first_arg}: вот кратенькое видео как это сделать: '
              'https://fuelrats.cloud/s/YYzSy2K2QKPfr4X',
    })
    api.register_alias('gogogo', templates={
        '': '{first_arg}: GO GO GO! 1. OPEN GAME | 2. light BEACON | 3. '
            'invite to WING: {rest_args} | 4. REPORT O2, be ready to '
            'logout if asked.\n'
            '!beacon {first_arg}\n'
            '!wing {first_arg}',
        'ru': '{first_arg}: ВПЕРЁД! 1. ОТКРЫТАЯ ИГРА | 2. зажечь МАЯК | 3. '
              'пригласить в КРЫЛО: {rest_args} | 4. Сообщить ОСТАТОК '
              'КИСЛОРОДА, быть готовым выйти в главное меню если попросят.\n'
              '!beacon-ru {first_arg}\n'
              '!wing-ru {first_arg}',
    })
    api.register_alias('ls', templates={
        '': '{first_arg}: please turn your Life Support on immediately: go '
            'to the right menu -> Modules tab, select Life Support and '
            'select Activate',
        'ru': '{first_arg}: пожалуйста, немедленно включите свою Сист. '
              'Жизнеобеспечения: правое меню -> Подисистемы корабля, выберите '
              'Сист. Жизнеобеспечения. и включите её.',
    })
    api.register_alias('sc', templates={
        '': '{first_arg}: looks like you\'re too close to a massive '
            'object. Please, reactivate your thrusters and Frameshift '
            'drive, then un-target everything and jump to supercruise. Fly '
            'away from the massive object for about 5 light seconds, '
            'then drop back down into normal space.',
        'ru': '{first_arg}: похоже, вы находитесь слишком близко от массивного'
              'объекта. Пожалуйста, включите обычные и рамочно-смесительные '
              'двигатели, выберите в цель первый пункт в левом меню '
              '"навигация", и выйдите в суперкруз. Отлетите от объекта прибл. '
              'на 5 сеетовых секунд и выйдите из суперкруза в обычное '
              'пространство.',
    })
    api.register_alias('scdrop', templates={
        '': '{first_arg}: to drop from supercruise slow down to 30km/s, '
            'open your left menu, navigation tab and select the main star '
            'in your current system (will be the first entry in the list), '
            'then press the jump button (J by default).',
        'ru': '{first_arg}: чтобы выйти из суперкруза, замедлитесь до '
              '30км/сек, откройте левое меню, вкладка "навигация" выберите '
              'первый элемент списка, потом нажмите кнопку прыжка (J по '
              'умолчанию).',
    })
    api.register_alias('bounce', templates={
        '': '{first_arg}: if you are using a mobile device or table for '
            'this chat, could you try and make sure the screen stays on so '
            'that you do not get disconnected?',
        'ru': '{first_arg}: если вы пользуетесь мобильным устройством для '
              'этого чата, не могли бы ли вы убедиться что экран остаётся '
              'включенным, чтобы чат не отсоединялся?',
    })
    api.register_alias('sorry', templates={
        '': '{first_arg}: sorry we couldn\'t get to you in time today, '
            'your rats will be there for you after you respawn to help you '
            'with some tips and tricks, so please stick with them for a '
            'bit.',
        'ru': '{first_arg}: нам очень жаль что мы не смогли добраться до вас '
              'вовремя сегодня... Пожалуйста, оставайтесь с вашими крысами '
              'для несолькоих полезных советов по менеджменту топлива.',
    })
    api.register_alias('fuel', templates={
        '': '{first_arg}: you should be receiving fuel now. Please remain '
            'with your rats for some quick and helpful tips on fuel '
            'management.',
        'ru': '{first_arg}: вас должны были заправить. Пожалуйста, '
              'оставайтесь с вашими крысами для несолькоих полезных '
              'советов по менеджменту топлива.',
    })
    api.register_alias('welcome', templates={
        '': 'You are most welcome, {first_arg}! Thank you for calling us. '
            'Let the fuel be with you and fly safe, commander! o7',
        'ru': '{first_arg}: рады помочь! Спасибо что обратились к нам. '
              'Безопасных полётов и да пребует с вами топливо! o7',
    })
