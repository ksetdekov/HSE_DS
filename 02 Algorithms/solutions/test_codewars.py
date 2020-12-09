def maskify(cc):
    """return masked string"""
    le = len(cc)
    if le < 5:
        return cc
    else:
        return "#" * (le - 4) + cc[le - 4:]
