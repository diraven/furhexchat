from .conftest import MockedHexchat


def test_go(hexchat: MockedHexchat):
    hexchat.send_command('pc test')

    hexchat.command.assert_called_once_with('MSG #mockrats !pc test')
