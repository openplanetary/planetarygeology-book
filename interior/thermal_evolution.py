import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 15.
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.labelsize'] = 12.
plt.rcParams['xtick.labelsize'] = 15.
plt.rcParams['ytick.labelsize'] = 15.
params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)

def thermal_evolution( planet, tecmode, T0, eta0 ):
    """
    Simple thermal evolution model of the mantle of a terrestrial body. Given the mode of surface deformation, the
    initial mantle temperature and the reference viscosity, the model calculates the evolution of
    the last two quanities over 4.5 Gyr. 

    As input the function accepts the follwing parameters:
    name of the planet (e.g. mars)
    tectonic mode tecmode (either 'ml' for mobile lid or 'sl' for stagnant lid
    initial mantle temperature T0 (in K)
    reference mantle viscosity eta0 (in Pa s)

    On output it returns three arrays containing time (in Myr), temperature (in K) and viscosity (in Pa s)
    """
    
    D = planet.radius - planet.Rcore # Mantle thickness (m)
    Rp = planet.radius               # Planetary radius (m)
    M = planet.mass                  # Planetary mass  (kg)
    g0 = planet.gravity              # Gravity acceleration (m/s^2)        
    A = 4*np.pi*Rp**2                # Planetary surface (m^2)
    Tsurf = planet.Ts                # Surface temperature

    H0 = 23e-12                      # Internal heat production 4.5 Gyr ago (W/kg)
    ll = 1.42e-17                    # Decay constant in (1/s)

    E = 3e5                          # Activation energy (J/mol)
    R = 8.314                        # Gas constant (J/K/mol)
    Tref = 1600.                     # Reference temperature for viscosity law (K)

    rho0 = 3.5e3                     # Mantle density (kg/m^3)
    k = 3.                           # Thermal conductivity (W/m/K)   
    cp = 1200.                       # Isobaric heat capacity (J/kg/K)
    kappa = k/rho0/cp                # Thermal diffusivity (m^2/s)
    alpha = 3e-5                     # Thermal expansivity (1/K)

    beta = 1./3.                     # Nusselt-Rayleigh exponent
    Racr = 1100.                     # Critical Rayleigh number

    f1 = H0/cp      
    f2 = A*k/(M*cp*D) * (rho0*g0*alpha*D**3 / (kappa*eta0*Racr))**beta

    yrs = 365.25*24*60*60            # 1 yr in seconds
    time = 4.5e9*yrs                 # Age of the Solar System
    dt = 1e7*yrs                     # Time stepping (10 Myr)     
    nsteps = time/dt                 # Number of time steps
    t = np.arange(0., time+dt, dt)   # Time array

    T = np.zeros_like(t)             # Temperature array
    T[0] = T0                        # Set initial temperature 

    eta = np.zeros_like(t)           # Viscosity array
    eta[0] = eta0*np.exp(E/R*(Tref-T0)/(Tref*T0)) # Set initial viscosity

    for i in np.arange(1, np.size(t)):

        # Choose tectonic mode: mobile lid (ml) vs stagnant lid (sl) and 
        # set accordingly the temperature of the upper boundary of the convecting layer, i.e.
        # surface temperature for ml and stagnant lid temperature for sl.
        if tecmode == 'ml':
            Tup = Tsurf
        elif tecmode == 'sl':
            Tup = T[i-1] - 2.21*R*T[i-1]**2/E

        # Advance temperature in time
        T[i] = T[i-1] + dt*( f1*np.exp(-ll*t[i]) - f2*(T[i-1]-Tup)**(1.+beta)*np.exp(-beta*E/R*(1./T[i-1] - 1./Tref)) )

        # Calculate the corresponding viscosity
        eta[i] = eta0*np.exp(E/R*(1./T[i] - 1./Tref))

    return t/yrs/1e6, T, eta


        
  


