"""Track B: safe dictionary access for the report layer."""


def deep_get(d, path, default=None):
    """Fetch a nested key like 'a.b.c' from dict d."""
    cur = d
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return cur
