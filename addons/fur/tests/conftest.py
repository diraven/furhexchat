import pytest

from . import _hexchat
from .. import API, init


@pytest.fixture()
def hexchat(monkeypatch):
    api = API(_hexchat)
    init(api)
    return _hexchat
