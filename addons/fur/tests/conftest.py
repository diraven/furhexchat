import typing as t
from unittest.mock import Mock

import pytest

from .. import API, init


class MockedHexchatContext:
    def __init__(self, server: str, channel: str):
        self.info = {
            'server': server,
            'channel': channel,
        }

    emit_print = Mock()

    def get_info(self, key):
        return self.info[key]


class MockedHexchat:
    def __init__(self):
        self.hooked_commands = []
        self.hooked_prints = []

    @staticmethod
    def nickcmp(n1, n2):
        return n1 == n2

    @staticmethod
    def strip(value):
        return value.strip()

    @staticmethod
    def get_context():
        return MockedHexchatContext('FuelRats', '#fuelrats')

    @staticmethod
    def find_context(server: str = '', channel: str = ''):
        return MockedHexchatContext(server, channel)

    @staticmethod
    def get_info(key):
        return MockedHexchat.get_context().get_info(key)

    # noinspection PyShadowingBuiltins
    def hook_command(
        self,
        name: str,
        callback: t.Callable,
        userdata: t.Any = None,
        priority: int = 0,
        help: str = None,
    ):
        self.hooked_commands.append({
            'name': name,
            'callback': callback,
            'userdata': userdata,
            'priority': priority,
            'help': help,
        })
        self.hooked_commands.sort(key=lambda x: x['priority'], reverse=True)

    def send_command(self, text: str):
        word = text.split()
        word_eol = None
        for handler in self.hooked_commands:
            if handler['name'].lower() == word[0].lower():
                userdata = handler['userdata']
                result = handler['callback'](word, word_eol, userdata)
                if result is not None and result > 0:
                    break

    # noinspection PyShadowingBuiltins
    def hook_print(
        self,
        name: str,
        callback: t.Callable,
        userdata: t.Any = None,
        priority: int = 0,
        help: str = None,
    ):
        self.hooked_prints.append({
            'name': name,
            'callback': callback,
            'userdata': userdata,
            'priority': priority,
            'help': help,
        })
        self.hooked_prints.sort(key=lambda x: x['priority'], reverse=True)

    def send_print(
        self,
        text: str, *,
        author: str = '',
        mode: str = '',
    ):
        word_eol = None
        for handler in self.hooked_prints:
            userdata = handler['userdata']
            result = handler['callback'](
                [author, text, mode], word_eol, userdata,
            )
            if result is not None and result > 0:
                return


@pytest.fixture()
def api():
    hexchat = MockedHexchat()
    hexchat.command = Mock()
    hexchat.prnt = Mock()
    api = API(hexchat)
    init(api)
    return api
