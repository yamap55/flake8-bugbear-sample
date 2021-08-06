try:
    pass
except (Exception, ValueError):  # ValueErrorはExceptionの子クラスなので冗長
    pass

# ------

try:
    pass
except Exception:
    pass
