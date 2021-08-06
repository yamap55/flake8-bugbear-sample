class A:
    s = ""

    def p(self):
        print(self.s)


# ------

a = A()
setattr(a, "s", None)

# ------

aa = A()
aa.s = "hoge"

setattr(aa, "except", None)
setattr(aa, "123abc", None)
