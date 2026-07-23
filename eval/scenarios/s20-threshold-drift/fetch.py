from logger import warn


def fetch(url, timeout):
    if timeout > 60:
        print(f"WARN: long timeout {timeout}s for {url}")
    return f"fetched {url}"
