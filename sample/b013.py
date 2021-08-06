try:
    pass
except (ValueError,):  # tupleである必要はない
    pass


# ------

try:
    pass
except ValueError:
    pass
