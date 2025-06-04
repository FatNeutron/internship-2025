
> [!NOTE]
> This file was written in obsidian and synced through GitHub, so some format may not load properly!!!
> 
> **GitHub app** does not load the format properly!!!


**Things to do:** 

- [x] read thesis by Shehzade Manzoor Khan.
	- [ ] learn the methods used.
		- [x] Crank-Nicolson method.
		- [ ] Method of lines.
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

So the our equation simplifies to following 1D heat equation,

##### 1D heat equation:
$$\frac{\partial{T}}{\partial{t}} = \frac{1}{R^{2}}\frac{\partial}{\partial{R}}\Big(R^{2} \kappa \frac{\partial{T}}{\partial{R}}\Big) + \frac{Q_{rad}}{\rho c_{v}}$$

| Symbol                                                                                              | Meaning                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $T(R, t)$                                                                                           | Temperature as a function of **radial distance** $R$ and **time** $t$                                                                                    |
| $t$                                                                                                 | Time (seconds, or years in planetary models)                                                                                                             |
| $R$                                                                                                 | Radial coordinate from the planet’s center (meters)                                                                                                      |
| $\frac{\partial T}{\partial t}$                                                                     | Rate of temperature change with time at radius $R$                                                                                                       |
| $\kappa(R, T)$                                                                                      | **Thermal conductivity** (W/m·K) — may depend on radius or temperature                                                                                   |
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

### Crank-Nicolson method 

