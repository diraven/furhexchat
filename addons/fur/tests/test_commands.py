from .. import API


def test_create_case(api: API):
    api.hc.send_command('fc 5 some_client')
    case = api.get_case(num='5')
    assert case
    assert case.cmdr == 'some_client'
    assert case.nick == 'some_client'
    assert len(api.get_all_cases()) == 1


def test_update_case_client(api: API):
    api.put_case(num='5', cmdr='some_client', nick='some_client')
    api.hc.send_command('fc 5 some_other_client')
    case = api.get_case(num='5')
    assert case.cmdr == 'some_other_client'
    assert case.nick == 'some_other_client'
    assert len(api.get_all_cases()) == 1


def test_set_case_num(api: API):
    api.put_case(cmdr='some_client', nick='some_client')
    api.hc.send_command('fc 5 some_client')
    case = api.get_case(num='5')
    assert case.cmdr == 'some_client'
    assert case.nick == 'some_client'
    assert len(api.get_all_cases()) == 1


def test_delete_case(api: API):
    api.put_case(num='5', cmdr='some_client', nick='some_client')
    api.hc.send_command('fcd 5 some_client')
    assert api.get_case(num='5') is None
    assert len(api.get_all_cases()) == 0


def test_cases_list(api: API):
    api.put_case(num='5', cmdr='some_client', nick='some_client')
    api.hc.send_command('fcc')
    assert api.hc.prnt.called_once()
