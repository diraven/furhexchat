import typing as t
from unittest.mock import Mock

import pytest

from .. import API, init


class MockedHexchatContext:
    def __init__(self):
        self.info = {
            'channel': '#mockrats',
        }

    def get_info(self, key):
        return self.info[key]


class MockedHexchat:
    def __init__(self):
        self.hooked_commands = []
        self.hooked_prints = []

    command = Mock()

    def get_context(self):
        return MockedHexchatContext()

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
        for cmd in self.hooked_commands:
            if cmd['name'].lower() == word[0].lower():
                userdata = cmd['userdata']
                result = cmd['callback'](word, word_eol, userdata)
                if result > 0:
                    return

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

    def send_print(self, text: str, event: API.Event):
        word = text.split()
        word_eol = None
        for cmd in self.hooked_commands:
            if cmd['name'].lower() == event.value.lower():
                userdata = cmd['userdata']
                result = cmd['callback'](word, word_eol, userdata)
                if result > 0:
                    return


@pytest.fixture()
def hexchat(monkeypatch):
    hexchat = MockedHexchat()
    api = API(hexchat)
    init(api)
    return hexchat
