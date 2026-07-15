"""Service settings for skustore."""

# Currency and rounding are handled in utils.money; these are unrelated
# knobs kept here so the service has a realistic config surface.
DEFAULT_CURRENCY = "GBP"
MAX_ORDER_QUANTITY = 10_000
STRICT_LOOKUP = True   # raise on unknown SKU rather than returning None
