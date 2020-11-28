from .. import API


def test_all(api: API):
    api.put_case(num='1', cmdr='some_client1', nick='some_client1')
    api.put_case(num='2', cmdr='some_client2', nick='some_client2')
    api.hc.send_print('some info on case #1')
    api.hc.send_print('some info on case #2')
    assert api.hc.prnt.call_count == 2


def test_odd(api: API):
    api.set_mode(api.Mode.odd)
    api.put_case(num='1', cmdr='some_client1', nick='some_client1')
    api.put_case(num='2', cmdr='some_client2', nick='some_client2')
    api.hc.send_print('some info on case #1')
    api.hc.send_print('some info on case #2')


def test_even(api: API):
    api.set_mode(api.Mode.even)
    api.put_case(num='1', cmdr='some_client1', nick='some_client1')
    api.put_case(num='2', cmdr='some_client2', nick='some_client2')
    api.hc.send_print('some info on case #1')
    api.hc.send_print('some info on case #2')
    assert '#2' in api.hc.prnt.call_args[0][0]


def test_unknown(api: API):
    api.set_mode(api.Mode.even)
    api.put_case(num='1', cmdr='some_client1', nick='some_client1')
    api.put_case(num='2', cmdr='some_client2', nick='some_client2')
    api.hc.send_print('some info on unknown case #123')
    assert '#123' in api.hc.prnt.call_args[0][0]
