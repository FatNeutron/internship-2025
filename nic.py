# heat source
import numpy as np
from scipy.optimize import fsolve
import scipy.optimize as optimize
from tqdm import tqdm
import matplotlib.pyplot as plt


# Constants
R = 270000  # Radius in meters
rho = 3500  # Density (kg/m^3)
yearins = 365.25 * 24 * 3600
mass = 4 / 3 * np.pi * R**3 * rho  # Mass in kg, for Vesta's radius and density
v = 4 / 3 * np.pi * R**3

# Aluminum and iron data
molar_mass_Al = 0.027  # kg/mol for aluminum
avogadro_number = 6.022e23  # atoms/mol
ratio_26Al_27Al = 5e-5  # Initial 26Al/27Al ratio
aluminum_content_mass_fraction = 0.0113  # Total aluminum content by mass
rho_Al = aluminum_content_mass_fraction * rho  # kg/m^3
N_27Al = (rho_Al / molar_mass_Al) * avogadro_number  # atoms/m^3
A0_26Al = ratio_26Al_27Al * N_27Al

molar_mass_Fe = 0.056  # kg/mol
ratio_60Fe_56Fe = 1e-8  # Initial 26Al/27Al ratio
Fe_content_mass_fraction = 0.24  # Total Fe content by mass
rho_Fe = Fe_content_mass_fraction * rho  # kg/m^3
N_Fe = (rho_Fe / molar_mass_Fe) * avogadro_number  # atoms/m^3
A0_60Fe = ratio_60Fe_56Fe * N_Fe

# Half-lives and decay constants
half_life_Al = 0.72e6
half_life_Fe = 1.5e6
lambda_Al = np.log(2) / half_life_Al
lambda_Fe = np.log(2) / half_life_Fe

# Decay energies in joules per atom
E_decay_Al = 3 * 1.60218e-13
E_decay_Fe = 3 * 1.60218e-13
t0 = 2.85e6  # Initial time offset in years

# Function for radiogenic heat production
def QAl(t):
    Q_Al = A0_26Al * E_decay_Al * np.exp(-lambda_Al * (t + t0))
    return Q_Al 




def QFe(t):
    Q_Fe = A0_60Fe * E_decay_Fe * np.exp(-lambda_Fe * (t + t0))
    return Q_Fe



# Material properties for Iron
k_Fe = 80             # Thermal conductivity of Iron (W/m·K)
c_Fe = 450            # Specific heat capacity of Iron (J/kg·K)


# Material properties for Silicates (Quartz)
k_SiO2 = 1.4          # Thermal conductivity of Silicates (W/m·K)
c_SiO2 = 740          # Specific heat capacity of Silicates (J/kg·K)


#initially the temperature is 290K
# Radial and time grids

Nr = 10000  # Number of radial nodes
Nt = 25000  # Number of time steps
t_f = 1.75e6  # Final time (seconds)
t = np.linspace(0, t_f, Nt)
dt = t_f / (Nt - 1)
r = np.linspace(0, R, Nr)
dr = R / (Nr - 1)
T = np.full(Nr, 292)  # Initial temperature (K)
T_new=np.full(Nr, 292)

def crank_matrix(A,B,k,N0,Nr,r,dt,dr):

    # Symmetry at the center (r=0)
    A[0, 0] = 1
    B[0, 0] = 1

    # Precompute coefficients
    alpha = k * dt / (2 * dr**2)
    beta = lambda ri: k * dt / (2 * ri * dr)
    for i in range(N0, Nr - 1):
        A[i, i - 1] = -alpha + beta(r[i])
        A[i, i] = 1 + 2 * alpha
        A[i, i + 1] = -alpha - beta(r[i])
        B[i, i - 1] = alpha - beta(r[i])
        B[i, i] = 1 - 2 * alpha
        B[i, i + 1] = alpha + beta(r[i])

    return A,B


# Initialize matrices
A = np.zeros((Nr, Nr))
B = np.zeros((Nr, Nr))

m=Nr//2


# Apply Fourier heat flux condition at the interface (i = m)
A[m, m - 1] = -k_SiO2
A[m, m] = (k_SiO2 + k_Fe)
A[m, m + 1] = -k_Fe

B[m, m - 1] = k_SiO2 
B[m, m] = -(k_SiO2 + k_Fe)
B[m, m + 1] = k_Fe

b=np.zeros(Nr)


# Apply boundary conditions at Nr (Dirichlet T_N = 292K)
A[Nr-1, :] = 0      # Zero out the last row
A[Nr-1, Nr-1] = 1    # Set diagonal to 1
B[Nr-1, :] = 0      # Zero out B's last row
B[Nr-1, Nr-1] = 1    # Keep it consistent
b[Nr-1] = 292       # Set boundary temperature

T = np.full(Nr, 292)  # Initial temperature (K)


# Define Crank-Nicholson matrices for each subdomain
A, B = crank_matrix(A,B,k_Fe,1,m+1,r, dr, dt)
A, B = crank_matrix(A,B,k_SiO2,m+1,Nr,r, dr, dt)



for n in tqdm(range(1, Nt)):
    b[:m] = B[:m, :] @ T + (QFe(t[n - 1]) - QFe(t[n])) * dt / (rho * c_SiO2)
    b[m:] = B[m:, :] @ T + (QAl(t[n - 1]) - QAl(t[n])) * dt / (rho * c_Fe)
    b[Nr-1] = 292       # Set boundary temperature
    T_new = np.linalg.solve(A, b)

    T[:] = T_new  # Update T after solving




plt.plot(r, T_new)
plt.show()