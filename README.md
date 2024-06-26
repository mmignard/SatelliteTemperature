# SatelliteTemperature

## Equations of heat flux impinging on a satellite in low earth orbit

Much of the Python code here is adapted from [Rickman, NASA 2014](https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf). The file [ThermalAnalysis.py](https://github.com/mmignard/SatelliteTemperature/blob/main/ThermalAnalysis.py) contains the working functions. File [EquationVerification.py](https://github.com/mmignard/SatelliteTemperature/blob/main/EquationVerification.py) duplicates several of the graphs in the Rickman presentation. For instance, compare the graph below to the graphs on page 131 and 132 of the presentation. The file [ThermalAnalysisTest.py](https://github.com/mmignard/SatelliteTemperature/blob/main/ThermalAnalysisTest.py) was used to generate the other plots shown in this readme.

![](./media/nadirFlux.svg)

However, the code extends the equations to consider emissivity at different wavelengths of light. The graph below shows the spectra of light emitted by the sun and by the earth. It is a linear plot where the two curves have been arbitrarily scaled so it can be seen that the sun emits mostly visible light, and the earth mostly emits long wave infrared light (see https://en.wikipedia.org/wiki/Black_body and https://en.wikipedia.org/wiki/Ultraviolet_catastrophe).

![](./media/sun-earthFluxLin.svg)

A logarithmic graph such as below is necessary to really compare the magnitudes of the two emission spectra. The earth emission is about 100x lower than the sun.

![](./media/sun-earthFluxLog.svg)

## Temperature of a satellite

When light hits an object, the light will be reflected, transmitted, or absorbed. For conservation of energy, the sum of those three must equal one. Transparent objects such as glass will reflect a small part of the light, and transmit almost all of the remainder. They do not absorb very much light. An opaque material such as aluminum does not transmit any of the light. All of it is reflected or absorbed, and if the fraction reflected is R, then by conservation of energy, A = 1-R is absorbed and heats up the aluminum. Interestingly, R depends on the wavelength. For instance, black anodized aluminum absorbs visible light, but it reflects long wave infrared. 

[Kirchhoff's Law of thermal radiation](https://en.wikipedia.org/wiki/Kirchhoff%27s_law_of_thermal_radiation) states that the emissivity (ε) of an object (its ability to emit light) is equal to its absorptivity. So, ε = A = 1-R. But remember that R is wavelength dependant. Some people like to distinguish short wave absorptivity (α) from long wave emissivity (ε). I rather dislike that because they are the exact same thing. Kirchhoff's Law makes intuitive sense. If the absorbed and emitted light is different, then there is a net heat flow and the temperature of the object will change until it eventually settles into a steady state where absorbed and emitted light are equal.

Black anodized aluminum is about the hottest object you will ever find laying out in the sun because it absorbs all the visible light from the sun. But because aluminum is reflective in thermal infrared, it cannot emit that heat so it gets very hot. Teflon is the opposite. It reflects most visible light (it is white), but Teflon absorbs much of the thermal infrared, so it is a reasonably good emitter at temperatures we normally encounter on Earth. See table 5.1 on page 62 of [Small Satellite Thermal Modeling Guide](https://apps.dtic.mil/sti/pdfs/AD1170386.pdf) for examples of $&alpha;$ and $&epsilon;$

Multiplying the area of each side of a satellite by the heat flux for that side, then summing the results over all six sides of a rectangular satellite (in this example a 6U cubesat size), we get the total heat flux incident on the satellite. The results are shown below for several β angles (β is the inclination of the satellite orbit plane with respect to the sun). I've made some assumptions that the satellite has its narrow ended pointing to the Earth, and the long skinny side is forward (in the direction of travel).

![](./media/satelliteHeatFlux.svg)

To estimate the temperature of the satellite we can write a heat flux balance equation: $\dot Q_{out} = \dot Q_{in} + P_{gen}$. The graph above gives the value for $\dot Q_{in}$. The power generated locally by electronics is $P_{gen}$, and the only outlet for heat in orbit is through radiation, so $\dot Q_{out} = &epsilon; k_{sb} AT^4$ where $&epsilon;$ is the emissivity, $k_{sb}$ is the Stephan-Boltzman constant, A is the surface area of the satellite, and T is the temperature. I ignore the small heat flux due to the background temperature of space at 3K since it is microwatts. To get temperature, solve for T in $&epsilon; k_{sb} AT^4 = \dot Q_{in} + P_{gen}$. The result is shown in the figure below.

![](./media/satelliteTemperature01.svg)

## Time dependant temperature change
The previous image showed what the satellite temperature would be if it was held in position at each point in its orbit long enough to thermally equilibrate. Of course the satellite is constantly moving, so the temperature will continuously change. We can estimate the time-dependent temperature using the formula
$$&rho; V C_p \frac{\partial T}{\partial t} = \dot Q_{in} + P_{gen} - ε_L k_{sb} A T^4$$

$$T = \frac{1}{&rho; V C_p}\int{\big(\dot Q_{in} + P_{gen} - ε_L k_{sb} A T^4 \big) dt}$$
where $&rho;$ = density, $C_p$ = specific heat capacity (J/(m^3ˑK)), V = volume, A = surface area, $k_{sb}$ = Stefan-Boltzmann constant (W/(m^2ˑK^4)), and $P_{gen}$ is the power generated locally in the satellite

The value of 'T' is what we want to solve for, and it appears on both sides of the equation. Just assume an initial value of T for the first iteration, and after a few steps of plugging the calculated value of T back into $T^4$ it rapidly converges.<br>
This simulation uses values of $C_p = 230J/(kgˑK)$, $\rho = 0.7g/cm^3$, which assumes that 1/4 the volume is aluminum, and the rest is vacuum.<br>

Some tables of specific heat for various materials are here:<br>
- [Engineering Toolbox](https://www.engineeringtoolbox.com/specific-heat-capacity-d_391.html)
- [Engineers Edge-metals](https://www.engineersedge.com/materials/specific_heat_capacity_of_metals_13259.htm)
- [Engineers Edge-nonmetals](https://www.engineersedge.com/heat_transfer/thermal_properties_of_nonmetals_13967.htm)

The image below shows the time-dependent temperature of a satellite. The lines labelled min & max are from the peaks in the previous image (with beta=0).

![](./media/satTimeTemp.svg)

## Multilayer insulation

Multilayer insulation (MLI) is commonly used on spacecraft. Below is an photo of the Mars Reconnaisance Orbiter showing its MLI (from [https://en.wikipedia.org/wiki/File:Mars_Reconnaissance_Orbiter_fully_assembled.jpg]())

![](./media/220px-Mars_Reconnaissance_Orbiter_fully_assembled.jpg)

Let's derive an expression for the temperature inside an enclosure completely wrapped. Assume the MLI is composed of two identical films with emissivity ε. Below is a diagram showing the energy balance.

![](./media/MLI_diagram.svg)

For the upper layer (facing the environment), there is a net flux of heat coming from something like the sun, $\dot Q_{in}$. For the lower film (facing inside toward the enclosure), there is a net flux of heat from the electronics inside the enclosure $\dot Q_{in}$. The following two equations describe this situation:

$$\dot Q_{in} + C {T_N}^4 = 2 C {T_0}^4$$

$$\dot Q_{out} + C {T_0}^4 = 2 C {T_N}^4$$

Where $C = ε k_{sb} A$. The solutions for this are fairly easy to determine:

$${T_0}^4 = \frac {2 Q_{in} + Q_{out}}{3 C}$$

$${T_N}^4 = \frac {Q_{in} + 2 Q_{out}}{3 C}$$

What if we have many films N, N-1, N-2, ... 0? It is harder to solve N equations in N unknowns by hand. For instance, with four films, the equations are:

$$\dot Q_{in} + C {T_1}^4 = 2 C {T_0}^4$$

$$C {T_0}^4 + C {T_2}^4 = 2 C {T_1}^4$$

$$C {T_1}^4 + C {T_N}^4 = 2 C {T_2}^4$$

$$\dot Q_{out} + C {T_2}^4 = 2 C {T_N}^4$$

Using sympy (symbolic python) as shown in file [ThermalAnalysisTest.py](https://github.com/mmignard/SatelliteTemperature/blob/main/ThermalAnalysisTest.py), the solutions are:

$${T_0}^4 = \frac {4 Q_{in} + Q_{out}}{5 C}$$

$${T_1}^4 = \frac {3 Q_{in} + 2 Q_{out}}{5 C}$$

$${T_2}^4 = \frac {2 Q_{in} + 3 Q_{out}}{5 C}$$

$${T_N}^4 = \frac {Q_{in} + 4 Q_{out}}{5 C}$$

The only temperature we care about is the last one near the enclosure, and for $T_N$ when N is large, then

$${T_N}^4 = \frac {Q_{in} + N Q_{out}}{(N+1) C}$$

$$T_N \approx \sqrt[4]{\frac {Q_{out}}{ε k_{sb} A}}$$

The units of $\dot Q_{in}$ and $\dot Q_{out}$ are W, and the units of C are W/K^4. A 6U satellite with 0.244m^ area dissipating 50W that is wrapped in MLI will be about -14°C when it is in either full sun or it is in eclipse. 


