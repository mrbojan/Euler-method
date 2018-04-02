import numpy as np
import matplotlib.pyplot as plt
def EE(f,x0,t0,tk,h):
    t=np.arange(t0,tk,h)
    N=len(t)
    x=np.zeros((N,len(x0)))  #dla rownania wektorowego #x=np.zeros(N)
    x[0]=np.array(x0)
    i=1
    while(i<N):
        x[i]=np.array(x[i-1]+h*f(t[i-1],x[i-1]))
        i+=1
    return t,x

def funcion(t,y):
    xx=y[0]
    yy=y[1]
    xdot=
    ydot=
    return np.array([xdot,ydot])

t,x=EE(funcion,[1.0,1.0],0.0,30,0.01)
plt.figure(1)
plt.plot(t,x[:,0])
plt.plot(t,x[:,1])
plt.figure(2)
plt.plot(x[:,0],x[:,1])
plt.show()