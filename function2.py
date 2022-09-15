#设置类的多态
class shape:
    def _init_(self, name):
        self.name = name

    def area(self):
        pass


class Square(Shape):
    def _init_(self, length):
        super()._init_("正方形")
        self.length = length

    def area(self):
        return self.length * self.length


class Circle(Shape):
    def _init_(self, radius):
        super()._init_("圆形")
        self.length = length

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def _init_(self, base, height):
        super()._init_("三角形")
        self.base = base
        self.length = length

    def area(self):
        return self.base * self.length / 2


s = Square(5)
c = Circle(6)
t = Triangle(3, 4)
s.name

c.name

s.area()

c.area()

t.area()

