import numpy as np
import matplotlib.pyplot as plt

#This is a basic ODE solver, except the ODE in question
#is the driven damped pendulum equation which is an
#ODE that's nonlinear enough to demonstrate chaotic 
#properties such as extreme sensitivity to intial
#conditions

#Here we set a the parameters
w = 2*np.pi
w0 = 1.5*w
b = w0/4
d = 1.503
x0 = [0,0.001] #Here's our two intial conditions, notice how close they are
v0 = 0
dt = 1E-4
x = x0
v = v0

#Then we solve the ODE for two initial conditions
for i in x0:
    x = i
    v = v0
    xT = []
    tT = []
    t = 0
    while t < 25:
        xT.append(x)
        tT.append(t)
    
        t = t + dt
        a = d*w0**2*np.cos(w*t) - w0**2*np.sin(x) - 2*b*v
        v = v + a*dt
        dx = v*dt + 0.5*a*dt**2
        x = x + dx

    plt.plot(tT,xT, label = "$\\theta(0) =${}".format(i))

#Then the prettiness
plt.xlabel("Time, $t$, (s)")
plt.ylabel("Angular displacement, $\\theta$, (rad)")
plt.title("The driven damped pendulum with two different initial conditions", fontsize = 12)
plt.legend(loc = "best")
plt.show()
 
