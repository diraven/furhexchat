from .. import API


def test_ratsignal(api: API):
    api.hc.send_print(
        'RATSIGNAL - '
        'CMDR colonel bagshot - '
        'Reported System: ICZ KI-S B4-5 (60.5 LY from Fuelum) - '
        'Platform: PC - '
        'O2: OK - '
        'Language: German (Germany) (de-DE) '
        '(Case #5) '
        '(PC_SIGNAL)',
        author='MechaSqueak[BOT]',
    )
    case = api.get_case(num='5')
    assert case
    assert case.cmdr == 'colonel bagshot'
    assert case.nick == 'colonel_bagshot'
