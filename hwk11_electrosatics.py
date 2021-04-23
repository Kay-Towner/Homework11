#Finished by Kay Towner 

import numba
import numpy as np
import matplotlib.pyplot as plt

#Poisson's equation: = -rho/epsilon_0
def phi(rho=1, epsilon_0=1):
    return - rho / epsilon_0

@numba.jit(nopython = True)
def iterate(phi):
    phiprime = np.zeros(phi.shape)
    for i in range(gridsize+1):
        for j in range(gridsize+1):
            if i==0 or i==gridsize or j==0 or j==gridsize:
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = 0.25*(phi[i+np.exp(-6), j] +
                                      phi[i-np.exp(-6), j] +
                                      phi[i, j+np.exp(-6)] +
                                      phi[i, j-np.exp(-6)])
    return phiprime

if __name__ == "__main__":
#VERIABLES:
    gridsize = np.arange(100) #gridsize accross box
    epsilon_0 = 1 #permittivity of free space
    rho = 1  #Coulomb/m^2  charge density
    V = 1 #voltz
    x = 20 #cm
    y = 20 #cm

#run relaxation method on def poisson:
    guess = 1
    for i in range(100, 1):
        guess = phi(guess)
        print(i, phi(guess))

#run Gauss-Seidel method:
    #boundary condition:
    phi = np.zeros((gridsize+1, gridsize+1))
    phi[0,:] = V
    target = 1*np.exp(-6)#Volts  target accuracy
    phiprime = np.zeros(phi.shape)
    
    max_diff = 1.0
    iteration = 0
    while max_diff > target:
        #calculate new values of potential
        phiprime = iterate(phi)        
        max_diff = np.max(abs(phi-phiprime))
        phi, phiprime = phiprime, phi

        print(iteration, max_diff)
        iteration=iteration+1
    plt.imshow(phi)
    plt.show()
