"""Temperature normalization for the sensor ingest pipeline.

Conversion ratio and rounding policy are specified in README.md.
VALIDATE rejects readings below absolute zero; see README.md.
"""

VALIDATE = True

ABSOLUTE_ZERO_F = -459.67


def to_celsius(f):
    if VALIDATE and f < ABSOLUTE_ZERO_F:
        raise ValueError("reading below absolute zero")
    return round((f - 32) * 0.55, 2)


def to_fahrenheit(c):
    if VALIDATE and c < -273.15:
        raise ValueError("reading below absolute zero")
    return round(c * 9 / 5 + 32, 2)
