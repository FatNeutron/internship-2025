#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from scipy.integrate import solve_ivp


# | **Quantity**                                                 | **Symbol**             | **Units**            | **Formula**                                                                                               | **Value**       | **Comment**                               |
# |:------------------------------------------------------------:|:----------------------:|:--------------------:|:---------------------------------------------------------------------------------------------------------:|:---------------:|:-----------------------------------------:|
# | **Radius**                                                   | $R$                    | m                    | -                                                                                                         | 27000           |                                           |
# | **Compressional wave**                                       | $V_{p}$                | Km/s                 | -                                                                                                         | 7.61            |                                           |
# | **Thermal diffusivity**                                      | $\kappa$                | m$^{2}$ s$^{-1}$     | (-1.67 + 2.1*$V_{p}$)                                                                                     | 1.4311e-6       |For H-Chondrites taken from Yomogida and Matsui (1983) https://gupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/JB088iB11p09513 |
# | **Emissivity**                                               | $e$                    | -                    | -                                                                                                         | 0.8             |                                           |
# | **Stefan-Boltzmann constant**                                | $\sigma$               | W m$^{-2}$ K$^{-4}$  | -                                                                                                         | 5.67037442e-8   |                                           |
# | **Initial temperature**                                      | $T_{neb}$              | K                    | -                                                                                                         | 292             |                                           |
# | **Avogadro number**                                          | $N_{A}$                | mol$^{-1}$           | -                                                                                                         | 6.022e23        |                                           |
# | **Density of H-chondrite**                                   | $\rho$                 | Kg m$^{-3}$          | -                                                                                                         | 3500            |                                           |
# | **Al abundance**                                             | Al_abnds               | %                    | -                                                                                                         | 1.13            |                                           |
# | **Ratio of $^{26}$Al**                                       | $^{26}$Al / $^{27}$Al  | -                    | -                                                                                                         | 5e-5            |                                           |
# | **Molar mass of Al**                                         | M_Al                   | Kg mol$^{-1}$        | -                                                                                                         | 0.026981538     |                                           |
# | **Atom density**                                             | A_Al                   | atoms m$^{-3}$       | Al_abnds * $\rho$ * $^{26}$Al / $^{27}$Al  * $N_{A}$ / M_Al                                               |                 |                                           |
# | **Fe abundance**                                             | Fe_abnds               | %                    | -                                                                                                         | 24              |                                           |
# | **Ratio of $^{60}$Al**                                       | $^{60}$Fe / $^{56}$Fe  | -                    | -                                                                                                         | 1e-8            |                                           |
# | **Molar mass of Al**                                         | M_Fe                   | Kg mol$^{-1}$        | -                                                                                                         | 0.026981538     |                                           |
# | **Atom density**                                             | A_Fe                   | atoms m$^{-3}$       | Fe_abnds * $\rho$ * $^{60}$Fe / $^{56}$Fe   * $N_{A}$ / M_Fe                                              |                 |                                           |
# | **Half life of $^{26}$Al**                                   | $t_{0.5, Al}$          | Myr                  | -                                                                                                         | 0.72            |                                           |
# | **Half life of $^{60}$Fe**                                   | $t_{0.5, Fe}$          | Myr                  | -                                                                                                         | 1.5             |                                           |
# | **Energy release per atom of Al**                            | $Q_{Al}$               | J                    | -                                                                                                         | 3 * 1.60218e-13 |                                           |
# | **Energy release per atom of Fe**                            | $Q_{Fe}$               | J                    | -                                                                                                         | 3 * 1.60218e-13 |                                           |
# | **Decay constant of Al**                                     | $\lambda_{Al}$           | s$^{-1}$             | $\log(2) / t_{0.5, Al}$                                                                                  |                 |                                           |
# | **Decay constant of Fe**                                     | $\lambda_{Fe}$           | s$^{-1}$             | $\log(2) / t_{0.5, Fe}$                                                                                  |                 |                                           |
# | **Thermal expansivity of olivine**                           | $\alpha$               | K$^{-1}$             | -                                                                                                         | 3.8e-5          |                                           |
# | **Compressibility**                                          | $\beta$                | Pa$^{-1}$            | -                                                                                                         | 1.82e-6         |                                           |
# | **Molar volume of Fayalite**                                 | $V_{m, Fa}$            | m$^{3}$ mol$^{-1}$   | -                                                                                                         | 46.39e-6        | https://pubs.usgs.gov/bul/1452/report.pdf |
# | **Specific heat capacity at constant pressure for Fayalite** | $c_{p}$                | J K$^{-1}$           | $172.76 - 3.4055*10^{-3}*(T) + 2.2411*10^{-5}*(T^{2}) - 3.6299*10^{6}*(T^{-2})$                                          |                 | https://pubs.usgs.gov/bul/1452/report.pdf |
# | **Specific heat capacity at volume for Fayalite**            | $c_{v}$                | J K$^{-1}$           | $c_{p} - (T*V_{m, Fa}*\alpha^{2} * \beta^{-1})$                                                           |                 |                                           |
# | **Heating rate per unit volume**                             | $Q_{rad}$              | W m$^{-3}$           | $(A_Al * \lambda_{Al} * Q_{Al} * e^{-\lambda_{Al} * t}) + (A_Fe * \lambda_{Fe} * Q_{Fe} * e^{-\lambda_{Fe} * t})$ | -               |                                           |
# | **Source term**                                              | $S$                    | K s$^{-1}$ Kg$^{-1}$ | $Q_{rad} / (\rho * c_{v}$)                                                                                |                 |                                           |

# In[10]:


#parameters
N = 700   #no of internvals
R = 270e3    #radius of sphere

dr = R/N
r = np.linspace(0, R, N+1)

yearins = 365.25 * 24 * 3600

##For H-Chondrites taken from Yomogida and Matsui (1983) https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/JB088iB11p09513
Vp = 7.61  #compressional wave velocity (km/s)
kappa = 3.8e-5 * yearins#(-1.67 + 2.1*Vp)*1e-7 #thermal diffusivity (m^2/s)


e = 0.8#emissivity
sigma = 5.67037442e-8  #stefan-boltzmann constant
T_neb = 292 #initial temp/temp of nebula

#yearstosec = 365.25*24*3600

Na = 6.022e23
Myr = 3.15576e13 #Myr in seconds
rho = 3500  #density (Kg/m^3)

# initial abundance of 26Al
Al_abnds = 0.0113
Al_ratio = 5e-5   #26al/27al
M_Al = 0.026981538    #molar mass of 27al
A_Al = Al_abnds * rho * Al_ratio * Na / M_Al  #atom density (atoms/m^3)

lambda_Al = np.log(2) / (0.717*Myr) #decay constant of 26Al (1/s)
Q_Al = 3 * 1.60218e-13    #energy release per atom (J)

#initial abundance of 60Fe
Fe_abnds = 0.24
Fe_ratio = 1e-8   #60fe/56fe
M_Fe = 0.05584      #molar mass of 56fe
A_Fe = Fe_abnds * rho * Fe_ratio * Na / M_Fe  #atom density (atoms/m^3)

lambda_Fe = np.log(2) / (2.61*Myr) #decay constant of 60Fe (1/s)
Q_Fe = 3 * 1.60218e-13    #energy release per atom (J)


#given in appendix
ther_expn = 3.8e-5  #thermal expansion (1/K)
cmprss = 1.82e-6    #compressibility (1/Pa)


t0 = 2.85*Myr  #in sec
tf = 4.58*Myr  #in sec


# In[11]:


# 1D heat equation


def Qrad(t):

  #heating rate per unit volume (W/m^3)
    return (A_Al *lambda_Al *Q_Al * np.exp(-lambda_Al * t) +
            A_Fe *lambda_Fe* Q_Fe * np.exp(-lambda_Fe * t))

def dTdt(t,T):

############################
    ##cp value and molar volume of calcium olivine taken from - https://pubs.usgs.gov/bul/1452/report.pdf
    #olivine_MVol = 59.11 * 1e-6  # Molar volume [m³/mol]
    #c_p = 1.3257e2 + 5.2510e-2*(T) - 1.9049e6/(T**2)  

    #cv = c_p - (T*olivine_MVol*(ther_expn)**2)/(cmprss)
############################
    #cp value and molar volume of Forsterite taken from - https://pubs.usgs.gov/bul/1452/report.pdf
    #Forst_MVol = 43.79 *1e-6
    #c_p = 2.2798e2 + 3.4139e-3*T - 1.7446e3*(T**-0.5) - 8.9397e5*(T**-2)

    #cv = c_p - (T*Forst_MVol*(ther_expn)**2)/(cmprss)
############################ 
    #cp value and molar volume of Fayalite taken from - https://pubs.usgs.gov/bul/1452/report.pdf
    Faya_MVol = 46.39 *1e-6
    c_p = 2100#1.7276e2 - 3.4055e-3*(T) + 2.2411e-5*(T**2) - 3.6299e6*(T**-2)

    cv = c_p #- (T*Faya_MVol*(ther_expn)**2)/(cmprss)
############################

    S = Qrad(t) / (rho * cv)
    dT = np.zeros_like(T)


    #center point
    dT[0] = 6*kappa*((T[1] - T[0])/ dr**2) + S

    #interior points
    i = np.arange(1,N)
    ri = i*dr

    dT[i] = kappa*((T[i+1] + T[i-1] - 2*T[i])/(dr**2) \
                     + (1/ri)*( (T[i+1] - T[i-1])/(dr)) ) \
                      + S

    #surface point
    dT[-1] = 2*kappa*((T[-2] - T[-1])/(dr**2) \
                     - e * sigma * (T[-1]**4 - T_neb**4)*( 1/dr + 1/R)/ (kappa * rho * c_p)) \
                     + S

    return dT
'''
    # Linearized radiation term for stability
    linear_factor = 4 * e * sigma * T[-1]**3 if T[-1] > 300 else 0
    dTdr_rad = -q_rad / k_cond

    # Hybrid implicit-explicit discretization
    dT[-1] = (2 * kappa * (T[-2] - T[-1]) / dr**2)\
              - (2 * kappa / (k_cond * dr) * q_rad\
              + (2 * kappa / R) * dTdr_rad\
              + S[-1])
'''


# In[13]:


#initial condition (constant temp)
T0 = np.full(N+1 , T_neb)

t_span = (t0, tf)

t_eval = np.linspace(*t_span, 25000)

#integrate the heat eqn
sol = solve_ivp(dTdt, t_span, T0, method = 'BDF', max_step=0.001*Myr, t_eval = t_eval)

print(sol)
print(np.shape(sol.y))
#print(sol.y)


# In[11]:


# Recreate your time and radial grids
r = np.linspace(0, R, N+1)        # radius from 0 to R, shape (N+1,)
time = sol.t / Myr                # time in Myr, shape (1000,)
temperature = sol.y               # shape (N+1, 1000)

# Create 2D grid for plotting
T_mesh, R_mesh = np.meshgrid(time, r)

# Plot 2D heatmap
plt.style.use('dark_bacValueError                                Traceback (most recent call last)
Cell In[11], line 74
     71 beta = lambda ri: k * dt / (2 * ri * dr)
     73 for i in range(1, Nr - 1):
---> 74     A[i, i - 1] = -alpha[i] + beta(r[i])
     75     A[i, i] = 1 + 2 * alpha
     76     A[i, i + 1] = -alpha - beta(r[i])

ValueError: setting an array element with a sequence.kground')
plt.figure(figsize=(12, 6))
c = plt.pcolormesh(T_mesh, R_mesh / 1e3, temperature, shading='auto', cmap='viridis')  # radius in km

# Labels and colorbar
plt.xlabel('Time (Myr)', fontsize=12)
plt.ylabel('Radius (km)', fontsize=12)
plt.title('Temperature Evolution (Color = Temperature)', fontsize=14)
plt.colorbar(c, label='Temperature (K)')

#plt.savefig('countor-plot6.png', dpi=1200, bbox_inches='tight')
plt.tight_layout()
plt.show()


# In[12]:


transparentr = np.linspace(0, R, N+1)  # shape: (N+1,)
T_mesh, R_mesh = np.meshgrid(sol.t / Myr, r)  # Convert time to Myr for nicer units
Temperature = sol.y  # shape: (N+1, 1000)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(T_mesh, R_mesh / 1e3, Temperature, cmap='viridis', edgecolor='none')  # Radius in km

# Labels
ax.set_xlim(ax.get_xlim()[::-1])
ax.set_xlabel('Time (Myr)', fontsize=12)
ax.set_ylabel('Radius (km)', fontsize=12)
ax.set_zlabel('Temperature (K)', fontsize=12)
ax.set_title('3D Plot of Temperature vs Time and Radius', fontsize=14)

#plt.savefig('3d-plot6.png', dpi=1200, bbox_inches='tight')
# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Temperature (K)')

plt.tight_layout()
plt.show()
# Save the figure
plt.tight_layout()
#plt.savefig("temperature_plot.png", dpi=300)  # You can adjust dpi for resolution


# In[ ]:





# In[ ]:





# In[ ]:




