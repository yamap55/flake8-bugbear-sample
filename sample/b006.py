def hoge(a=[]):  # デフォルト引数に可変のオブジェクトを設定しない
    a.append(1)
    return a


assert hoge() == [1]
assert hoge() == [1, 1]

# ------


def hoge2(a=None):
    a = [] if a is None else a
    a.append(1)
    return a


assert hoge2() == [1]
assert hoge2() == [1]
