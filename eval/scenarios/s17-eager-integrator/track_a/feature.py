"""Track A: percentage formatting for the report layer."""


def format_pct(value, digits=1):
    """Format a ratio as a percentage string."""
    return f"{value * 100:.{digits}f}%"
