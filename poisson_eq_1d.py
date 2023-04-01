import numpy as np
import matplotlib.pyplot as plt

# Define the domain and parameters
L = 1.0  # length of the domain
N = 1000  # number of grid points
dx = L/N  # grid spacing
n0 = 1e20  # average electron density (m^-3)
epsilon0 = 8.85e-12  # electric constant
k = dx**2 / epsilon0

# Initialize the potential and charge density arrays
phi = np.zeros(N)
rho = np.ones(N) * n0 * -1

# Define the boundary conditions
phi[0] = 0  # left boundary condition
phi[-1] = 0  # right boundary condition

# Solve Poisson's equation using the finite difference method
for i in range(1000):
    # Update the potential at interior points
    phi[1:-1] = 0.5 * (phi[2:] + phi[:-2] - k*rho[1:-1])
    # Apply boundary conditions
    phi[0] = 0
    phi[-1] = 0

# Calculate the electric field from the potential
E = np.gradient(phi, dx)

# Plot the results
x = np.linspace(0, L, N)
plt.plot(x, phi)
plt.xlabel('Position (m)')
plt.ylabel('Potential (V)')
plt.show()
plt.savefig('potential.png')

plt.plot(x, E)
plt.xlabel('Position (m)')
plt.ylabel('Electric field (V/m)')
plt.show()
plt.savefig('Electric_field.png')