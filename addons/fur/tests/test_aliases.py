import pytest

from .. import API


@pytest.mark.parametrize('sent_cmd,actual_cmd', [
    ('pc client', 'MSG #fuelrats !pc client'),
    ('prep-fr client', 'MSG #fuelrats !prep-fr client'),
    ('pcfr-fr client', 'MSG #fuelrats !pcfr-fr client'),
    ('fr client', 'MSG #fuelrats !pcfr client'),
])
def test_go(api: API, sent_cmd, actual_cmd):
    api.hc.send_command(sent_cmd)
    api.hc.command.assert_called_once_with(actual_cmd)
