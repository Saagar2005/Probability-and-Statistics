import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import collections as mc

plt.close('all')

# Set Seaborn style
sns.set(style='whitegrid')

def random_endpoints(num_lines, center_x, center_y, radius):

    alpha = 2 * np.pi * np.random.uniform(0, 1, num_lines)
    beta = 2 * np.pi * np.random.uniform(0, 1, num_lines)
    x1 = center_x + radius * np.cos(alpha)
    x2 = center_x + radius * np.cos(beta)
    x0 = (x1 + x2) / 2
    y1 = center_y + radius * np.sin(alpha)
    y2 = center_y + radius * np.sin(beta)
    y0 = (y1 + y2) / 2
    return x1, y1, x2, y2, x0, y0

def random_radius(num_lines, center_x, center_y, radius):

    l = radius * np.random.uniform(0, 1, num_lines)
    m = np.sqrt(radius ** 2 - l ** 2)
    alpha = 2 * np.pi * np.random.uniform(0, 1, num_lines)
    sin_alpha = np.sin(alpha)
    cos_alpha = np.cos(alpha)
    x1 = center_x + l * cos_alpha + m * sin_alpha
    y1 = center_y + l * sin_alpha - m * cos_alpha
    x2 = center_x + l * cos_alpha - m * sin_alpha
    y2 = center_y + l * sin_alpha + m * cos_alpha
    x0 = (x1 + x2) / 2
    y0 = (y1 + y2) / 2
    return x1, y1, x2, y2, x0, y0

def random_midpoint(num_lines, center_x, center_y, radius):

    l = radius * np.sqrt(np.random.uniform(0, 1, num_lines))
    m = np.sqrt(radius ** 2 - l ** 2)
    alpha = 2 * np.pi * np.random.uniform(0, 1, num_lines)
    sin_alpha = np.sin(alpha)
    cos_alpha = np.cos(alpha)
    x1 = center_x + l * cos_alpha + m * sin_alpha
    y1 = center_y + l * sin_alpha - m * cos_alpha
    x2 = center_x + l * cos_alpha - m * sin_alpha
    y2 = center_y + l * sin_alpha + m * cos_alpha
    x0 = (x1 + x2) / 2
    y0 = (y1 + y2) / 2
    return x1, y1, x2, y2, x0, y0

def calculate_prob(x1, y1, x2, y2, radius):
    length = np.hypot(x1 - x2, y1 - y2)
    side_length = radius * np.sqrt(3)
    prob = np.mean(length > side_length)
    return prob

def plot_chords(ax, center_x, center_y, radius, x1, y1, x2, y2, color):
    # Plotting circle
    t = np.linspace(0, 2 * np.pi, 200)
    xp = radius * np.cos(t)
    yp = radius * np.sin(t)
    ax.plot(center_x + xp, center_y + yp, color='k')
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Plotting chords
    chords = [[(x1[i], y1[i]), (x2[i], y2[i])] for i in range(num_chords)]
    lc = mc.LineCollection(chords, colors=color)
    ax.add_collection(lc)

def plot_histogram(ax, length, side_length, color):
    ax.hist(length, bins='auto', color=color, alpha=0.75)
    ax.axvline(x=side_length, color='k', linestyle='--')
    ax.set_xlabel('Chord Length')
    ax.set_ylabel('Frequency')

def plot_midpoints(ax, center_x, center_y, radius, xx0, yy0, color):
    # Plotting circle
    t = np.linspace(0, 2 * np.pi, 200)
    xp = radius * np.cos(t)
    yp = radius * np.sin(t)
    ax.plot(center_x + xp, center_y + yp, color='k')
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Plotting midpoints
    ax.scatter(xx0, yy0, color=color, alpha=0.5)
    ax.set_title(f'Midpoints of Solution Chords')

# Simulation parameters
radius = 1
center_x = 0
center_y = 0
num_chords = int(input("Enter number of chords: "))



# chords obtained by different methods
x1_a, y1_a, x2_a, y2_a, x0_a, y0_a = random_endpoints(num_chords, center_x, center_y, radius)
x1_b, y1_b, x2_b, y2_b, x0_b, y0_b = random_radius(num_chords, center_x, center_y, radius)
x1_c, y1_c, x2_c, y2_c, x0_c, y0_c = random_midpoint(num_chords, center_x, center_y, radius)

# Calculate probabilities
prob_a = calculate_prob(x1_a, y1_a, x2_a, y2_a, radius)
prob_b = calculate_prob(x1_b, y1_b, x2_b, y2_b, radius)
prob_c = calculate_prob(x1_c, y1_c, x2_c, y2_c, radius)

#display the probabilities
print("Probability of chord by random endpoints method is: ", prob_a)
print("Probability of chord by random radius method is: ", prob_b)
print("Probability of chord by random midpoint method is: ", prob_c)

# Plotting
fig, axes = plt.subplots(3, 3, figsize=(20, 20))

# Plot Random Endpoints chords
plot_chords(axes[0, 0], center_x, center_y, radius, x1_a, y1_a, x2_a, y2_a, 'r')
axes[0, 0].set_title(f'Chords of Random Endpoints method(Prob: {prob_a:.4f})')

# Plot Random Radius chords
plot_chords(axes[1, 0], center_x, center_y, radius, x1_b, y1_b, x2_b, y2_b, 'g')
axes[1, 0].set_title(f'Chords of Random Radius method(Prob: {prob_b:.4f})')

# Plot Random Midpoint chords
plot_chords(axes[2, 0], center_x, center_y, radius, x1_c, y1_c, x2_c, y2_c, 'b')
axes[2, 0].set_title(f'Chords of Random Midpoint method (Prob: {prob_c:.4f})')

# Plot histograms (dotted line at x = side length is for reference)
plot_histogram(axes[0, 1], np.hypot(x1_a - x2_a, y1_a - y2_a), radius * np.sqrt(3), 'r')
plot_histogram(axes[1, 1], np.hypot(x1_b - x2_b, y1_b - y2_b), radius * np.sqrt(3), 'g')
plot_histogram(axes[2, 1], np.hypot(x1_c - x2_c, y1_c - y2_c), radius * np.sqrt(3), 'b')

# Plot midpoints
plot_midpoints(axes[0, 2], center_x, center_y, radius, x0_a, y0_a, 'r')
plot_midpoints(axes[1, 2], center_x, center_y, radius, x0_b, y0_b, 'g')
plot_midpoints(axes[2, 2], center_x, center_y, radius, x0_c, y0_c, 'b')

# Add a gap between the subplots
plt.subplots_adjust(hspace=0.6)
# Display the plots
plt.show()
