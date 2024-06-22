# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:26:18 2023

@author: MarcMignard
"""

import numpy as np

c = 2.99792458e8            #speed of light, m/s
h = 6.62607015e-34          #Planck constant, J·s
k = 1.380649e-23            #Boltzmann constant, J/K
ksb = 5.67e-8               #stefan-boltzmann constant, W/m^2/K^4
qDotSol = 1367              #heat flux of sun at earth, W/m^2
                            #varies from 1321 to 1423 depending on season
albedoEarth = 0.3           #albedo of earth    
radiusEarth = 6.37814e6     #radius of earth, m
radiusSun = 6.957e8
sunEarthDistance = 1.496e11
sunSolidAngleOnEarth = np.pi*(radiusSun/sunEarthDistance)**2
sunTemp = 5777              #blackbody temperature of the sun
earthTemp = 300             #blackbody temperature of the earth

def planck(w,T):
    '''
    return the spectral radiance in W/(sr·m^2·m) (last meter is for wavelength)
    '''
    return 2*h*c*c/np.power(w,5)/(np.exp(h*c/(w*k*T))-1)

def irradianceSunFromEarth(w,T):
    '''
    return the spectral irradiance of the sun in earth orbit in W/(m^2·m)
    as seen from earth, the solid angle of the sun per square meter is:
    '''
    sunSolidAngleOnEarth = np.pi*(radiusSun/sunEarthDistance)**2
    return sunSolidAngleOnEarth*planck(w,T)
#Integrate irradianceSunFromEarth to get the total irradiance power of the sun 
#per square meter at the earth (qDotSol). The range of wavelength has to be from like 0.2um to 20um
#w = np.linspace(0.2,20,1000)*1e-6
#sum(irradianceSunFromEarth(w,5777))*(w[1]-w[0])

def irradianceEarthFromSat(w,T,height):
    '''
    return the spectral irradiance of the earth in earth orbit in W/(m^2·m)
    as seen from a satellite, the solid angle of the earth per square meter is: xxx
    This is returning unreasonably large values--TODO: come back and find this bug
    '''
    earthSolidAngleOnSat = np.pi*(radiusEarth/height)**2
    return earthSolidAngleOnSat*planck(w,T)

def eclipseAngle(heightOrbit,beta):
    '''
    calculates the theta angle where eclipse starts. Beta and theta in radians, heightOrbit in m
    uses the global value of radiusEarth
    '''
    radical = ((radiusEarth/(radiusEarth+heightOrbit))**2-np.sin(beta)**2)/(np.cos(beta)**2)
    if (radical<0):
        retVal = 0
    else:
        retVal = np.pi-np.arcsin(np.sqrt(radical))
    return retVal
# beta = 0
# print('eclipse start = {:0.1f}, end = {:0.1f}'.format(eclipseAngle(400e3,np.pi/180*beta)*180/np.pi,(2*np.pi-eclipseAngle(400e3,np.pi/180*beta))*180/np.pi))

def criticalEclipseBeta(heightOrbit):
    '''
    returns value of beta (in degrees) where there is no longer an eclipse
    uses the global value of radiusEarth
    '''
    beta = np.arange(0,90,0.1)
    b = beta*np.pi/180
    radical = ((radiusEarth/(radiusEarth+heightOrbit))**2-np.sin(b)**2)/(np.cos(b)**2)
    return beta[np.argmax(radical<0)]
# criticalEclipseBeta(100e3)    
# criticalEclipseBeta(400e3)    
# criticalEclipseBeta(600e3)    

def sunFlux(heightOrbit,theta,beta,face,waves=0,sunT=sunTemp):
    '''
    Parameters
    ----------
    heightOrbit : float
        Height of satellite orbit above the earth in meters.
    theta : numpy array
        Position in degrees of satellite in its orbit.
        0 is directly between sun and earth.
        Varies from 0-360
    beta : float
        Angle in degrees between sun plane and orbit plane.
        Varies from -90 to +90, negative is south of sun, positive is north of sun.
    face : string
        Identifies which of the 6 faces of a cubic satellite to calculate flux for.
        'zenith' (sun facing at theta=beta=0)
        'nadir' (earth facing at theta=beta=0)
        'forward' side facing the forward direction of travel
        'aft' facing side
        'north' facing side
        'south' facing side
    waves : float or numpy array, optional
        If waves is a numpy array of wavelengths, then return the flux at each wavelength in waves.
        To do an accurate numerical integration to get total solar flux, need 1000 samples from 0.2um to 20um
        waves = np.linspace(0.2,20,1000)*1e-6
        A smaller number of wavelengths could be used with a nonlinear spacing
        If waves is not an array, or not provided, then return flux integrated across all wavelengths
        
    Returns
    -------
    qDot : numpy array
        Heat flux density from sun on one side of an earth orbiting satellite.
        If waves is an array, then qDot is an array of dimensions [theta.size,waves.size],
        otherwise qDot is flux integrated across all wavelengths
        Uses global values radiusEarth and qDotSol
        This is a fairly good approximation, but it assumes the sun's spectrum is
        a blackbody. It actually has some absorption bands from the sun's atmosphere.
    '''
    if (type(theta)!=np.ndarray):
        theta = np.array([theta])
    projection = np.zeros(theta.size)
    t = theta*np.pi/180
    b = beta*np.pi/180
    if face == 'zenith':
        i = (t<np.pi/2) | (t>3*np.pi/2)
        projection[i] = np.cos(t[i])*np.cos(b)
    elif face == 'nadir':
        eclipseStart = eclipseAngle(heightOrbit,b)
        if (eclipseStart<1): #for beta>70.3 deg, there is no eclipse, and function returns 0
            i = ((t>np.pi/2) & (t<3*np.pi/2)) #no eclipse but sun only on back side of earth
        else:
            eclipseEnd = 2*np.pi-eclipseStart
            i = ((t<eclipseStart) & (t>np.pi/2)) | ((t>eclipseEnd) & (t<3*np.pi/2))
        projection[i] = -np.cos(t[i])*np.cos(b) 
    elif face == 'forward':
        eclipseStart = eclipseAngle(heightOrbit,b)
        if (eclipseStart<1): #for beta>70.3 deg, there is no eclipse, and function returns 0
            i = ((t>np.pi) & (t<2*np.pi)) #no eclipse but sun only when approaching sun
        else:
            eclipseEnd = 2*np.pi-eclipseStart
            i = (t>eclipseEnd)
        projection[i] = np.cos(t[i]+np.pi/2)*np.cos(b)
    elif face == 'aft':
        eclipseStart = eclipseAngle(heightOrbit,b)
        if (eclipseStart<1): #for beta>70.3 deg, there is no eclipse, and function returns 0
            i = (t<np.pi) #no eclipse but sun only when receeding from sun
        else:
            i = (t<eclipseStart)
        projection[i] = np.cos(t[i]-np.pi/2)*np.cos(b)
    elif face == 'north':
        if (b<0):
            eclipseStart = eclipseAngle(heightOrbit,b)
            if (eclipseStart<1): #for beta>70.3 deg, there is no eclipse, and function returns 0
                i = (t>=0) #no eclipse, so north side always sees sun
            else:
                eclipseEnd = 2*np.pi-eclipseStart
                i = (t<eclipseStart) | (t>eclipseEnd)
            projection[i] = -np.sin(b)
    else: # presumably south
        if (b>=0):
            eclipseStart = eclipseAngle(heightOrbit,b)
            if (eclipseStart<1): #for beta>70.3 deg, there is no eclipse, and function returns 0
            #if np.isnan(eclipseStart): #for beta>70.3 deg, there is no eclipse, and function returns NaN
                i = (t>=0) #no eclipse, so south side always sees sun
            else:
                eclipseEnd = 2*np.pi-eclipseStart
                i = (t<eclipseStart) | (t>eclipseEnd)
            projection[i] = np.sin(b)
    if (type(waves)==np.ndarray):
        qDot = np.outer(projection,irradianceSunFromEarth(waves,sunT))
    else:
        qDot = qDotSol*projection
    return np.squeeze(qDot)

def perpFormFactor(heightOrbit):
    '''
    The shape of earth projected onto a vertical (perpendicular) surface in orbit.
    Used only for albedo reflection of the sun off the earth.
    uses global value radiusEarth
    '''
    radical = np.sqrt(1-(radiusEarth/(radiusEarth+heightOrbit))**2)
    retVal = 1/(2*np.pi)*(np.pi - 2*np.arcsin(radical) - np.sin(2*np.arcsin(radical)))
    return retVal

def albedoCorrection(albedo,xi):
    '''
    empirical correction from data between +/-30deg latitude
    xi is the angle (in radians) between the sun and the satellite
    cos(xi) = cos(theta)*cos(beta)
    '''
    retVal = albedo + 1.3798e-3*xi - 2.1793e-5*xi**2 + 6.0372e-8*xi**3 + 4.9115e-9*xi**4
    return retVal

def earthAlbedoFlux(heightOrbit,theta,beta,face,waves=0,sunT=sunTemp):
    '''
    Parameters
    ----------
    heightOrbit : float
        Height of satellite orbit above the earth in meters.
    theta : numpy array
        Position in degrees of satellite in its orbit.
        0 is directly between sun and earth.
        Varies from 0-360
    beta : float
        Angle in degrees between sun plane and orbit plane.
        Varies from -90 to +90, negative is south of sun, positive is north of sun.
    face : string
        Identifies which of the 6 faces of a cubic satellite to calculate flux for.
        'zenith' (sun facing at theta=beta=0)
        'nadir' (earth facing at theta=beta=0)
        'forward' side facing the forward direction of travel
        'aft' facing side
        'north' facing side
        'south' facing side
    waves : float or numpy array, optional
        If waves is a numpy array of wavelengths, then return the flux at each wavelength in waves.
        To do an accurate numerical integration to get total solar flux, need 1000 samples from 0.2um to 20um
        waves = np.linspace(0.2,20,1000)*1e-6
        A smaller number of wavelengths could be used with a nonlinear spacing
        If waves is not an array, or not provided, then return flux integrated across all wavelengths
        
    Returns
    -------
    qDot : numpy array
        Heat flux density on one side of an earth orbiting satellite from sun reflecting off earth.
        If waves is an array, then qDot is an array of dimensions [theta.size,waves.size],
        otherwise qDot is flux integrated across all wavelengths
        Uses global values radiusEarth, albedoEarth and qDotSol
        This is a fairly good approximation, but it assumes the sun's spectrum is
        a blackbody. It actually has some absorption bands from the sun's atmosphere, and
        the earth's reflection is not uniform in spectrum.
    '''

    if (type(theta)!=np.ndarray):
        theta = np.array([theta])
    projection = np.zeros(theta.size)
    t = theta*np.pi/180
    b = beta*np.pi/180
    xi = np.arccos(np.cos(t)*np.cos(b))
    albedo = albedoEarth*np.ones(theta.shape)
    #albedo = albedoCorrection(albedoEarth,xi)
    if face == 'zenith':
        projection[0] = 0 #never sees the earth reflection
    elif face == 'nadir':
        i = (xi<np.pi/2) | (xi>3*np.pi/2)
        projection[i] = albedo[i]*(radiusEarth/(radiusEarth+heightOrbit))**2*np.cos(xi[i])
    else: #forward, aft, north, south
        i = (xi<np.pi/2) | (xi>3*np.pi/2)
        projection[i] = albedo[i]*perpFormFactor(heightOrbit)*np.cos(xi[i])
    if (type(waves)==np.ndarray):
        qDot = np.outer(projection,irradianceSunFromEarth(waves,sunT))
    else:
        qDot = qDotSol*projection
    return np.squeeze(qDot)

def earthGlowFlux(heightOrbit,face,waves=0):
    '''
    Returns heat flux from outgoing long-wave radiation emitted by earth in W/m^2.
    face is one of ['zenith','nadir','forward','aft','north','south'], it is one of the six faces of a satellite cube.
    uses global values radiusEarth, albedoEarth and qDotSol
    '''
    qDotEarth = qDotSol*(1-albedoEarth)/4 #IR heat flux from earth ~239 W/m^2
    projection = 0
    if face == 'zenith':
        projection = 0 #never sees the earth glow
    elif face == 'nadir':
        projection = (radiusEarth/(radiusEarth+heightOrbit))**2
    else: #forward, aft, north, south
        projection = perpFormFactor(heightOrbit)
        
    if (type(waves)==np.ndarray):
        qDot = np.outer(projection,irradianceSunFromEarth(waves,sunTemp))*(1-albedoEarth)
    else:
        qDot = qDotEarth*projection
    return qDot

def orbitalPeriod(a,G=6.674e-11,M=5.972168e24 ):
    '''
    Returns orbital period in seconds.
    a is semimajor axis (radius for circular orbit).
    G is gravitational constant
    M is mass at center of orbit
    '''
    return 2*np.pi*np.sqrt(a**3/G/M)

