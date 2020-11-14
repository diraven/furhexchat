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


@pytest.mark.parametrize('cmd', [
    '!nick 0 other_nick',
    '!nick #0 other_nick',
])
def test_case_nick(api: API, cmd):
    api.put_case(num='0', cmdr='some client')
    api.hc.send_print(cmd)
    assert api.get_case(num='0').nick == 'other_nick'


def test_cases_found(api: API):
    api.hc.send_print(
        '4 cases found, '
        '[2] (Weird Name#2) (PC)  , '
        '[3] 1NumberName (PC)  , '
        '[4] Three Words Name (PC)  , '
        '[5] Other Name (PC)  , '
        '[6] CMDR_NAME (PS4) (CR)  , '
        '[7] CMDR-NAME (PS4) (CR) ',
        author='MechaSqueak[BOT]',
    )
    assert len(api.get_all_cases()) == 6
    assert api.get_case(num='2').nick == 'Weird_Name#2'
    assert api.get_case(num='3').nick == 'c_1NumberName'
    assert api.get_case(num='4').nick == 'Three_Words_Name'
    assert api.get_case(num='5').nick == 'Other_Name'
    assert api.get_case(num='6').nick == 'CMDR_NAME'
    assert api.get_case(num='7').nick == 'CMDRNAME'


@pytest.mark.parametrize('msg, highlighted_msg', [
    (
        'fr+',
        f'{API.Color.success}fr+{API.Color.default}'),
    (
        'wr+',
        f'{API.Color.success}wr+{API.Color.default}',
    ),
    (
        '#1 sys-',
        f'{API.Color.info}#1{API.Color.default} '
        f'{API.Color.danger}sys-{API.Color.default}',
    ),
    (
        'prep-',
        f'{API.Color.danger}prep-{API.Color.default}',
    ),
])
def test_highlights(api: API, msg, highlighted_msg):
    author = 'SomeRat'
    api.hc.send_print(msg, author=author)
    prefix = f'{API.Color.untailed}{author}{API.Color.default}'
    assert api.hc.prnt.call_args[0][0] == f'{prefix}\t-\n{highlighted_msg}'


def test_calls(api: API):
    case = api.put_case(num='0', cmdr='some client')
    case.put_rat('Rat1')
    case.put_rat('Rat2')
    api.hc.send_print('#0 fr+', author='Rat1')
    api.hc.send_print('#0 fr+', author='Rat2')
    assert 'FR(2/2)' in str(case)


def test_failed_calls(api: API):
    case = api.put_case(num='0', cmdr='some client')
    api.hc.send_print('#0 fr+', author='Rat1')
    api.hc.send_print('#0 fr-', author='Rat2')
    assert 'FR' not in str(case)


def test_retracted_calls(api: API):
    case = api.put_case(num='0', cmdr='some client')
    api.hc.send_print('#0 fr+', author='Rat1')
    api.hc.send_print('#0 fr-', author='Rat1')
    assert 'FR' not in str(case)


def test_retracted_lower_level_calls(api: API):
    case = api.put_case(num='0', cmdr='some client')
    case.put_rat('Rat1')
    api.hc.send_print('#0 fr+', author='Rat1')
    api.hc.send_print('#0 wr+', author='Rat1')
    api.hc.send_print('#0 fr-', author='Rat1')
    assert 'WR(1/1)' in str(case)


def test_assign_rats(api: API):
    case = api.put_case(num='0', cmdr='some client')
    api.hc.send_print('!go 0 rat1 rat2')
    assert len(case.get_rats()) == 2


def test_calls_with_assigned_rats(api: API):
    case = api.put_case(num='0', cmdr='some client')
    api.hc.send_print('!go 0 rat1 rat2')
    api.hc.send_print('#0 fr+', author='rat1')
    api.hc.send_print('#0 wr+', author='rat2')
    assert 'WR(1/2)' in str(case)
    api.hc.send_print('#0 wr+', author='rat1')
    assert 'WR(2/2)' in str(case)


@pytest.mark.parametrize('msg,author', (
    ('some text relating #0 case', 'not_rat'),
    ('some text relating #0 case', 'rat1'),
    ('some text relating some case', 'rat2'),
    ('some text relating some_client case', 'not_rat'),
    ('some text relating case 0', 'not_rat'),
))
def test_case_detection(api: API, msg, author):
    case = api.put_case(num='0', cmdr='some client')
    case.put_rat('rat1')
    case.put_rat('rat2')
    api.hc.send_print(msg, author=author)
    assert case.nick in api.hc.prnt.call_args[0][0]
    assert f'#{case.num}' in api.hc.prnt.call_args[0][0]
    assert '\n' in api.hc.prnt.call_args[0][0]
