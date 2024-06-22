# SatelliteTemperature

## Equations of heat flux impinging on a satellite in low earth orbit

Much of the Python code here is adapted from [Rickman, NASA 2014](https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf). The file 'ThermalAnalysis.py' contains the working functions. File 'EquationVerification.py' duplicates several of the graphs in the Rickman presentation. For instance, compare the graph below to the graphs on page 131 and 132 of the presentation.

![](./media/nadirFlux.svg)

However, the code extends the equations to consider emissivity at different wavelengths of light. The graph below shows the spectra of light emitted by the sun and by the earth. It is a linear plot where the two curves have been arbitrarily scaled so it can be seen that the sun emits mostly visible light, and the earth mostly emits long wave infrared light (see https://en.wikipedia.org/wiki/Black_body and https://en.wikipedia.org/wiki/Ultraviolet_catastrophe).

![](./media/sun-earthFluxLin.svg)

A logarithmic graph such as below is necessary to really compare the magnitudes of the two emission spectra. The earth emission is about 100x lower than the sun.

![](./media/sun-earthFluxLog.svg)

When light hits an object, the light will be reflected, transmitted, or absorbed. For conservation of energy, the sum of those three must equal one. Transparent objects such as glass will reflect a small part of the light, and transmit almost all of the remainder. They do not absorb very much light. An opaque material such as aluminum does not transmit any of the light. All of it is reflected or absorbed, and if the fraction reflected is R, then by conservation of energy, A = 1-R is absorbed and heats up the aluminum. Interestingly, R depends on the wavelength. For instance, black anodized aluminum absorbs visible light, but it reflects long wave infrared. 

(Kirchhoff's Law of thermal radiation)[https://en.wikipedia.org/wiki/Kirchhoff%27s_law_of_thermal_radiation] states that the emissivity (ε) of an object (its ability to emit light) is equal to its absorptivity. So, ε = A = 1-R. But remember that R is wavelength dependant. Some people like to distinguish short wave absorptivity (α) from long wave emissivity (ε). I rather dislike that because they are exactly the same thing. Black anodized aluminum is about the hottest object you will ever find laying out in the sun because it absorbs all the visible light from the sun, but because it is reflective in thermal infrared, it cannot emit that heat, so it gets very hot. Teflon is the opposite. It reflects most visible light (it is white), but Teflon absorbs much of the thermal infrared, so it is a reasonably good emitter at temperatures we normally encounter on Earth.

## Multilayer insulation

## Temperature of a satellite

## Time dependant temperature change
