class plc:
   """
   
      ----- USAGE ---------------------------------
      # Import the class
      from planets_class import plc
      
      # Create planet object [e.g., Mars]
      pl = plc('Mars')
      
      # Access planet's attributes with dot operator
      PlanetRadius = pl.radius
      -----------------------------------------------


      **SI units adopted**  

      PLANETARY DATA: 
         - Bulk parameters -
      radius   : planetary radius [m]
      Rcore : core radius [m]
      Cr    : crustal thickness [m]
      NCr   : northern hemisphere modal crustal thickness [m] (*Only for Mars*)
      SCr   : southern hemisphere modal crustal thickness [m] (*Only for Mars*)
      mass  : mass [kg]
      dmt   : density of the mantle [kg/m^3]
      dcore : density of the core [kg/m^3]
      moif  : Non-dimensional moment of inertia [1]
      TS    : equilibrium temperature [K] (Possibly substitute with albedo)
      Tcmb  : Core mantle boundary temperature [K]
      meltP : pressure above which melt is buoyant [Pa]
         - Orbital parameters - 
      ecc   : eccentricity [1]
      sma   : semi-major axis [m]
      Mc    : mass of the parent body, i.e. the object around which the body orbits [kg]

      MATERIAL PARAMETERS:
      Cp     : Silicate heat capacity [J/kg/K]
      Ka     : Thermal diffusivity    [m*m/s]
      etaref : Reference viscosity    [Pa*s]
      TrefK  : Reference temperature  [K]
      PrefPa : Reference pressure     [Pa]
      alpha  : thermal expansivity    [1/K]
      kc     : crustal thermal conductivity [W/m/K]
      kr     : regolith thermal conductivity [W/m/K]

      DERIVED DIMENSIONAL QUANTITIES:
      D      : Mantle thickenss [m]
      DeltaT : Temperature increase across mantle [K]
      km     : Mantle thermal conductivity (obtained from Ka,dmt,Cp)
      gravity     : Surface gravitational acceleration [m/s/s]
      n      : Mean orbita motion
      density    : Density of the planet

      SCALING FACTORS
      Pscale   : Pressure scale [Pa]
      CPscale  : Heat capacity scale [J/kg/K]
      vscalemt : Velocity scale mantle [m/s] (~1e-12)
      vscaleip : Velocity scale impacts [m/s] (1e3)
      sEscale  : Specific energy scale [J/kg]
      tscale   : Time scale [s]

      NON-DIMENSIONAL QUANTITIES [unitless]
      T0      : Surface temperature 
      Ra      : Rayleigh number
      Di      : Dissipation number
      Tref    : Reference temperature
      Pref    : Reference pressure
      AgeOfSS : Age of the solar system


   """ 
   def __init__(self,body,debug=2):
      import numpy as np
      import sys,string
      from GV import GV
      gc = GV()

      if debug>0: print plc.__doc__
      
      body = string.lower(body)
      self.body  = body

      if body=='mercury':
         # Bulk parameters
         self.radius = 2.439e6 # [Perry et al 2015]
         self.Rcore  = 2.02e6  # [Hauck et al 2013]
         self.Cr     = 35.e3   # [Padovan et al 2015]
         self.mass   = 3.3e23  # [Smith et al. 2012] 
         self.dmt    = 3380.   # [Hauck et al 2013]
         self.dcore  = 6980.   # [Hauck et al 2013]
         self.moif   = 0.346   # [Margot et al. 2012] 
         self.TS     = 440.    # 
         self.Tcmb   = 1900.   # [Tosi et al. 2013] 
         self.meltP  = 100.e9  # [VanderKaaden McCubbin, 2015] (melt buoyant in the entire mantle)
         # Orbital p arameters
         self.ecc  =  0.2056    # [Mercury fact sheet]
         self.sma  = 57.91e9   # [Mercury fact sheet]
         self.Mc   = 1.9885e30 # [Sun fact sheet]
         # Material parameters
         self.Cp     = 1200.  # [Ina's spreadsheet]
         self.Ka     = 1.e-6  # 
         self.etaref = 1.e20  # 
         self.TrefK  = 1600   # 
         self.PrefPa = 3e9    # 
         self.alpha  = 3.e-5  # [Roberts & Barnouin, 2012]
         self.kc     = 3.3    #  
         self.kr     = 0.2    #  
      
      elif body=='earth':
         # Bulk parameters
         self.radius = 6.371e6   # [Earth fact sheet]
         self.Rcore  = 3.485e6   # [Earth fact sheet]
         self.Cr     = 35.e3     # [Continental]
         self.mass   = 5.9723e24 # [Earth fact sheet] 
         self.dmt    = 4e3       # [PREM]
         self.dcore  = 11e3      # [PREM]
         self.moif   = 0.3308    # [Earth fact sheet]
         self.TS     = 293.      # 
         self.Tcmb   = 4000.     # [SSS]
         self.meltP  = 8.e9      # [SSS]
         # Orbital p arameters 
         self.ecc  =  0.0167   # [Earth fact sheet]
         self.sma  = 1.496e11  # [Earth fact sheet]
         self.Mc   = 1.9885e30 # [Earth fact sheet]
         # Material parameters
         self.Cp     = 1200.  # 
         self.Ka     = 1e-6   # 
         self.etaref = 1e21   #  
         self.TrefK  = 1600   #  
         self.PrefPa = 3e9    # 
         self.alpha  = 2.5e-5 #
         self.kc     = 2.     #
         self.kr     = 0.2    # 

      elif body=='moon':
         # Bulk parameters
         self.radius = 1.74e6   # [GAIA spreadsheet]
         self.Rcore  = 3.9e5    # [GAIA spreadsheet]
         self.Cr     = 38.5e3   # [Wieczorek et al 2014]
         self.mass   = 7.346e22 # [Smith et al. 2012] 
         self.dmt    = 3300.    # [Moon Fact sheet]
         self.dcore  = 7000.    # 
         self.moif   = 0.392728 # [Williams et al 2014]
         self.TS     = 250.     # 
         self.Tcmb   = 1900.    # 
         self.meltP  = 100.e9   # (melt buoyant in the entire mantle)
         # Orbital p arameters 
         self.ecc  =  0.0549    # [Moon fact sheet]
         self.sma  = 3.844e8   # [Moon fact sheet]
         self.Mc   = 5.97e24   # [Earth fact sheet]
         # Material parameters
         self.Cp     = 1200.  # 
         self.Ka     = 1e-6   # 
         self.etaref = 1e21   #  
         self.TrefK  = 1600   #  
         self.PrefPa = 3e9    # 
         self.alpha  = 2.5e-5 #
         self.kc     = 2.     #
         self.kr     = 0.2    # 

      elif body=='mars':
         # Sources: MaFS [Mars Fact Sheet], R11 [Rivoldini et al, 2011]
         #          N04 [Neumann et al., 2004] WZ04 [Wieczorek & Zuber, 2004]
         #          P15 [Plesa et al., 2015]
         # Bulk parameters
         self.radius = 3.3895e6   # [R11,MaFS]
         self.Rcore  = 1.794e6    # [R11] [1.7e6 in MaFS]
         self.Cr     = 50.e3      # [WZ04, sigma 12 km]
         self.NCr    = 32.e3      # [N04]
         self.SCr    = 58.e3      # [N04]
         self.mass   = 6.41855e23 # [R11] [MaFS=6.4171e23] 
         self.dmt    = 3500.      # [P15] 
         self.dcore  = 6433.      # Obtained from Rcore, density, and self.dmt with TwoLModel.py
         self.moif   = 0.3644     # [Konopliv et al 2011]
         self.TS     = 210.       # [with albed=0.25 from SolarConstant.py]
         self.Tcmb   = 2225.      # [P15] 
         self.meltP  = 7.e9       #  
         # Orbital data 
         self.ecc  = 0.0935      # [MaFS]
         self.sma  = 2.2792e8    # [MaFS]
         self.Mc   = 1.9885e30   # [Sun fact sheet]
         # Material parameters
         self.Cp     = 1200.  # [P15, Table 3] 
         self.Ka     = 1e-6   # [P15, Table 3]
         self.etaref = 1e21   # [P15, between 1e20 e 1e23] 
         self.TrefK  = 1600   #  
         self.PrefPa = 3e9    # 
         self.alpha  = 2.5e-5 # [P15]
         self.kc     = 2.     # [P15]
         self.kr     = 0.2    # 

      else:
         print ("****** Data not available for planet %s"%(body))
         sys.exit()


      # DERIVED QUANTITIES
      self.D       = self.radius-self.Rcore # [m] Mantle thickness
      self.DeltaT  = self.Tcmb-self.TS # [K] T scaling
      self.km      = self.Ka*self.dmt*self.Cp                # [W/m/K] thermal conductivity mantle  
      self.gravity = (gc.G*self.mass)/(self.radius**2.)          # [m/s2] grav. acc.
      self.n       = ((gc.G*self.Mc)/self.sma**3.)**(1./2.) # [1/s]
      self.density = 3.*self.mass/(4*np.pi*self.radius**3.) # kg/m^3
      # SCALING FACTORS
      self.Pscale    = self.dmt*self.gravity*self.D  # [Pa] pressure scale
      self.Cpscale   = (self.gravity*self.D)/(self.DeltaT) # [J/kg/K] specific heat scale
      self.vscalemt  = self.Ka/self.D   # [m/s] velocity scale mantle (~1e-12 m/s)
      self.vscaleimp = np.sqrt(self.gravity*self.D)   # [m/s] velocity scale impacts (~ km/s)
      self.sEscale   = self.Cp*self.DeltaT # [J/kg] specific energy scale
      self.tscale    = self.D*self.D/self.Ka
      # NON-DIMENSIONAL QUANTITIES
      self.T0      = self.TS/self.DeltaT
      self.Ra      = (self.dmt*self.gravity*self.alpha*self.DeltaT*self.D**3.)/(self.Ka*self.etaref)
      self.Di      = (self.alpha*self.gravity*self.D)/self.Cp 
      self.Tref    = (self.TrefK - self.TS)/self.DeltaT
      self.Pref    = self.PrefPa/self.Pscale
      self.AgeOfSS = (4.5e9*365.*24*60*60)/self.tscale

