from Point import PositivePoint, NegativePoint, get_x, get_y
import matplotlib.pyplot as plt
from Function import Function
from DriverCode import algorithm, NUMBER_OF_POINTS
import numpy as np


def generate_points():
    points_list = []
    positive_points_list = []
    negative_points_list = []
    for _ in range(0, int(NUMBER_OF_POINTS/2)):
        positive_point = PositivePoint()

        for point in points_list:
            if point.x == positive_point.x and point.y == positive_point.y:
                while point.x == positive_point.x and point.y == positive_point.y:
                    positive_point.random_coordinates()

        points_list.append(positive_point)
        positive_points_list.append(positive_point)

    for _ in range(0, int(NUMBER_OF_POINTS/2)):
        negative_point = NegativePoint()

        for point in points_list:
            if point.x == negative_point.x and point.y == negative_point.y:
                while point.x == negative_point.x and point.y == negative_point.y:
                    negative_point.random_coordinates()

        points_list.append(negative_point)
        negative_points_list.append(negative_point)

    return points_list, positive_points_list, negative_points_list


function_population = []

for _ in range(100):
    function_population.append(Function())

points_list, positive_points_list, negative_points_list = generate_points()

positive_x_coordinates = get_x(positive_points_list)
positive_y_coordinates = get_y(positive_points_list)

negative_x_coordinates = get_x(negative_points_list)
negative_y_coordinates = get_y(negative_points_list)

# plt.plot(positive_x_coordinates, positive_y_coordinates, 'go')
# plt.plot(negative_x_coordinates, negative_y_coordinates, 'ro')
# plt.axis([0, 500, 0, 500])
# plt.show()

best, fitness_list = algorithm(function_population, points_list)
y_pos = np.arange(len(fitness_list))
plt.bar(y_pos, fitness_list)
print(fitness_list)
print(len(fitness_list))
plt.show()

# def plot_function(function):
#     y = []
#     for i in range(500):
#         y.append(function.get_value(i))
#     plt.plot(y, 'b-')
#
#
# plot_function(best)
# print("Winner: " + str(best.coefficients) + " Fitness score: "
#       + str(best.fitness_score) + " Generation nr.: " + str(generation))
#
# plt.plot(positive_x_coordinates, positive_y_coordinates, 'go')
# plt.plot(negative_x_coordinates, negative_y_coordinates, 'ro')
# plt.axis([0, 500, 0, 500])
# plt.show()
