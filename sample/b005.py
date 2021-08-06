s = "a"
ss = s.strip(".facebook.com")  # strip系の関数に複数文字列を使用しない
assert ss == ""

# ------

s.replace(".facebook.com", "")
