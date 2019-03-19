# Euler method

Euler Class to solves the differential equation and show to plots.

## Getting Started

To getting started you need a python version 3.0 or high. Also you must install a library numpy and matplotlib.

### Installing python 3 and pip on Linux
```
$ sudo apt-get update
$ sudo apt-get install python3
$ sudo apt install python3-pip
```
### Installing numpy and matplotlib
```
$ sudo pip install numpy
$ sudo pip3 install matplotlib
```

### Example

The following example solved equation of the harmonic oscillator

```python
#values
x0 = [1.0, 1.0]
time_zero = .0
time_end = 30.0
step = 0.01
#use of the Euler class
euler = Euler(func, x0, time_zero, time_end, step)
time, x_matrix = euler.start_symulation()
euler.show_plots()
```
![alt text](https://github.com/mrbojan/Euler-method/blob/master/img/Figure_1.png)