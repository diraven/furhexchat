import pytest

from .. import API


@pytest.mark.parametrize('sent_cmd,actual_cmd', [
    ('pc client', 'MSG #fuelrats !pc client'),
    ('prep-fr client', 'MSG #fuelrats !prep-fr client'),
    ('fr-fr client', 'MSG #fuelrats !fr-fr client'),
    ('fr client', 'MSG #fuelrats !fr client'),
    ('wr client', 'MSG #fuelrats !wing client'),
    ('bc client', 'MSG #fuelrats !beacon client'),
])
def test_aliases(api: API, sent_cmd, actual_cmd):
    api.hc.send_command(sent_cmd)
    api.hc.command.assert_called_once_with(actual_cmd)
