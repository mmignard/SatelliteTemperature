# -*- coding: utf-8 -*-
'''
Created on Wed Apr 26 11:29:59 2023

@author: MarcMignard
ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρσςτυφχψωάέήϊίόύϋώΆΈΉΊΌΎΏ±≥≤ΪΫ÷≈°√ⁿ²

equations from https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf
'''

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

##########################################################################
###    Verify planck() equation in ThermalAnalysis.py
###    
##########################################################################

#this matches the first figure at https://en.wikipedia.org/wiki/Planck%27s_law
wavelength = np.linspace(0.1,3,1000)*1e-6
plt.figure(figsize=(5,3.5),dpi=150)
for T in [5000,4000,3000]:
#for T in [300,252]:
    #/1e12 is to get kW/nm
    plt.plot(wavelength*1e6,ta.planck(wavelength,T)/1e12,label='T={:.0f}K'.format(T))
plt.grid(True)
plt.xlabel('wavelength (um)')
plt.ylabel('radiance (kW/(sr·m^2·nm))')
#plt.xlim([0,360])
#plt.xticks(np.arange(0,390,30))
#plt.ylim([0,1400])
plt.legend()
plt.show    
       
##########################################################################
###    Verify irradianceSunFromEarth() equation in ThermalAnalysis.py
###    
##########################################################################
#this is the same as the figure on page 13 of 
#https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf
plt.figure(figsize=(5,3.5),dpi=150)
for T in [5777,4000,3000]:
    plt.plot(wavelength*1e9,ta.irradianceSunFromEarth(wavelength,T)/1e9,label=f'T={T:.0f}K')
plt.grid(True)
plt.xlabel('wavelength (nm)')
plt.ylabel('radiance (W/(m^2·nm))')
#plt.xlim([0,360])
#plt.xticks(np.arange(0,390,30))
#plt.ylim([0,1400])
plt.legend()
plt.show  
  
plt.figure(figsize=(5,3.5),dpi=150)
for T in [300,252]:
    plt.plot(wavelength*1e9,ta.planck(wavelength,T)/1e9,label=f'T={T:.0f}K')
plt.grid(True)
plt.xlabel('wavelength (nm)')
plt.ylabel('radiance (W/(m^2·nm))')
#plt.xlim([0,360])
#plt.xticks(np.arange(0,390,30))
#plt.ylim([0,1400])
plt.legend()
plt.show    

##########################################################################
###    Had to adjust the sun temperature from 5777 to 5930 to get
###    numerical integration of spectral flux to match number based
###    on qDot. This is odd because integration of irradianceSunFromEarth()
###    with 5777 works almost perfectly
##########################################################################
theta = np.linspace(0,360,73)
heightOrbit = 408e3

waves = np.linspace(0.2,20,900)*1e-6
sf0w = ta.sunFlux(heightOrbit,theta,0,1,waves,5930)
sf0 = np.sum(sf0w,axis=1)*(waves[1]-waves[0])
sf60w = ta.sunFlux(heightOrbit,theta,60,1,waves,5930)
sf60 = np.sum(sf60w,axis=1)*(waves[1]-waves[0])

#zenith facing side
plt.figure(figsize=(5,3.5),dpi=150)
plt.suptitle('Difference in flux with numerical integration')
beta = 0
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,1),label='beta={:.0f}deg'.format(beta))
plt.plot(theta,sf0,'--',label='beta={:.0f}deg'.format(beta))
beta = 60
plt.plot(theta,ta.sunFlux(heightOrbit,theta,beta,1),label='beta={:.0f}deg'.format(beta))
plt.plot(theta,sf60,'--',label='beta={:.0f}deg'.format(beta))
#plt.plot(theta,(1-sf60/ta.sunFlux(heightOrbit,theta,beta,1))*100,label='beta={:.0f}deg'.format(beta))
plt.grid(True)
plt.xlabel('orbit angle, theta (deg)')
plt.xlim([0,360])
plt.xticks(np.arange(0,390,90))
#plt.ylim([0,1400])
plt.xlabel('orbit angle, theta (deg)')
plt.ylabel('Incident flux (w/m^2)')
plt.legend()
plt.show

##########################################################################
###    Satellite temperature
###    
##########################################################################

heightOrbit = 400e3
print(f'period of satellite at an altitude of {heightOrbit/1000} km is {ta.orbitalPeriod(600e3+ta.radiusEarth)/60:.2f} minutes')

#Integrate irradianceSunFromEarth to get the total irradiance power of the sun 
#per square meter at the earth (qDotSol). The range of wavelength has to be from like 0.1um to 20um
w = np.linspace(0.2,30,1000)*1e-6
print(f'qDotSol = {ta.qDotSol:.1f} W/m^2')
print(f'flux density in earth orbit from the sun is {sum(ta.irradianceSunFromEarth(w,5777))*(w[1]-w[0]):.1f} W/m^2')

qDotEarth = ta.qDotSol*(1-ta.albedoEarth)/4 #IR heat flux from earth ~239 W/m^2
print(f'qDotEarth = {qDotEarth:.1f} W/m^2')
#the flux density below can't possibly be right
print(f'flux density in earth orbit from the earth is {sum(ta.irradianceEarthFromSat(w,255,heightOrbit))*(w[1]-w[0]):.0f} W/m^2')
      #255 earth temperature from pg 64 of https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf


