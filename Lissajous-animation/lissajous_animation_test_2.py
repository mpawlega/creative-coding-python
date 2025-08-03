
# imports
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class AnimationParameters:

    def __init__(self, interval, frames, trail_length, color, marker, marker_size, line_width, x_parametric, y_parametric):
        self.interval = interval
        self.frames = frames
        self.trail_length = trail_length
        self.color = color
        self.marker = marker
        self.marker_size = marker_size
        self.line_width = line_width
        self.x_parametric = x_parametric
        self.y_parametric = y_parametric


    def set_parameters(self, interval2, frames2, trail_length2, color2, marker2, marker_size2, line_width2, x_parametric2, y_parametric2):
        self.interval = interval2
        self.frames = frames2
        self.trail_length = trail_length2
        self.color = color2
        self.marker = marker2
        self.markersize = marker_size2
        self.linewidth = line_width2
        self.x_parametric = x_parametric2
        self.y_parametric = y_parametric2

    def get_parameters(self):
        return [self.interval, self.frames, self.trail_length, self.color, self.marker,
        self.marker_size, self.line_width, self.x_parametric, self.y_parametric]
    


class AnimationPlotter:
    def __init__(self, animation_parameter_object):
        self.animation_parameter_object = animation_parameter_object
        self.x_trail = []
        self.y_trail = []
        self.fig = None
        self.ax = None
        #self.trail, =  None

    def plot(self):
        self.fig, self.ax = plt.subplots(dpi=500)
        self.ax.axis([-15,15,-15,15])
        self.ax.set_aspect("equal")
        self.ax.set_facecolor('xkcd:black')
        self.ax.tick_params(axis='x', bottom=False, labelbottom=False)
        self.ax.tick_params(axis='y', left=False, labelleft=False)
        self.trail, = self.ax.plot(0, 0, alpha=1, linewidth = self.animation_parameter_object[6], color = self.animation_parameter_object[3], marker = self.animation_parameter_object[4], markersize = self.animation_parameter_object[5]) 
    
    def update_trail(self, phi): 
        x_func = self.animation_parameter_object[7]
        y_func = self.animation_parameter_object[8]
        x = x_func(phi)
        y = y_func(phi)

        self.x_trail.append(x) 
        self.y_trail.append(y)

        if len(self.x_trail) > self.animation_parameter_object[2]:
            self.x_trail.pop(0)
            self.y_trail.pop(0)

        self.trail.set_data(self.x_trail, self.y_trail)
        return self.trail, 

    def animation(self): 
        ani = FuncAnimation(self.fig, self.update_trail, interval=self.animation_parameter_object[0], blit=True, repeat=True,
                    frames=self.animation_parameter_object[1])
        plt.show()


# Class calls

def x_parametric(phi):
    return 12 * np.sin(2* phi + phi)

def y_parametric(phi):
    return 7 * np.sin(16 * phi)

parameter_object = AnimationParameters(30, np.linspace(0, 3*np.pi, 360*4), 100, "lime", "o", 0.5, 0, x_parametric, y_parametric)
retrieve_parameter_object = parameter_object.get_parameters() 

plot_object = AnimationPlotter(retrieve_parameter_object)
plot_object_initialize = plot_object.plot()
plot_object_animate = plot_object.animation()