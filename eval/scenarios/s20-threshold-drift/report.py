def render(rows):
    if len(rows) > 1000:
        print(f"WARN: large report, {len(rows)} rows")
    return "ok"
