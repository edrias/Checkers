class foo:
    def __init__(self):
        self.look = "b "

    def __str__(self):
        return self.look

    def change_b(self):
        self.look = "bk "


x = foo()
print(x)
x.change_b()
print(x)

