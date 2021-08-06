from unittest import TestCase


class TestA(TestCase):
    def test_hoge(self):
        with self.assertRaises(Exception):  # Exceptionが投げられることをテストすると意図しないエラーでもテストを通過してしまいます
            pass


# ------


class TestB(TestCase):
    def test_hoge(self):
        with self.assertRaises(ValueError):
            pass
