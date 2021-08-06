getattr("a", "upper")  # getattrを使わず直接呼び出す


# ------

"a".upper()


getattr("a", "upper", None)  # 存在しない場合の返り値を設定しておくと警告されない

hoge = "upper"
getattr("a", hoge)  # 動的に使うケースは警告されない
