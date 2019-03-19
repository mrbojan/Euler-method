import numpy as np
import matplotlib.pyplot as plt

#function that we differentiate
def func(t, y):
    x = y[0]
    xdot = y[1]
    return np.array([xdot, -x])

class Euler:

    def __init__(self, func, x0, time_zero, time_end, step):
        self.func = func    #function
        self.x0 = x0        #function zero place
        self.time_zero = time_zero      #start differentiate
        self.time_end = time_end        #stop differentiate
        self.step = step
        self.time = np.arange(self.time_zero, self.time_end, self.step)     #list with time from time_zero to time_end with step
        self.length_time = len(self.time)
        self.x_matrix = np.zeros((self.length_time, len(self.x0)))          #for a vector equation x_matrix = np.zeros(N)
        self.x_matrix[0] = np.array(self.x0)
        self.iter = 1

    #method of start symulation
    def start_symulation(self):
        while(self.iter < self.length_time):
            self.x_matrix[self.iter]= np.array(self.x_matrix[self.iter - 1] + self.step
                                               * self.func(self.time[self.iter - 1],
                                                           self.x_matrix[self.iter - 1]))   #equation Euler
            self.iter += 1
        return self.time, self.x_matrix     #return our time and euler solution

    #method
    def show_plots(self):
        plt.subplot(211)     #first plot with time to solution xdot and ydot
        plt.plot(self.time, self.x_matrix[:,0])
        plt.plot(self.time, self.x_matrix[:,1])
        plt.subplot(212)       #second plot with solution xdot to ydot
        plt.plot(self.x_matrix[:,0], self.x_matrix[:,1])
        return plt.show()

#values
x0 = [1.0, 1.0]
time_zero = .0
time_end = 30.0
step = 0.01
#use of the Euler class
euler = Euler(func, x0, time_zero, time_end, step)
time, x_matrix = euler.start_symulation()
euler.show_plots()
