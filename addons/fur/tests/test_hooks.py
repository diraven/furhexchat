import pytest

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


@pytest.mark.parametrize('cmd', [
    '!close 0',
    '!clear 0',
    '!md #0',
    '!trash #0',
])
def test_case_close(api: API, cmd):
    api.put_case(num='0', cmdr='some client')
    api.put_case(num='1', cmdr='some other client')
    api.hc.send_print(cmd)
    assert api.get_case(num='0') is None
    assert api.get_case(num='1')
