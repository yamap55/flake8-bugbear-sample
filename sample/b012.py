def a():
    try:
        return "a"
    finally:
        return "b"  # finally句の中でreturnは行わない


assert a() == "b"
