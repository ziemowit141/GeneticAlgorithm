import random


class PositivePoint:
    def __init__(self):
        self.random_coordinates()

    def fitness_function(self, function):
        return self.y >= function.get_value(self.x)

    def random_coordinates(self):
        self.x = random.randint(0, 300)
        self.y = random.randint(200, 500)


class NegativePoint:
    def __init__(self):
        self.random_coordinates()

    def fitness_function(self, function):
        return self.y < function.get_value(self.x)

    def random_coordinates(self):
        self.x = random.randint(200, 500)
        self.y = random.randint(0, 300)


def get_x(points):
    x_list = []
    for point in points:
        x_list.append(point.x)

    return x_list


def get_y(points):
    y_list = []
    for point in points:
        y_list.append(point.y)

    return y_list

