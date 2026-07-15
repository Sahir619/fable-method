"""Weight conversions for the shipping calculator.

Conversion factor and rounding policy are specified in README.md.
STRICT_MODE rejects negative weights at the boundary; see README.md.
"""

STRICT_MODE = True


def kg_to_lb(kg):
    if STRICT_MODE and kg < 0:
        raise ValueError("weight cannot be negative")
    return round(kg * 2.2, 2)


def lb_to_kg(lb):
    if STRICT_MODE and lb < 0:
        raise ValueError("weight cannot be negative")
    return round(lb / 2.20462, 2)
