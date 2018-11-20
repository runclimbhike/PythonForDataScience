import matplotlib.pyplot as plt


class Circle(object):
    def __init__(self, radius, color):  # __init_ is a constructor
        self.radius = radius
        self.color = color

    def grow_circle(self, new_radius):
        self.radius = self.radius + new_radius
        return self.radius

    def change_color(self, new_color):
        self.color = new_color
        return self.color

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


# instantiating an instance of the class named RedCircle
RedCircle = Circle(10, "red")

# changing an attribute
RedCircle.change_color("blue")

RedCircle.grow_circle(20)

# Test units
# print(RedCircle.radius)
# print(RedCircle.color)

RedCircle.drawCircle()
