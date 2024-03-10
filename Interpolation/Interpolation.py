import numpy as np
import matplotlib.pyplot as plt

def plot_arc(x1, y1, x2, y2, curvature):
    # blend from start to end point and apply curvature to simulate an arc
    t = np.linspace(0, 1, num=100)
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2 + curvature * np.sin(np.pi * t)  # sine wave adds the arc
    plt.plot(x, y, 'r-')

def process_and_plot(x_list, y_list):
    slopes = np.diff(y_list) / np.diff(x_list)  # calculate slopes between points
    curvatures = np.zeros(len(x_list) - 1)  # prepare for curvature values

    # decide curvature based on slope comparison
    for i in range(len(curvatures) - 1):
        curvatures[i] = -0.5 if slopes[i] < 0 and (i == len(slopes) - 1 or slopes[i] < slopes[i+1]) else 0.5
    curvatures[-1] = curvatures[-2]  # reuses the last curvature for smoothness

    plt.figure(figsize=(8, 6))
    for i in range(len(x_list) - 1):
        plot_arc(x_list[i], y_list[i], x_list[i+1], y_list[i+1], curvatures[i])
    plt.plot(x_list, y_list, 'bo')  # plot data points

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Piecewise Arcs with Sine Curvature')
    plt.show()

# datasets to visualize
datasets = [
    (np.array([0, 2, 3, 5, 6, 9]), np.array([2, 1, 0, 1, 2, 0])),
    (np.array([0, 1, 2, 4, 5, 6]), np.array([0, 1, 2, 4, 3, 1])),
    (np.array([0, 1, 2, 4, 5, 9, 10]), np.array([2, 1, 2, 5, 6, 5, 5])),
    (np.array([0, 1, 2, 3, 4, 5, 6, 7]), np.array([0, 0, 0, 0, 2, 0, 0, 0])),
    (np.array([0, 1, 2, 4, 6, 7, 9, 10]), np.array([5, 2, 1, 0, 1, 3, 4, 2]))
]

for x_list, y_list in datasets:
    process_and_plot(x_list, y_list)
