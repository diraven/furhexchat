from .. import API


def test_ratsignal(api: API):
    api.hc.send_print(
        'RATSIGNAL - '
        'CMDR some client - '
        'Reported System: ICZ KI-S B4-5 (60.5 LY from Fuelum) - '
        'Platform: PC - '
        'O2: OK - '
        'Language: English (English) (en-EN) '
        '(Case #5) '
        '(PC_SIGNAL)',
        author='MechaSqueak[BOT]',
    )
    case = api.get_case(num='5')
    assert case
    assert case.cmdr == 'some client'
    assert case.nick == 'some_client'


def test_incoming_client(api: API):
    api.hc.send_print(
        'Incoming Client: some client - '
        'System: core sys sector fb-0 a6-3 - '
        'Platform: PC - '
        'O2: OK - '
        'Language: English (en-US)',
        author='RatMama[BOT]',
    )
    case = api.get_case(nick='some_client')
    assert case
    assert case.cmdr == 'some client'
    assert case.nick == 'some_client'
    assert case.num is None
