# imports
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# plotting
plt.rcParams["figure.figsize"] = 48,32
fig, ax = plt.subplots(dpi=500)
ax.axis([-15,15,-15,15])
ax.set_aspect("equal")
ax.set_facecolor('xkcd:black')

ax.tick_params(axis='x', bottom=False, labelbottom=False)
ax.tick_params(axis='y', left=False, labelleft=False)



#point, = ax.plot(0,0, marker="o", color="lime", markersize=10)
trail_length = 100
trail, = ax.plot(0, 0, 'r', alpha=1, linewidth = 0, color="lime", marker = "o", markersize=0.5)

x_trail = []
y_trail = []

# point
def init():
    #point.set_data([], [])
    trail.set_data([], [])
    return trail, point,

# function
def func(x):
    return x

# update animation
def update(phi):

    #start = max(0, phi - trail_length)

    x = 12 * np.sin(2* phi + phi)
    y = 7 * np.sin(16 * phi)
    #point.set_data([x],[y])

    x_trail.append(x)
    y_trail.append(y)

    if len(x_trail) > trail_length:
        x_trail.pop(0)
        y_trail.pop(0)
    trail.set_data(x_trail, y_trail)

    return trail,

# animation
ani = FuncAnimation(fig, update, interval=30, blit=True, repeat=True,
                    frames=np.linspace(0, 3*np.pi, 360*4, endpoint=True))

# plotting
plt.show()