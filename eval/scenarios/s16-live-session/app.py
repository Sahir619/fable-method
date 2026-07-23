from config import load_cfg


def start(config_path):
    cfg = load_cfg(config_path)
    return f"app started with {len(cfg)} settings"
