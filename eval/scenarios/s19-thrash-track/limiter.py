"""Track C: request rate limiter."""
import json

RATE_LIMIT = 100


def allow(count):
    return count < RATE_LIMIT


def config_version():
    with open("config_lock.json") as f:
        return json.load(f)["version"]
