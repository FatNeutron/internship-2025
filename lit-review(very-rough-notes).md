
> [!warning]
> This file was written in obsidian and synced through GitHub, so some format may not load properly!!!
> 
> **GitHub app** does not load the format properly!!!


**Things to do:** 

- [x] read thesis by Shehzade Manzoor Khan.
	- [x] learn the methods used.
		- [x] Crank-Nicolson method.
		- [x] Method of lines.
- [ ] read paper by Amitabha Ghosh.
- [ ] Write code for modelling thermal evolution.

-------------
# Thesis notes

## Some terms

- Planetesimals -> solid body formed by accretion, in its early stages.
- Circumstellar disc -> a ring-shaped accretion disk of matter.
- Protoplanetary disc -> Circumstellar disc but around a newly formed star.
- protoplanet -> a planet at very early stages of becoming a planet. 


--------------


## Imp Isotopes

$^{27}\text{Al}$ is stable, and $^{26}\text{Al}$ is radioactive isotope.
$^{24}\text{Mg}$ is most abundant & stable.
$^{26}\text{Mg}$ is stable isotope.

$^{26}\text{Al}$(hf ~0.717 myr) & $^{60}\text{Fe}$(hf ~2.6 myr) are important while considering thermal energy.

>$^{26}\text{Al}$ -> $^{26}\text{Mg}$ 
>
>$^{60}\text{Fe}$ ->-> $^{60}\text{Ni}$

After the complete decay of Al, to get its presence before decay we use the ratios comparison of $^{26}\text{Mg} / ^{24}\text{Mg}$ and $^{27}\text{Al} / ^{24}\text{Mg}$ in the minerals.

$^{26}\text{Al}$ is for quick heating(relatively speaking, it was imp as it was releasing energy when the planetesimals were still young) and $^{60}\text{Fe}$ helps in maintaining that elevated temp after all the $^{26}\text{Al}$ is decayed.


## Vesta

Vesta is a differentiated asteroid with metallic core, silicate mantle, and basaltic crust.

radius ~270 Km

Formed just after few myr of the solar system formation with rapid accretion. From the [[ghosh_mcsween_1998_maps_vesta_thermal_model (2).pdf|paper by Amitabha Ghosh and Harry Y. McSween, Jr.]], the predicted times are relative [CAIs](https://en.wikipedia.org/wiki/Calcium%E2%80%93aluminium-rich_inclusion) formation and are given as,

> ==accretion at 2.85 Myr==
> 
> ==core formation at 4.58 Myr==
> 
> ==crust formation at 6.58 Myr==


[HED meteorites](https://en.wikipedia.org/wiki/HED_meteorite) (howardites, eucrites, and diogenites) are considered to be originated from Vesta. Diogenites are derived from the lower crust or upper mantle, eucrites comes from basaltic surface flows or shallow intrusions.

Heat released from $^{26}\text{Al}$ decay was enough for partial to extensive melting which lead to the formation of core(metallic iron towards center & silicate mantle and crust).


## Modeling Equation


##### 3D heat equation:
$$\frac{\partial T}{\partial t} = \frac{\kappa}{\rho c_v} \left[
\frac{1}{R^2} \frac{\partial}{\partial R} \left( R^2 \frac{\partial T}{\partial R} \right) + \frac{1}{R^2 \sin \theta} \frac{\partial}{\partial \theta} \left( \sin \theta \frac{\partial T}{\partial \theta} \right) + \frac{1}{R^2 \sin^2 \theta} \frac{\partial^2 T}{\partial \phi^2}\right] + \frac{Q_{\text{rad}}}{\rho c_v} $$

For modelling we assume spherical symmetry, which means that there are no angular dependencies so the angular terms become 0.

So our equation simplifies to following 1D heat equation,

##### 1D heat equation:
$$\frac{\partial{T}}{\partial{t}} = \frac{1}{R^{2}}\frac{\partial}{\partial{R}}\Big(R^{2} \kappa \frac{\partial{T}}{\partial{R}}\Big) + \frac{Q_{rad}}{\rho c_{v}}$$

| Symbol                                                                                              | Meaning                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $T(R, t)$                                                                                           | Temperature as a function of **radial distance** $R$ and **time** $t$                                                                                    |
| $t$                                                                                                 | Time (seconds, or years in planetary models)                                                                                                             |
| $R$                                                                                                 | Radial coordinate from the planet’s center (meters)                                                                                                      |
| $\frac{\partial T}{\partial t}$                                                                     | Rate of temperature change with time at radius $R$                                                                                                       |
| $\kappa(R, T)$                                                                                      | **Thermal diffusivity** (W/m·K) — may depend on radius or temperature                                                                                    |
| $\frac{\partial T}{\partial R}$                                                                     | Radial temperature gradient (how temperature changes with depth)                                                                                         |
| $\frac{1}{R^2} \frac{\partial}{\partial R} \left( R^2 \kappa \frac{\partial T}{\partial R} \right)$ | **Radial heat conduction term** — accounts for heat flowing in/out of a spherical shell at radius $R$, including the increasing surface area with radius |
| $Q_{\text{rad}}$                                                                                    | **Volumetric internal heat production rate** (W/m³), e.g., from radioactive decay                                                                        |
| $\rho$                                                                                              | Density of the material (kg/m³)                                                                                                                          |
| $c_v$                                                                                               | **Specific heat capacity at constant volume** (J/kg·K) — amount of energy needed to raise the temperature of a unit mass by 1 K                          |
| $\frac{Q_{\text{rad}}}{\rho c_v}$                                                                   | Temperature increase due to internal heating, normalized per unit mass and heat capacity                                                                 |

###### $Q_{rad}$ term:

$Q_{rad}$ term is the total internal radiogenic heat produced by radioactive isotopes,

$$Q_{\text{rad}} = A_{0,\text{Al}} \cdot Q_{0,\text{Al}} \cdot e^{-\lambda_{\text{Al}} t} + A_{0,\text{Fe}} \cdot Q_{0,\text{Fe}} \cdot e^{-\lambda_{\text{Fe}} t}$$


| Symbol                | Meaning                                                          |
| --------------------- | ---------------------------------------------------------------- |
| $Q_{\text{rad}}$      | Volumetric radiogenic heat production rate at time $t$ (in W/m³) |
| $A_{0,\text{Al}}$     | Initial abundance of $^{26}\text{Al}$ (atoms per m³ or kg)       |
| $Q_{0,\text{Al}}$     | Energy released per decay of $^{26}\text{Al}$ (in joules)        |
| $\lambda_{\text{Al}}$ | Decay constant of $^{26}\text{Al}$, related to its half-life     |
| $A_{0,\text{Fe}}$     | Initial abundance of $^{60}\text{Fe}$                            |
| $Q_{0,\text{Fe}}$     | Energy released per decay of $^{60}\text{Fe}$                    |
| $\lambda_{\text{Fe}}$ | Decay constant of $^{60}\text{Fe}$                               |
| $t$                   | Time since the start of the solar system (in years or seconds)   |
| $e^{-\lambda t}$      | Exponential decay factor for radioactive nuclides                |


## Modelling Methods

We have our heat equation as,

$$\frac{\partial{T}}{\partial{t}} = \frac{1}{R^{2}}\frac{\partial}{\partial{R}}\Big(R^{2} \kappa \frac{\partial{T}}{\partial{R}}\Big) + \frac{Q_{rad}}{\rho c_{v}}, \quad 0 < r < R, \quad t > 0.$$

Let,   $\quad S = \frac{Q_{rad}}{\rho c_{v}}$

$$\boxed{\frac{\partial{T}}{\partial{t}} = \Big(\frac{2\kappa}{r}\frac{\partial{T}}{\partial{r}} + \kappa \frac{\partial^2{T}}{\partial{r^2}}\Big) + S}$$


### Crank-Nicolson method 


We consider the 1D heat equation in spherical coordinates on $([0,R])$. We partition the spatial domain into $(N)$ intervals of width $(\Delta{r} = \frac{R}{N})$, so

$$
r_{i} = i\Delta{r}, \quad i = 0,1,2,\dots,N.
$$

We partition the time domain into steps of size $(\Delta{t})$, so

$$
t^{n} = n\Delta{t}, \quad n = 0,1,2,\dots
$$


> [!Note] 
> Note that here we $t^{n}$ doesn't mean t raised to $n$ th power. It is just an index notation like $r_{n}$.
> For convenience we use superscript for index in time domain and subscript for index in spatial domain.

#### Discretize the time derivative

We need to approximate the time derivative by a forward difference:

$$
\frac{\partial{T}}{\partial{t}}(r_{i},t^{n}) \approx \frac{T_{i}^{n+1} - T_{i}^{n}}{\Delta{t}}
$$


#### Discretize the space derivative

Then we approximate the second spatial derivative by central difference:

$$\frac{\partial^2{T}}{\partial{r^2}}(r_{i},t^{n}) \approx \frac{T_{i+1}^{n} + T_{i-1}^{n} - 2T_{i}^{n}}{(\Delta{r})^2}$$

And first spatial derivative by backward difference:

$$\frac{\partial{T}}{\partial{r}}(r_{i},t^{n}) \approx \frac{T_{i+1}^{n} - T_{i-1}^{n}}{2\Delta{r}}$$

#### Crank–Nicolson: Averaging Explicit and Implicit

Crank-Nicolos is formed by averaging the spatial derivatives terms at time $(n)$(called explicit) and $(n+1)$(called implicit). So the form of equation will look like this,

$$\frac{T_{i}^{n+1} - T_{i}^{n}}{\Delta{t}} = \kappa \Big(\frac{\text{(Spatial terms)}^{n} + \text{(Spatial terms)}^{n+1}}{2}\Big) + S$$

Substituting terms in this equation for spatial terms,

$$
\frac{T_{i}^{n+1} - T_{i}^{n}}{\Delta{t}} = \kappa \Big[ \frac{\frac{2}{r_{i}}\Big(\frac{T_{i+1}^{n} - T_{i-1}^{n}}{2\Delta{r}} \Big) + \Big( \frac{T_{i+1}^{n} +T_{i-1}^{n} - 2T_{i}^{n}}{(\Delta{r})^2}\Big) + \frac{2}{r_{i}}\Big(\frac{T_{i+1}^{n+1} - T_{i-1}^{n+1}}{2\Delta{r}} \Big) + \Big( \frac{T_{i+1}^{n+1} +T_{i-1}^{n+1} - 2T_{i}^{n+1}}{(\Delta{r})^2}\Big)}{2} \Big] + S
$$

$$
= T_{i}^{n+1} - T_{i}^{n} = \Delta{t} \kappa \Big[ \frac{\frac{2}{r_{i}}\Big(\frac{T_{i+1}^{n} - T_{i-1}^{n}}{2\Delta{r}} \Big) + \Big( \frac{T_{i+1}^{n} +T_{i-1}^{n} - 2T_{i}^{n}}{(\Delta{r})^2}\Big) + \frac{2}{r_{i}}\Big(\frac{T_{i+1}^{n+1} - T_{i-1}^{n+1}}{2\Delta{r}} \Big) + \Big( \frac{T_{i+1}^{n+1} +T_{i-1}^{n+1} - 2T_{i}^{n+1}}{(\Delta{r})^2}\Big)}{2}  \Big] + S\Delta{t}
$$

$$
= T_{i}^{n+1} - T_{i}^{n} = \frac{\Delta{t} \kappa}{2r_{i}\Delta{r}} (T_{i+1}^{n} - T_{i-1}^{n}) + \frac{\Delta{t} \kappa}{2(\Delta{r})^{2}}(T_{i+1}^{n} + T_{i-1}^{n} -2T_{i}^{n}) + \frac{\Delta{t} \kappa}{2r_{i}\Delta{r}} (T_{i+1}^{n+1} - T_{i-1}^{n+1}) + \frac{\Delta{t} \kappa}{2(\Delta{r})^{2}}(T_{i+1}^{n+1} + T_{i-1}^{n+1} -2T_{i}^{n+1} + S\Delta{t}
$$

$$
\text{let,} \quad \alpha = \frac{\Delta{t} \kappa}{2(\Delta{r})^2}, \quad \text{and} \quad \beta_{i} = \frac{\Delta{t} \kappa}{2r_{i} \Delta{r}}
$$

$$
\boxed{T_{i}^{n+1}(1 + 2 \alpha) + T_{i+1}^{n+1}(- \alpha - \beta_{i}) + T_{i-1}^{n+1}(\beta_{i} - \alpha) = T_{i}^{n}(1 - 2 \alpha) + T_{i+1}^{n}(\alpha + \beta_{i}) + T_{i-1}^{n}(\alpha - \beta_{i}) + S\Delta{t}}
$$

This equations can be defined in tridigonal linear system,

$$AT^{n+1} = BT^{n} + C$$

which further can be solved some algorithms like Thomas algorithm.

---------------
We will not use the crank-nicolson method, it uses explicit terms which can be unstable when solving, we will be using **Method of lines** which uses implicit terms which is stable.
And also crank-nicolos method uses fixed $\Delta{t}$ where MOL uses adaptive $\Delta{t}$ which is helpful when large scale modelling.

--------------------


### Method of line

In this method we discretize **only spatial terms** and keep time continuous.

We partition the spatial domain into $(N)$ intervals of width $(\Delta{r} = \frac{R}{N})$, so

$$
r_{i} = i(\Delta{r}), \quad i = 0,1,2,\dots,N.
$$

$i = 0$ -> center
$i = N$ -> surface

We discretize the spatial terms with central difference and backward difference equation and substitute in the 1D heat equation, then we have,

$$
\boxed{\frac{dT_{i}}{dt} = \kappa \Big[\frac{T_{i+1} + T_{i-1} - 2T_{i}}{(\Delta{r})^{2}} + \frac{2}{r_{i}}\Big(\frac{T_{i+1} - T_{i - 1}}{2(\Delta{r})}\Big)\Big] + S_{i} \quad for \quad i=[1,N-1]}
$$


##### Center point ($i = 0, r = 0$)


Since our heat equation is,

$$
\frac{\partial{T}}{\partial{t}} = \Big(\frac{2\kappa}{r}\frac{\partial{T}}{\partial{r}} + \kappa \frac{\partial^2{T}}{\partial{r^2}}\Big) + S_{i}
$$

and at $r = 0$ first spatial derivative term is undefined.
so we need to take limit,

$$
\lim_{r \to 0} \frac{1}{r}{\frac{\partial{T}}{\partial{r}}}
$$

for $r = 0$, which is at the center of body we assume that there is no heat flux so,

$$
\frac{\partial{T}}{\partial{r}}\Big|_{r = 0} = 0
$$

So we can use L'Hôpital's rule to this form, 

$$
\lim_{r \to 0} \frac{\frac{\partial{T}}{\partial{r}}}{r}. \quad \text{since}, \quad \frac{\frac{\partial{T}}{\partial{r}}}{r} = \frac{0}{0}
$$

So,

$$
\lim_{r \to 0} \frac{\frac{\partial{T}}{\partial{r}}}{r} = \frac{\frac{d}{dr}(\frac{\partial{T}}{\partial{r}}) }{\frac{d}{dr}(r)} = \frac{\frac{\partial^2{T}}{\partial{r^2}}}{1} = \frac{\partial^2{T}}{\partial{r^2}}
$$

Substitute this term back in heat equation,

$$
\frac{\partial{T}}{\partial{t}} = \Big(2\kappa\frac{\partial^2{T}}{\partial{r^2}} + \kappa \frac{\partial^2{T}}{\partial{r^2}}\Big) + S_{0}
$$

$$
= \frac{\partial{T}}{\partial{t}} = \Big(3\kappa\frac{\partial^2{T}}{\partial{r^2}}\Big) + S_{0}
$$

$$
= \frac{\partial{T}}{\partial{t}} \approx 3\kappa\Big(\frac{T_{1} + T_{{-1}} - 2T_{0}}{(\Delta{r})^2}\Big) + S_{0}
$$

here $T_{-1}$ is a ghost point we can replace it with $T_{1}$ due to symmetry, $T_{-1} = T_{1}$

$$
\boxed{\frac{\partial{T}}{\partial{t}} \approx 3\kappa\Big(\frac{2T_{1} - 2T_{0}}{(\Delta{r})^2}\Big) + S_{0} \quad \text{for,} \quad r=0.}
$$

##### Surface point ($i = N, r = R$)

here we consider the heat loss from surface is due to radiative boundary condition, which is given as,

$$
\frac{dT_{N}}{dr} = \frac{e\sigma}{\kappa_c} (T_{surf}^{4} - T_{neb}^{4})
$$

where,

| **Symbol** | **Meaning**                                  |
| ---------- | -------------------------------------------- |
| $T_{surf}$ | Temperature at surface                       |
| $T_{neb}$  | Temperature of surrounding nebula (constant) |
| $\sigma$   | Stefan-Boltzmann constant                    |
| $e$        | Emissivity                                   |
| $\kappa_c$ | Thermal conductivity                         |

we can rewrite the equation as,

$$
\frac{T_{N+1} - T_{N-1}}{2(\Delta{r})} = \frac{e\sigma}{\kappa_c} (T_{surf}^{4} - T_{neb}^{4})
$$

here $T_{N+1}$ is ghost point.

rearranging equation, 

$$
T_{N+1} = \frac{{2(\Delta{r})}e\sigma}{\kappa_c} (T_{surf}^{4} - T_{neb}^{4}) + T_{N-1}
$$

we know that,

$$
\frac{\partial^2{T}}{\partial{r^2}} = \frac{T_{N+1} + T_{N-1} - 2T_{N}}{(\Delta{r})^2} \quad \text{for,} \quad r = R \quad \text{or} \quad i = N.
$$

Substitute the term for $T_{N+1}$ in this equation,

$$
\frac{\partial^2{T}}{\partial{r^2}} = \frac{(\frac{{2(\Delta{r})}e\sigma}{\kappa_c} (T_{surf}^{4} - T_{neb}^{4}) + T_{N-1}) + T_{N-1} - 2T_{N}}{(\Delta{r})^2}
$$

now substitute first spatial derivative and second spatial derivative in heat equation,

$$
\frac{\partial{T}}{\partial{t}} = \Big[\frac{2\kappa}{r}\Big(\frac{e\sigma}{\kappa_c} (T_{surf}^{4} - T_{neb}^{4})\Big) + \kappa \Big(\frac{(\frac{{2(\Delta{r})}e\sigma}{\kappa_c} (T_{surf}^{4} - T_{neb}^{4}) + T_{N-1}) + T_{N-1} - 2T_{N}}{(\Delta{r})^2}\Big)\Big] + S_{N}
$$

rearranging, 

$$
\boxed{\frac{dT}{dt} = 2\kappa \Big[ \frac{(T_{N-1} - T_{N})}{(\Delta{r})^2} + \frac{e \sigma (T_{surf}^{4} - T_{neb}^{4})}{\kappa_c}\Big(\frac{1}{\Delta{r}} + \frac{1}{R}  \Big) \Big] + S_{N} \quad \text{for,} \quad r=R.}
$$

So the final equation will be,

$$
\boxed{\frac{dT_{i}}{dt} = 
\begin{cases}
3\kappa\Big(\frac{2T_{1} - 2T_{0}}{(\Delta{r})^2}\Big) + S_{0} & \text{if } r = 0 \\
\kappa \Big[\frac{T_{i+1} + T_{i-1} - 2T_{i}}{(\Delta{r})^{2}} + \frac{2}{r_{i}}\Big(\frac{T_{i+1} - T_{i - 1}}{2(\Delta{r})}\Big)\Big] + S_{i} & \text{if } 0 < r < R \\
\frac{dT}{dt} = 2\kappa \Big[ \frac{(T_{N-1} - T_{N})}{(\Delta{r})^2} + \frac{e \sigma (T_{surf}^{4} - T_{neb}^{4})}{\kappa_c}\Big(\frac{1}{\Delta{r}} + \frac{1}{R}  \Big) \Big] + S_{N} & \text{if } r = R
\end{cases}}
$$


### Parameters


| **Quantity**                                           |      **Symbol**       |      **Units**       |                                                                        **Formula**                                                                        |             **Value**             | **Comment**          |
| :----------------------------------------------------- | :-------------------: | :------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------: | :------------------- |
| Radius                                                 |          $R$          |          m           |                                                                             -                                                                             |               27000               | [1]                  |
| Compressional wave                                     |         $V_p$         |         km/s         |                                                                             -                                                                             |               7.61                | For H-Chondrites [2] |
| Thermal diffusivity                                    |       $\kappa$        |       m$^2$/s        |                                                                  $-1.67 + 2.1 \cdot V_p$                                                                  |             1.4311e-6             | For H-Chondrites [2] |
| Emissivity                                             |          $e$          |          -           |                                                                             -                                                                             |                0.8                | [1]                  |
| Stefan-Boltzmann constant                              |       $\sigma$        | W m$^{-2}$ K$^{-4}$  |                                                                             -                                                                             |           5.67037442e-8           | Taken from internet  |
| Initial temperature                                    |   $T_{\text{neb}}$    |          K           |                                                                             -                                                                             |                292                | [1]                  |
| Avogadro number                                        |         $N_A$         |      mol$^{-1}$      |                                                                             -                                                                             |      $6.022 \times 10^{23}$       | Taken from internet  |
| Density of H-chondrite                                 |        $\rho$         |     kg m$^{-3}$      |                                                                             -                                                                             |               3500                | [1]                  |
| Al abundance                                           |       Al\_abnds       |          %           |                                                                             -                                                                             |               1.13                | [1]                  |
| Ratio of $^{26}$Al                                     |  $^{26}$Al/$^{27}$Al  |          -           |                                                                             -                                                                             |        $5 \times 10^{-5}$         | [1]                  |
| Molar mass of Al                                       |    $M_{\text{Al}}$    |    kg mol$^{-1}$     |                                                                             -                                                                             |            0.026981538            | Taken from internet  |
| Atom density of Al                                     |    $A_{\text{Al}}$    |    atoms m$^{-3}$    |                      $\text{Al}_\text{abnds} \cdot \rho \cdot \frac{^{26}\text{Al}}{^{27}\text{Al}} \cdot \frac{N_A}{M_{\text{Al}}}$                      |            Calculated             |                      |
| Fe abundance                                           |       Fe\_abnds       |          %           |                                                                             -                                                                             |                24                 | [1]                  |
| Ratio of $^{60}$Fe                                     |  $^{60}$Fe/$^{56}$Fe  |          -           |                                                                             -                                                                             |        $1 \times 10^{-8}$         | [1]                  |
| Molar mass of Fe                                       |    $M_{\text{Fe}}$    |    kg mol$^{-1}$     |                                                                             -                                                                             |              0.05584              | Taken from internet  |
| Atom density of Fe                                     |    $A_{\text{Fe}}$    |    atoms m$^{-3}$    |                      $\text{Fe}_\text{abnds} \cdot \rho \cdot \frac{^{60}\text{Fe}}{^{56}\text{Fe}} \cdot \frac{N_A}{M_{\text{Fe}}}$                      |            Calculated             |                      |
| Half life of $^{26}$Al                                 |  $t_{0.5,\text{Al}}$  |         Myr          |                                                                             -                                                                             |               0.72                | [1]                  |
| Half life of $^{60}$Fe                                 |  $t_{0.5,\text{Fe}}$  |         Myr          |                                                                             -                                                                             |                1.5                | [1]                  |
| Energy release per atom of Al                          |    $Q_{\text{Al}}$    |          J           |                                                                             -                                                                             | $3 \cdot 1.60218 \times 10^{-13}$ | [1]                  |
| Energy release per atom of Fe                          |    $Q_{\text{Fe}}$    |          J           |                                                                             -                                                                             | $3 \cdot 1.60218 \times 10^{-13}$ | [1]                  |
| Decay constant of Al                                   | $\lambda_{\text{Al}}$ |       s$^{-1}$       |                                                                $\log(2)/t_{0.5,\text{Al}}$                                                                |            Calculated             |                      |
| Decay constant of Fe                                   | $\lambda_{\text{Fe}}$ |       s$^{-1}$       |                                                                $\log(2)/t_{0.5,\text{Fe}}$                                                                |            Calculated             |                      |
| Thermal expansivity of olivine                         |       $\alpha$        |       K$^{-1}$       |                                                                             -                                                                             |       $3.8 \times 10^{-5}$        | [1]                  |
| Compressibility                                        |        $\beta$        |      Pa$^{-1}$       |                                                                             -                                                                             |       $1.82 \times 10^{-6}$       | [1]                  |
| Molar volume of Fayalite                               |   $V_{m,\text{Fa}}$   |      m$^3$/mol       |                                                                             -                                                                             |      $46.39 \times 10^{-6}$       | [3]                  |
| Specific heat capacity at constant pressure (Fayalite) |         $c_p$         |      J K$^{-1}$      |                                 $172.76 - 3.4055 \cdot 10^{-3} T + 2.2411 \cdot 10^{-5} T^2 - 3.6299 \cdot 10^{6} T^{-2}$                                 |                                   | [3]                  |
| Specific heat capacity at volume (Fayalite)            |         $c_v$         |      J K$^{-1}$      |                                                 $c_p - (T \cdot V_{m,\text{Fa}} \cdot \alpha^2 / \beta)$                                                  |                                   | [1]                  |
| Heating rate per unit volume                           |   $Q_{\text{rad}}$    |      W m$^{-3}$      | $A_{\text{Al}} \lambda_{\text{Al}} Q_{\text{Al}} e^{-\lambda_{\text{Al}} t} + A_{\text{Fe}} \lambda_{\text{Fe}} Q_{\text{Fe}} e^{-\lambda_{\text{Fe}} t}$ |                 -                 | Calculated           |
| Source term                                            |          $S$          | K s$^{-1}$ kg$^{-1}$ |                                                            $Q_{\text{rad}} / (\rho \cdot c_v)$                                                            |                                   | [1]                  |


[1] A Thermal Model for the Differentiation of Asteroid 4 Vesta, Based on Radiogenic Heating — Amitabha Ghosh & Harry Y. McSween, Jr.

[2] Yomogida, K. & Matsui, T. (1983). *Physical properties of ordinary chondrites*, Journal of Geophysical Research: Solid Earth, 88(B11), 9513–9533. [https://doi.org/10.1029/JB088iB11p09513](https://doi.org/10.1029/JB088iB11p09513)

[3] Thermodynamic Properties of Minerals and Related Substances at 298.15 K and 1 Bar Pressure and at Higher Temperatures. *USGS Bulletin 1452*. [https://pubs.usgs.gov/bul/1452/report.pdf](https://pubs.usgs.gov/bul/1452/report.pdf)
