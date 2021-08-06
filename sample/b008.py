def hoge(a=list()):  # デフォルト引数で関数の実行を行わない
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
