# -*- coding: utf-8 -*-
'''
Created on Wed Apr 26 11:29:59 2023

@author: MarcMignard
'''
#ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρσςτυφχψωάέήϊίόύϋώΆΈΉΊΌΎΏ±≥≤ΪΫ÷≈°√ⁿ²

#from https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf

import numpy as np
import matplotlib.pyplot as plt
import ThermalAnalysis as ta


##########################################################################
###    test plots to compare with same plots in reference
###    https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf
##########################################################################

theta = np.linspace(0,360,73)
heightOrbit = 408e3

#zenith facing side
plt.figure(figsize=(8,3),dpi=150)
plt.suptitle('Variation of heating to zenith-facing surface')
plt.subplot(121)
beta = 0
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'zenith'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'zenith'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'zenith')*np.ones(theta.shape),'g:',label='Earth glow')
plt.text(50,1200,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.xlim([0,360])
plt.ylim([-10,1400])
#plt.legend()
plt.subplot(122)
beta = 60
plt.text(50,1200,f'beta={beta:.0f}deg')
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'zenith'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'zenith'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'zenith')*np.ones(theta.shape),'g:',label='Earth glow')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.xlim([0,360])
plt.ylim([-10,1400])
plt.legend()
plt.show

#nadir facing side (direct solar is slightly off compared to reference for beta=0)
plt.figure(figsize=(8,6),dpi=150)
plt.suptitle('Variation of heating to nadir-facing surface (pg 131-132)')
plt.subplot(221)
beta = 0
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'nadir'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'nadir'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'nadir')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(5,600,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.xlim([0,360])
plt.ylim([0,700])
#plt.legend()
plt.subplot(222)
beta = 60
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'nadir'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'nadir'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'nadir')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(5,600,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.xlim([0,360])
plt.ylim([0,700])
plt.legend()
plt.subplot(223)
beta = 75
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'nadir'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'nadir'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'nadir')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(5,600,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.xlim([0,360])
plt.ylim([0,700])
plt.legend()
#plt.savefig('./media/nadirFlux.svg', bbox_inches='tight')
plt.show

#forward facing side
plt.figure(figsize=(8,3),dpi=150)
plt.suptitle('Variation of heating to forward-facing surface (pg 133)')
plt.subplot(121)
beta = 0
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'forward'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'forward'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'forward')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(5,600,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.xlim([0,360])
plt.ylim([0,1400])
#plt.legend()
plt.subplot(122)
beta = 60
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'forward'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'forward'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'forward')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(5,600,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.xlim([0,360])
plt.ylim([0,1400])
plt.legend()
plt.show

#aft facing side
plt.figure(figsize=(8,3),dpi=150)
plt.suptitle('Variation of heating to aft-facing surface (pg 134)')
plt.subplot(121)
beta = 0
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'aft'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'aft'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'aft')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(200,1200,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.xlim([0,360])
plt.ylim([0,1400])
#plt.legend()
plt.subplot(122)
beta = 60
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'aft'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'aft'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'aft')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(5,1200,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.xlim([0,360])
plt.ylim([0,1400])
plt.legend()
plt.show

#north facing side
plt.figure(figsize=(8,3),dpi=150)
plt.suptitle('Variation of heating to north-facing surface (pg 135)')
plt.subplot(121)
beta = 0
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'north'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'north'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'north')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(200,1200,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.xlim([0,360])
plt.ylim([0,1400])
#plt.legend()
plt.subplot(122)
beta = -60
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'north'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'north'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'north')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(50,1200,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.xlim([0,360])
plt.ylim([0,1400])
plt.legend()
plt.show

#south facing side
plt.figure(figsize=(8,3),dpi=300)
plt.suptitle('Variation of heating to south-facing surface (pg 136)')
plt.subplot(121)
beta = 0
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'south'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'south'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'south')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(200,1200,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.xlim([0,360])
plt.ylim([0,1400])
#plt.legend()
plt.subplot(122)
beta = 60
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,'south'),'b',label='Solar')
plt.plot(theta,ta.earthAlbedoFlux(heightOrbit,theta,beta,'south'),'r',label='Albedo')
plt.plot(theta,ta.earthGlowFlux(heightOrbit,'south')*np.ones(theta.shape),'g',label='Earth glow')
plt.text(50,1200,f'beta={beta:.0f}deg')
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.xlim([0,360])
plt.ylim([0,1400])
plt.legend()
plt.show

