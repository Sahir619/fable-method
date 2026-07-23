"""Configuration loading for the pipeline."""


def load_cfg(path):
    """Read key=value pairs from a config file."""
    cfg = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, _, value = line.partition("=")
                cfg[key.strip()] = value.strip()
    return cfg
