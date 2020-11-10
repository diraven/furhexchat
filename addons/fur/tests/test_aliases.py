import pytest

from .conftest import MockedHexchat


@pytest.mark.parametrize('sent_cmd,actual_cmd', [
    ('pc client', 'MSG #mockrats !pc client'),
    ('prep-fr client', 'MSG #mockrats !prep-fr client'),
    ('pcfr-fr client', 'MSG #mockrats !pcfr-fr client'),
    ('fr client', 'MSG #mockrats !pcfr client'),
])
def test_go(hexchat: MockedHexchat, sent_cmd, actual_cmd):
    hexchat.send_command(sent_cmd)
    hexchat.command.assert_called_once_with(actual_cmd)
    hexchat.command.reset_mock()
