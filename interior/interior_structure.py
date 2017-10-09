import numpy as np
from matplotlib import pyplot as plt

def two_layer_model(rho0, moif):
    """
    2-layer interior strucutre model. Given the mean density (rho) and moment of inertia factor (moif)
    of a planetary body, the function calculates the core density, mantle density and core mass fraction 
    as a function of the relative core radius that are compatible with the given rho and moif.

    Input:
    rho0: mean density of the planet
    moif: moment of inertia factor

    Output:
    Three arrays containing core radius ratio, core mass fraction, core density and mantle density (in kg/m^3)
    """

    Rc_ratio = np.linspace(0,1,100)              # Core over planetary radius
    rho = np.ones_like(Rc_ratio)*rho0            # Mean density array

    # Core density, mantle density and core mass fraction
    rhoc = rho*(5./2*moif-(1-Rc_ratio**5)/(1-Rc_ratio**3)) / (Rc_ratio**5-Rc_ratio**3*(1-Rc_ratio**5)/(1-Rc_ratio**3))
    rhom = rho/(1-Rc_ratio**3) - Rc_ratio**3 / (1-Rc_ratio**3)*rhoc
    Mc_ratio = rhoc*(rho-rhom) / (rho*(rhoc - rhom))

    return Rc_ratio, Mc_ratio, rhoc, rhom


