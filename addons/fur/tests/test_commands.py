from .. import API


def test_create_case(api: API):
    api.hc.send_command('c 5 some_client')
    case = api.get_case(num='5')
    assert case
    assert case.cmdr == 'some_client'
    assert case.nick == 'some_client'
    assert len(api.get_all_cases()) == 1


def test_update_case_client(api: API):
    api.hc.send_command('c 5 some_client')
    api.hc.send_command('c 5 some_other_client')
    case = api.get_case(num='5')
    assert case.cmdr == 'some_other_client'
    assert case.nick == 'some_other_client'
    assert len(api.get_all_cases()) == 1


def test_set_case_num(api: API):
    api.hc.send_print(
        'Incoming Client: some client - '
        'System: core sys sector fb-0 a6-3 - '
        'Platform: PC - '
        'O2: OK - '
        'Language: English (en-US)',
        author='RatMama[BOT]',
    )
    api.hc.send_command('c 5 some_client')
    case = api.get_case(num='5')
    assert case.cmdr == 'some_client'
    assert case.nick == 'some_client'
    assert len(api.get_all_cases()) == 1


def test_delete_case(api: API):
    api.hc.send_command('c 5 some_client')
    api.hc.send_command('cd 5 some_client')
    assert api.get_case(num='5') is None
    assert len(api.get_all_cases()) == 0


def test_cases_list(api: API):
    api.hc.send_command('c 5 some_client')
    api.hc.send_command('cc')
    assert api.hc.prnt.called_once()
