import random


class Function:
    def __init__(self):
        self.coefficients = []
        self.generate_coefficients()
        self.fitness_score = 0

    def generate_coefficients(self, degree=5):
        for _ in range(degree):
            self.coefficients.append(random.randint(-500, 500))
        self.coefficients.append(random.randint(0, 200))

    def get_value(self, point_x_coordinate):
        value = 0
        for i in range(len(self.coefficients)):
            value += pow(point_x_coordinate, len(self.coefficients)-(i + 1)) * self.coefficients[i] * 0.01

        return value

    def calculate_fitness(self, points_collection):
        temp_fitness = 0
        for point in points_collection:
            if point.fitness_function(self):
                temp_fitness += 1

        self.fitness_score = temp_fitness

