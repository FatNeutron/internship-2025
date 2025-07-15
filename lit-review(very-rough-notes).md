
> [!warning]
> This file was written in obsidian and synced through GitHub, so some format may not load properly!!!
> 
> **GitHub app** does not load the format properly!!!


**Things to do:** 

- [x] read thesis by Shehzade Manzoor Khan.
	- [x] learn the methods used.
		- [x] Crank-Nicolson method.
		- [x] Method of lines.
- [x] read paper by Amitabha Ghosh.
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


### Parameters (Stage 1)


| **Quantity**                                           | **Symbol**                          | **Units**  | **Formula**                                                                                       | **Value**                         | **Comment**          |
| :----------------------------------------------------- | :---------------------------------- | :--------- | :------------------------------------------------------------------------------------------------ | :-------------------------------- | :------------------- |
| Compressional wave                                     | $V_p$                               | km/s       | -                                                                                                 | 7.61                              | For H-Chondrites [2] |
| Thermal diffusivity                                    | $\kappa$                            | m²/s       | $-1.67 + 2.1 \cdot V_p$                                                                           | 1.4311e−6                         | For H-Chondrites [2] |
| Emissivity                                             | $e$                                 | -          | -                                                                                                 | 0.8                               | [1]                  |
| Stefan–Boltzmann constant                              | $\sigma$                            | W·m⁻²·K⁻⁴  | -                                                                                                 | 5.67037442e−8                     | Taken from internet  |
| Initial temperature                                    | $T_{neb}$                           | K          | -                                                                                                 | 292                               | [1]                  |
| Avogadro number                                        | $N_A$                               | mol⁻¹      | -                                                                                                 | $6.022 \times 10^{23}$            | Taken from internet  |
| Density of H-chondrite                                 | $\rho$                              | kg·m⁻³     | -                                                                                                 | 3500                              | [1]                  |
| Al abundance                                           | $Al_{abnds}$                        | %          | -                                                                                                 | 1.13                              | [1]                  |
| Ratio of $^{26}\text{Al}$                              | $^{26}\text{Al}$ / $^{27}\text{Al}$ | -          | -                                                                                                 | $5 \times 10^{-5}$                | [1]                  |
| Molar mass of Al                                       | $M_{Al}$                            | kg·mol⁻¹   | -                                                                                                 | 0.026981538                       | Taken from internet  |
| Atom density of Al                                     | $A_{Al}$                            | atoms·m⁻³  | $Al_{abnds} \cdot \rho \cdot \frac{{}^{26}Al}{{}^{27}Al} \cdot \frac{N_A}{M_{Al}}$                | -                                 | Calculated           |
| Fe abundance                                           | $Fe_{abnds}$                        | %          | -                                                                                                 | 24                                | [1]                  |
| Ratio of $^{20}\text{Fe}$                              | $^{60}\text{Fe}$ / $^{56}\text{Fe}$ | -          | -                                                                                                 | $1 \times 10^{-8}$                | [1]                  |
| Molar mass of Fe                                       | $M_{Fe}$                            | kg·mol⁻¹   | -                                                                                                 | 0.05584                           | Taken from internet  |
| Atom density of Fe                                     | $A_{Fe}$                            | atoms·m⁻³  | $Fe_{abnds} \cdot \rho \cdot \frac{{}^{60}Fe}{{}^{56}Fe} \cdot \frac{N_A}{M_{Fe}}$                | -                                 | Calculated           |
| Half life of $^{26}\text{Al}$                          | $t_{0.5,Al}$                        | Myr        | -                                                                                                 | 0.72                              | [1]                  |
| Half life of $^{60}\text{Fe}$                          | $t_{0.5,Fe}$                        | Myr        | -                                                                                                 | 1.5                               | [1]                  |
| Energy per atom of Al                                  | $Q_{Al}$                            | J          | -                                                                                                 | $3 \cdot 1.60218 \times 10^{-13}$ | [1]                  |
| Energy per atom of Fe                                  | $Q_{Fe}$                            | J          | -                                                                                                 | $3 \cdot 1.60218 \times 10^{-13}$ | [1]                  |
| Decay constant of Al                                   | $\lambda_{Al}$                      | s⁻¹        | $\log(2) / t_{0.5,Al}$                                                                            | -                                 | Calculated           |
| Decay constant of Fe                                   | $\lambda_{Fe}$                      | s⁻¹        | $\log(2) / t_{0.5,Fe}$                                                                            | -                                 | Calculated           |
| Thermal expansivity of olivine                         | $\alpha$                            | K⁻¹        | -                                                                                                 | $3.8 \times 10^{-5}$              | [1]                  |
| Compressibility                                        | $\beta$                             | Pa⁻¹       | -                                                                                                 | $1.82 \times 10^{-6}$             | [1]                  |
| Molar volume of Fayalite                               | $V_{m,Fa}$                          | m³/mol     | -                                                                                                 | $46.39 \times 10^{-6}$            | [3]                  |
| Specific heat capacity at constant pressure (Fayalite) | $c_p$                               | J·K⁻¹      | $172.76 - 3.4055 \cdot 10^{-3}T + 2.2411 \cdot 10^{-5}T^2 - 3.6299 \cdot 10^{6}T^{-2}$            | -                                 | [3]                  |
| Specific heat capacity at volume (Fayalite)            | $c_v$                               | J·K⁻¹      | $c_p - (T \cdot V_{m,Fa} \cdot \alpha^2 / \beta)$                                                 | -                                 | [1]                  |
| Heating rate per unit volume                           | $Q_{rad}$                           | W·m⁻³      | $A_{Al} \lambda_{Al} Q_{Al} e^{-\lambda_{Al} t} + A_{Fe} \lambda_{Fe} Q_{Fe} e^{-\lambda_{Fe} t}$ | -                                 | Calculated           |
| Source term                                            | $S$                                 | K·s⁻¹·kg⁻¹ | $Q_{rad} / (\rho \cdot c_v)$                                                                      | -                                 | [1]                  |



[1] A Thermal Model for the Differentiation of Asteroid 4 Vesta, Based on Radiogenic Heating — Amitabha Ghosh & Harry Y. McSween, Jr.

[2] Yomogida, K. & Matsui, T. (1983). *Physical properties of ordinary chondrites*, Journal of Geophysical Research: Solid Earth, 88(B11), 9513–9533. [https://doi.org/10.1029/JB088iB11p09513](https://doi.org/10.1029/JB088iB11p09513)

[3] Thermodynamic Properties of Minerals and Related Substances at 298.15 K and 1 Bar Pressure and at Higher Temperatures. *USGS Bulletin 1452*. [https://pubs.usgs.gov/bul/1452/report.pdf](https://pubs.usgs.gov/bul/1452/report.pdf)




### Difference b/w CN and MOL



###### parameters



| **Quantity**                                           | **Symbol**                          | **Units(MOL)**               | **Value(MOL)**                    | **Units(CN)**                | **Value(CN)**                     |
| :----------------------------------------------------- | :---------------------------------- | :--------------------------- | :-------------------------------- | :--------------------------- | :-------------------------------- |
| Compressional wave                                     | $V_p$                               | km/s                         | 7.61                              | -                            | -                                 |
| Thermal diffusivity                                    | $\kappa$                            | m²/yr                        | 45.16208136                       | -                            | -                                 |
| Thermal Conductivity                                   | k                                   | $W m^{-1} K^{-1}$            | varying [~17.2, ~30.72]           | $W m^{-1} K^{-1}$            | 1199.1888                         |
| Emissivity                                             | $e$                                 | -                            | 0.8                               | -                            | 0.8                               |
| Stefan–Boltzmann constant                              | $\sigma$                            | W·m⁻²·K⁻⁴                    | 5.67037442e−8                     | W·m⁻²·K⁻⁴                    | 5.67037442e−8                     |
| Initial temperature                                    | $T_{neb}$                           | K                            | 292                               | K                            | 292                               |
| Avogadro number                                        | $N_A$                               | mol⁻¹                        | $6.022 \times 10^{23}$            | mol⁻¹                        | $6.022 \times 10^{23}$            |
| Density of H-chondrite                                 | $\rho$                              | kg·m⁻³                       | 3500                              | kg·m⁻³                       | 3500                              |
| Al abundance                                           | $Al_{abnds}$                        | %                            | 1.13                              | %                            | 1.13                              |
| Ratio of $^{26}\text{Al}$                              | $^{26}\text{Al}$ / $^{27}\text{Al}$ | -                            | $5 \times 10^{-5}$                | -                            | $5 \times 10^{-5}$                |
| Molar mass of Al                                       | $M_{Al}$                            | kg·mol⁻¹                     | 0.026981538                       | kg·mol⁻¹                     | 0.027                             |
| Atom density of Al                                     | $A_{Al}$                            | atoms·m⁻³                    | $4.413575 \times 10^{22}$         | atoms·m⁻³                    | $4.410557 \times 10^{22}$         |
| Fe abundance                                           | $Fe_{abnds}$                        | %                            | 24                                | %                            | 24                                |
| Ratio of $^{20}\text{Fe}$                              | $^{60}\text{Fe}$ / $^{56}\text{Fe}$ | -                            | $1 \times 10^{-8}$                | -                            | $1 \times 10^{-8}$                |
| Molar mass of Fe                                       | $M_{Fe}$                            | kg·mol⁻¹                     | 0.05584                           | kg·mol⁻¹                     | 0.056                             |
| Atom density of Fe                                     | $A_{Fe}$                            | atoms·m⁻³                    | $9.058882 \times 10^{19}$         | atoms·m⁻³                    | $9.033 \times 10^{19}$            |
| Half life of $^{26}\text{Al}$                          | $t_{0.5,Al}$                        | Myr                          | 0.72                              | Myr                          | 0.72                              |
| Half life of $^{60}\text{Fe}$                          | $t_{0.5,Fe}$                        | Myr                          | 1.5                               | Myr                          | 1.5                               |
| Energy per atom of Al                                  | $Q_{Al}$                            | J                            | $3 \cdot 1.60218 \times 10^{-13}$ | J                            | $3 \cdot 1.60218 \times 10^{-13}$ |
| Energy per atom of Fe                                  | $Q_{Fe}$                            | J                            | $3 \cdot 1.60218 \times 10^{-13}$ | J                            | $3 \cdot 1.60218 \times 10^{-13}$ |
| Decay constant of Al                                   | $\lambda_{Al}$                      | ye⁻¹                         | $9.627044 \times 10^{-7}$         | yr⁻¹                         | $9.627044 \times 10^{-7}$         |
| Decay constant of Fe                                   | $\lambda_{Fe}$                      | yr⁻¹                         | $4.620781 \times 10^{-7}$         | yr⁻¹                         | $4.620781 \times 10^{-7}$         |
| Thermal expansivity of olivine                         | $\alpha$                            | K⁻¹                          | $3.8 \times 10^{-5}$              | K⁻¹                          | $3.8 \times 10^{-5}$              |
| Compressibility                                        | $\beta$                             | Pa⁻¹                         | $1.82 \times 10^{-6}$             | Pa⁻¹                         | $1.82 \times 10^{-6}$             |
| Molar volume of Fayalite                               | $V_{m,Fa}$                          | m³/mol                       | $46.39 \times 10^{-6}$            | -                            | -                                 |
| Specific heat capacity at constant pressure (Fayalite) | $c_p$                               | $J\cdot K^{-1}\cdot kg^{-1}$ | varying [~700,~1250]              | $J\cdot K^{-1}\cdot kg^{-1}$ | 2100                              |
| Specific heat capacity at volume (Fayalite)            | $c_v$                               | $J\cdot K^{-1}\cdot kg^{-1}$ | varying [~700,~1250]              | $J\cdot K^{-1}\cdot kg^{-1}$ | 2100                              |
| Heating                                                | $Q_{rad}$                           | W·m⁻³                        |                                   | J·m⁻³                        | -                                 |
| Source term                                            | $S$                                 | K·s⁻¹·kg⁻¹                   | -                                 | K·kg⁻¹                       | -                                 |








|                                 | **Crank–Nicolson (Code 1)**                                                                                                                                                                                                                                     | **Method of Lines (Code 2)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Discretization Approach**     | Fully implicit finite difference (CN) in time and space                                                                                                                                                                                                         | Semi-discrete: finite difference in space, ODE in time integrated using solve_ivp                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Thermal Equation Form**       | $$T_{i}^{n+1}(1 + 2 \alpha) + T_{i+1}^{n+1}(- \alpha - \beta_{i}) + T_{i-1}^{n+1}(\beta_{i} - \alpha) = T_{i}^{n}(1 - 2 \alpha) + T_{i+1}^{n}(\alpha + \beta_{i}) + T_{i-1}^{n}(\alpha - \beta_{i}) + S\Delta{t}$$<br><br>$$A\cdot T^{n+1} = B\cdot T^{n} + C$$ | $$<br>\frac{dT_{i}}{dt} = <br>\begin{cases}<br>3\kappa\Big(\frac{2T_{1} - 2T_{0}}{(\Delta{r})^2}\Big) + S_{0} & \text{if } r = 0 \\<br>\kappa \Big[\frac{T_{i+1} + T_{i-1} - 2T_{i}}{(\Delta{r})^{2}} + \frac{2}{r_{i}}\Big(\frac{T_{i+1} - T_{i - 1}}{2(\Delta{r})}\Big)\Big] + S_{i} & \text{if } 0 < r < R \\<br>\frac{dT}{dt} = 2\kappa \Big[ \frac{(T_{N-1} - T_{N})}{(\Delta{r})^2} + \frac{e \sigma (T_{surf}^{4} - T_{neb}^{4})}{\kappa_c}\Big(\frac{1}{\Delta{r}} + \frac{1}{R}  \Big) \Big] + S_{N} & \text{if } r = R<br>\end{cases}<br>$$ |
| **Temporal Integration**        | Linear system solve at each step: $A \cdot T_{new} = B \cdot T_{old} + b$ (CN scheme, implicit)                                                                                                                                                                 | Solves `dT/dt = RHS` using `solve_ivp(method='BDF')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Heat Source Q(t)Q(t)**        | Based on $^{26}$Al + $^{60}$Fe decay with offset 2.85 Myr                                                                                                                                                                                                       | Similar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Decay Constants & Energies**  | Same for both                                                                                                                                                                                                                                                   | Same for both                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Mass Fractions & Abundances** | Same for both                                                                                                                                                                                                                                                   | Same for both                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Boundary at Center r=0**      | Symmetric (Neumann): fixed via matrix `A[0,0] = 1`                                                                                                                                                                                                              | Assumed symmetric. Central difference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Boundary at Surface r=R**     | Radiative boundary condition: $-k \frac{\partial T}{\partial r} = \varepsilon\sigma(T^4 - T_{neb}^4)$                                                                                                                                                           | Radiative boundary condition: $-k \frac{\partial T}{\partial r} = \varepsilon\sigma(T^4 - T_{neb}^4)$                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Time Units**                  | Years                                                                                                                                                                                                                                                           | Years                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Implementation**              | Requires solving a matrix at each step                                                                                                                                                                                                                          | relies on solver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |


###### CN themal equation:

$$
\alpha = \frac{\Delta{t}\kappa}{2(\Delta{r}^{2})} \quad,\quad \beta_{i} = \frac{\Delta{t}\kappa}{2r_{i}\Delta{r}} \quad,\quad S\Delta{t} = \frac{Q_{rad,i}(\Delta{t})}{\rho c_{v}}
$$

$$
T_{i}^{n+1}(1 + 2 \alpha) + T_{i+1}^{n+1}(- \alpha - \beta_{i}) + T_{i-1}^{n+1}(\beta_{i} - \alpha) = T_{i}^{n}(1 - 2 \alpha) + T_{i+1}^{n}(\alpha + \beta_{i}) + T_{i-1}^{n}(\alpha - \beta_{i}) + S\Delta{t}
$$

$$
A\cdot T^{n+1} = B\cdot T^{n} + C
$$

A, B and C are tridiagonal matrix





Difference in parameters


| **Quantity**                                           | **Symbol**                          | **Units(Ghosh et al 1998)**  | **Value(Ghosh et al 1998)**       | **Units(my model)**          | **Formula(my model)**                                                                             | **Value(my model)**               | **Units(Shehzade's model)**  | **Value(Shehzade's model)**       |
| :----------------------------------------------------- | :---------------------------------- | :--------------------------- | :-------------------------------- | :--------------------------- | :------------------------------------------------------------------------------------------------ | :-------------------------------- | :--------------------------- | :-------------------------------- |
| Compressional wave                                     | $V_p$                               | --                           | --                                | km/s                         | -                                                                                                 | 7.61                              | -                            | -                                 |
| Thermal diffusivity                                    | $\kappa$                            | m²/s                         | (value not given)                 | m²/yr                        | $-1.67 + 2.1 \cdot V_p$                                                                           | 45.16208136                       | -                            | -                                 |
| Thermal Conductivity                                   | k                                   | $W m^{-1} K^{-1}$            | (value not given)                 | $W m^{-1} K^{-1}$            | -                                                                                                 | varying [~17.2, ~30.72]           | $W m^{-1} K^{-1}$            | 1199.1888                         |
| Emissivity                                             | $e$                                 | -                            | 0.8                               | -                            | -                                                                                                 | 0.8                               | -                            | 0.8                               |
| Stefan–Boltzmann constant                              | $\sigma$                            | W·m⁻²·K⁻⁴                    | 5.67037442e−8                     | W·m⁻²·K⁻⁴                    | -                                                                                                 | 5.67037442e−8                     | W·m⁻²·K⁻⁴                    | 5.67037442e−8                     |
| Initial temperature                                    | $T_{neb}$                           | K                            | 292                               | K                            | -                                                                                                 | 292                               | K                            | 292                               |
| Avogadro number                                        | $N_A$                               | --                           | --                                | mol⁻¹                        | -                                                                                                 | $6.022 \times 10^{23}$            | mol⁻¹                        | $6.022 \times 10^{23}$            |
| Density of H-chondrite                                 | $\rho$                              | kg·m⁻³                       | 3500                              | kg·m⁻³                       | -                                                                                                 | 3500                              | kg·m⁻³                       | 3500                              |
| Al abundance                                           | $Al_{abnds}$                        | %                            | 1.13                              | %                            | -                                                                                                 | 1.13                              | %                            | 1.13                              |
| Ratio of $^{26}\text{Al}$                              | $^{26}\text{Al}$ / $^{27}\text{Al}$ | -                            | $5 \times 10^{-5}$                | -                            | -                                                                                                 | $5 \times 10^{-5}$                | -                            | $5 \times 10^{-5}$                |
| Molar mass of Al                                       | $M_{Al}$                            | kg·mol⁻¹                     | 0.026981538                       | kg·mol⁻¹                     | $Al_{abnds} \cdot \rho \cdot \frac{{}^{26}Al}{{}^{27}Al} \cdot \frac{N_A}{M_{Al}}$                | 0.026981538                       | kg·mol⁻¹                     | 0.027                             |
| Atom density of Al                                     | $A_{Al}$                            | atoms·m⁻³                    | $4.413575 \times 10^{22}$         | atoms·m⁻³                    | -                                                                                                 | $4.413575 \times 10^{22}$         | atoms·m⁻³                    | $4.410557 \times 10^{22}$         |
| Fe abundance                                           | $Fe_{abnds}$                        | %                            | 24                                | %                            | -                                                                                                 | 24                                | %                            | 24                                |
| Ratio of $^{20}\text{Fe}$                              | $^{60}\text{Fe}$ / $^{56}\text{Fe}$ | -                            | $1 \times 10^{-8}$                | -                            | -                                                                                                 | $1 \times 10^{-8}$                | -                            | $1 \times 10^{-8}$                |
| Molar mass of Fe                                       | $M_{Fe}$                            | kg·mol⁻¹                     | 0.05584                           | kg·mol⁻¹                     | $Fe_{abnds} \cdot \rho \cdot \frac{{}^{60}Fe}{{}^{56}Fe} \cdot \frac{N_A}{M_{Fe}}$                | 0.05584                           | kg·mol⁻¹                     | 0.056                             |
| Atom density of Fe                                     | $A_{Fe}$                            | atoms·m⁻³                    | $9.058882 \times 10^{19}$         | atoms·m⁻³                    | -                                                                                                 | $9.058882 \times 10^{19}$         | atoms·m⁻³                    | $9.033 \times 10^{19}$            |
| Half life of $^{26}\text{Al}$                          | $t_{0.5,Al}$                        | Myr                          | 0.72                              | Myr                          | -                                                                                                 | 0.72                              | Myr                          | 0.72                              |
| Half life of $^{60}\text{Fe}$                          | $t_{0.5,Fe}$                        | Myr                          | 1.5                               | Myr                          | -                                                                                                 | 1.5                               | Myr                          | 1.5                               |
| Energy per atom of Al                                  | $Q_{Al}$                            | J                            | $3 \cdot 1.60218 \times 10^{-13}$ | J                            | -                                                                                                 | $3 \cdot 1.60218 \times 10^{-13}$ | J                            | $3 \cdot 1.60218 \times 10^{-13}$ |
| Energy per atom of Fe                                  | $Q_{Fe}$                            | J                            | $3 \cdot 1.60218 \times 10^{-13}$ | J                            | $\log(2) / t_{0.5,Al}$                                                                            | $3 \cdot 1.60218 \times 10^{-13}$ | J                            | $3 \cdot 1.60218 \times 10^{-13}$ |
| Decay constant of Al                                   | $\lambda_{Al}$                      | ye⁻¹                         | $9.627044 \times 10^{-7}$         | ye⁻¹                         | $\log(2) / t_{0.5,Fe}$                                                                            | $9.627044 \times 10^{-7}$         | yr⁻¹                         | $9.627044 \times 10^{-7}$         |
| Decay constant of Fe                                   | $\lambda_{Fe}$                      | yr⁻¹                         | $4.620781 \times 10^{-7}$         | yr⁻¹                         | -                                                                                                 | $4.620781 \times 10^{-7}$         | yr⁻¹                         | $4.620781 \times 10^{-7}$         |
| Thermal expansivity of olivine                         | $\alpha$                            | K⁻¹                          | $3.8 \times 10^{-5}$              | K⁻¹                          | -                                                                                                 | $3.8 \times 10^{-5}$              | K⁻¹                          | $3.8 \times 10^{-5}$              |
| Compressibility                                        | $\beta$                             | Pa⁻¹                         | $1.82 \times 10^{-6}$             | Pa⁻¹                         | -                                                                                                 | $1.82 \times 10^{-6}$             | Pa⁻¹                         | $1.82 \times 10^{-6}$             |
| Molar volume of Fayalite                               | $V_{m,Fa}$                          | m³/mol                       | $46.39 \times 10^{-6}$            | m³/mol                       | $172.76 - 3.4055 \cdot 10^{-3}T + 2.2411 \cdot 10^{-5}T^2 - 3.6299 \cdot 10^{6}T^{-2}$            | $46.39 \times 10^{-6}$            | -                            | -                                 |
| Specific heat capacity at constant pressure (Fayalite) | $c_p$                               | $J\cdot K^{-1}\cdot kg^{-1}$ | varying [~700,~1250]              | $J\cdot K^{-1}\cdot kg^{-1}$ | $c_p - (T \cdot V_{m,Fa} \cdot \alpha^2 / \beta)$                                                 | varying [~700,~1250]              | $J\cdot K^{-1}\cdot kg^{-1}$ | 2100                              |
| Specific heat capacity at volume (Fayalite)            | $c_v$                               | $J\cdot K^{-1}\cdot kg^{-1}$ | varying [~700,~1250]              | $J\cdot K^{-1}\cdot kg^{-1}$ | $A_{Al} \lambda_{Al} Q_{Al} e^{-\lambda_{Al} t} + A_{Fe} \lambda_{Fe} Q_{Fe} e^{-\lambda_{Fe} t}$ | varying [~700,~1250]              | $J\cdot K^{-1}\cdot kg^{-1}$ | 2100                              |
| Heating                                                | $Q_{rad}$                           | W·m⁻³                        |                                   | W·m⁻³                        | $Q_{rad} / (\rho \cdot c_v)$                                                                      |                                   | J·m⁻³                        | -                                 |
| Source term                                            | $S$                                 | K·s⁻¹·kg⁻¹                   | -                                 | K·s⁻¹·kg⁻¹                   |                                                                                                   | -                                 | K·kg⁻¹                       | -                                 |
