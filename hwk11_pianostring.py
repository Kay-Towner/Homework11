#Finished by Kay Towner // animation code: Jake Vanderplas
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import math

def dphi_dt(x=None, t=None):
    return psi(x, t)
def dpsi_dt(x=None, t=None, v=None, a=None):
    return (v**2/a**2)*[dphi_dt(x+a,t) + dphi_dt(x-a,t)-2*dphi_dt(x,t)]

def psi(x=None, L=None, C=None, sigma=None):
    psi_x = C*(x*(L-x)/L**2) * np.exp(-((x-d**2)/2* sigma**2))
    return psi_x
def phi(x=None, L=None, C=None, sigma=None):
    phi_x = (C*(x*(L-x)/L**2) * np.exp(-((x-d**2)/2* sigma**2)))*h
    return phi_x

if __name__ == "__main__":
#VERIABLES:
    L = 1 #m  length
    C = 1 #ms-1
    d = 10 #cm  distance from the end of string
    h = 1*np.exp(-6) #s seconds timestep
    v = 100 #ms-1
    sigma = 0.3 #m
    phi_x = 0 #initial condition
    a = 0.01  #grid spacing
    
    t = 0 #sec  time the string is struc
    tmax = 1 #sec  longest time
    
    x = np.arange(0, L+a, a)
    y = np.zeros(x.shape)#hight position to find
    newy = y.copy()
    
#FTCS Algorithm
    iteration = 0
    while t < tmax:
        for i in range(len(y)):
            iteration += 1
            newy[i] = y[i]+(v**2/a**2)*(psi(x[i]+a, L, C, sigma)+ psi(x[a]-a, L, C, sigma)
                                        -2*psi(x[t], L, C, sigma))
            t += h
    print("The Iterations are:", iteration)


#--------------------------------------------------------------------
#animation:
    fig = plt.figure(iteration)
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], lw=2)
# initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,
# animation function.  This is called sequentially
    def animate(i):
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        line.set_data(x, y)
        return line,
# call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

    anim.save('Homework11ANIMATION.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
