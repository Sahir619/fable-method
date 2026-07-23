from limiter import allow, config_version


def test_allow_under_limit():
    assert allow(50)


def test_deny_over_limit():
    assert not allow(150)


def test_config_schema_current():
    # Wave 10 requires config schema version 7 (see WAVE-NOTES.md)
    assert config_version() == 7
