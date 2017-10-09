class GV:
   """ Collection of constants [SI units]
       and useful quantities """
   def __init__(self):
      import numpy as np
      self.G = 6.67408e-11 # Gravitational constant [m3/kg/s2] (Mohr et al., 2016).
      self.pi = np.pi      # [1]
      self.sXd = 86400.    # Seconds per day
      self.sXy = self.sXd*365 # Seconds per year
      self.sXMy= self.sXy*1e6 # Seconds per million years
      self.C2K = 273.15    # Celsius to Kelvin additive constant [K]
      self.SSa = 4.55e3    # Solar system age [My] (Bouvier and Wadhwa, 2010).
      self.Rgc = 8.3144621 # Gas constant [J/K/mol] ().
      self.d2r = np.pi/180.  # Degree to radian conversion factor   [1]
      self.r2d = 180./np.pi  # Radians to degrees conversion factor [1]

