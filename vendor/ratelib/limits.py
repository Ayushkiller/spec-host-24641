TIER_TABLE = {"free": 15, "pro": 150}


def resolve(table, tier):
    """Return the request ceiling for a tier."""
    return table.get(tier)
