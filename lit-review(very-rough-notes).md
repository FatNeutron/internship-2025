
**Things to do:** 

- [x] read thesis by Shehzade Manzoor Khan.
	- [ ] learn the methods used.
- [ ] read paper by Amitabha Ghosh.

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
$^{24}\text{Mg}$ is most abundant stable.
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

Formed just after few myr after the solar system formation with rapid accretion.(within 1-2 myr after [CAIs](https://en.wikipedia.org/wiki/Calcium%E2%80%93aluminium-rich_inclusion))

HED (howardites, eucrites, and diogenites) meteorites are considered to be originated from Vesta. Diogenites are derived from the lower crust or upper mantle, eucrites comes from basaltic surface flows or shallow intrusions.

Heat released from $^{26}\text{Al}$ decay was enough for partial to extensive melting which lead to the formation of core(metallic iron towards center & silicate mantle and crust).


## Modeling


> [!NOTE] 3D heat equation
> $$\frac{\partial T}{\partial t} = \frac{\kappa}{\rho c_v} \left[
\frac{1}{R^2} \frac{\partial}{\partial R} \left( R^2 \frac{\partial T}{\partial R} \right) + \frac{1}{R^2 \sin \theta} \frac{\partial}{\partial \theta} \left( \sin \theta \frac{\partial T}{\partial \theta} \right) + \frac{1}{R^2 \sin^2 \theta} \frac{\partial^2 T}{\partial \phi^2}\right] + \frac{Q_{\text{rad}}}{\rho c_v} $$

For modelling we assume spherical symmetry, which means that there are no angular dependencies so the angular terms become 0.

So the out equation simplifies to following

> [1D heat equation]  
>$$\frac{\partial{T}}{\partial{t}} = \frac{1}{R^{2}}\frac{\partial}{\partial{R}}\Big(R^{2} \kappa \frac{\partial{T}}{\partial{R}}\Big) + \frac{Q_{rad}}{\rho c_{v}}$$

| Symbol                                                                                                  | Meaning                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \( T = T(R, t) \)                                                                                       | Temperature as a function of **radial distance** \( R \) and **time** \( t \)                                                                                |
| \( t \)                                                                                                 | Time (seconds, or years in planetary models)                                                                                                                 |
| \( R \)                                                                                                 | Radial coordinate from the planet’s center (meters)                                                                                                          |
| \( \frac{\partial T}{\partial t} \)                                                                     | Rate of temperature change with time at radius \( R \)                                                                                                       |
| \( \kappa = \kappa(R, T) \)                                                                             | **Thermal conductivity** (W/m·K) — may depend on radius or temperature                                                                                       |
| \( \frac{\partial T}{\partial R} \)                                                                     | Radial temperature gradient (how temperature changes with depth)                                                                                             |
| \( \frac{1}{R^2} \frac{\partial}{\partial R} \left( R^2 \kappa \frac{\partial T}{\partial R} \right) \) | **Radial heat conduction term** — accounts for heat flowing in/out of a spherical shell at radius \( R \), including the increasing surface area with radius |
| \( Q_{\text{rad}} \)                                                                                    | **Volumetric internal heat production rate** (W/m³), e.g., from radioactive decay of U, Th, K in planetary mantles                                           |
| \( \rho \)                                                                                              | Density of the material (kg/m³)                                                                                                                              |
| \( c_v \)                                                                                               | **Specific heat capacity at constant volume** (J/kg·K) — amount of energy needed to raise the temperature of a unit mass by 1 K                              |
| \( \frac{Q_{\text{rad}}}{\rho c_v} \)                                                                   | Temperature increase due to internal heating, normalized per unit mass and heat capacity                                                                     |

