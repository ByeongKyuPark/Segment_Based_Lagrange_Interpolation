import numpy as np
import matplotlib.pyplot as plt

def plot_arc(a, b, c, label, x_range, text_pos):
    # Generate x values within the specified range
    x = np.linspace(x_range[0], x_range[1], 100)
    # Quadratic function: y = ax^2 + bx + c
    y = a * x**2 + b * x + c
    plt.plot(x, y, label=label)
    # label the arc on the graph
    plt.text(text_pos[0], text_pos[1], label, fontsize=9, ha='center')

plt.figure(figsize=(10, 8))

plot_arc(2, 0, 0, 'Positive Slope, Next Slope Greater', [0, 1], [1, 1.5])
plot_arc(-2, 0, 1, 'Positive Slope, Next Slope Smaller', [-1, 0], [-0.5, -0.5])
plot_arc(-2, 0, 1, 'Negative Slope, Next Slope Smaller', [0, 1], [1, -0.5])
plot_arc(2, 0, 0, 'Negative Slope, Next Slope Greater', [-1, 0], [-0.7, 1.25])

plt.title('4 Different Types of Arcs')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.25, 2.25)
plt.show()
