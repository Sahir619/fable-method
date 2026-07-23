from config import load_cfg


def run_nightly(config_path):
    cfg = load_cfg(config_path)
    return [name for name in cfg if name.startswith("task_")]
