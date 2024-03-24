# MAT357 Proj-2 : interpolation byeonggyu.park

import numpy as np
import matplotlib.pyplot as plt

def classify_and_propagate(x, y):
    # calc slopes for each edge
    slopes = np.diff(y) / np.diff(x)
    # calc forward differences to identify trend shifts
    slope_changes = np.diff(slopes)
    # (0). initial classification based on slope direction
    classifications = np.sign(slope_changes)
    # (1). propagate classifications to handle zeros (overwrite '0' classifications with those of the left seg.)
    for i in range(1, len(classifications)):
        if classifications[i] == 0:
            classifications[i] = classifications[i - 1]
    return classifications

""" returns polynomial function """
def lagrange_interpolation(x, y):
    """ computes lagrange interpolating polynomial function"""
     # (closure function) 
     # the inner function below has access to the local variables of the enclosing (outer) one
     # even after the outer function has finished execution. 
    def interpolating_polynomial(x_val):
        total = 0
        n = len(x)
        for i in range(n):
            xi, yi = x[i], y[i]
            term = yi
            for j in range(n):
                if i != j:
                    term *= (x_val - x[j]) / (xi - x[j])
            total += term
        return total
    return interpolating_polynomial

def fit_and_plot(x, y, classifications):
    plt.figure(figsize=(8, 6))
  
    start_idx = 0
    
    for i in range(len(classifications) - 1):
        # check if at the end of a segment
        if classifications[i] != classifications[i + 1]:
            end_idx = i + 2  # include next point in segment (not +1, but +2 as 'end' range is exclusive. see codes below)

            # extract segment points
            segment_x = x[start_idx:end_idx] #[inclusive,exclusive)
            segment_y = y[start_idx:end_idx] #[inclusive,exclusive)

            # apply lagrange interpolation
            lagrange_poly = lagrange_interpolation(segment_x, segment_y)
            x_fit = np.linspace(segment_x[0], segment_x[-1], 100)
            y_fit = [lagrange_poly(xi) for xi in x_fit]

            # plot fitted seg
            plt.plot(x_fit, y_fit, 'r-')
            start_idx = i + 1  # update start for next segment, note [i+1] is the closest idx with different classification
    
    # handle the last edge manullay here
    if start_idx < len(x):  # lex(x) <- number of data points
        segment_x = x[start_idx:n]
        segment_y = y[start_idx:n]
        lagrange_poly = lagrange_interpolation(segment_x, segment_y)
        x_fit = np.linspace(segment_x[0], segment_x[-1], 100)
        y_fit = [lagrange_poly(xi) for xi in x_fit]
        plt.plot(x_fit, y_fit, 'r-')
    
    plt.plot(x, y, 'bo')  # plot the given original data points
    plt.title('Slope-guided Segmentation with Lagrange Polynomial Approximation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# given datasets
datasets = [
    (np.array([0, 2, 3, 5, 6, 9]), np.array([2, 1, 0, 1, 2, 0])),
    (np.array([0, 1, 2, 4, 5, 6]), np.array([0, 1, 2, 4, 3, 1])),
    (np.array([0, 1, 2, 4, 5, 9, 10]), np.array([2, 1, 2, 5, 6, 5, 5])),
    (np.array([0, 1, 2, 3, 4, 5, 6, 7]), np.array([0, 0, 0, 0, 2, 0, 0, 0])),
    (np.array([0, 1, 2, 4, 6, 7, 9, 10]), np.array([5, 2, 1, 0, 1, 3, 4, 2]))
]

# plot each dataset
for x_list, y_list in datasets:
    classifications = classify_and_propagate(x_list, y_list)
    fit_and_plot(x_list, y_list, classifications)
