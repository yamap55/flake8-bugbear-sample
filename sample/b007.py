_list = (
    ("1", "a"),
    ("2", "b"),
)

for i, s in _list:  # 使用しない変数は「_」と定義する
    print(s)

# ------

_list = (
    ("1", "a"),
    ("2", "b"),
)

for _, s in _list:
    print(s)
