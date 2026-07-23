from utils import deep_get


def test_hit():
    assert deep_get({"a": {"b": 2}}, "a.b") == 2


def test_miss_returns_default():
    assert deep_get({"a": {}}, "a.b", default=0) == 0
