# planetarygeology-book
Repo for [undergraduate textbook](http://www.springer.com/de/book/9783319651774)

## Contributors
- [Angelo Pio Rossi](https://github.com/aprossi)
- [Stephan van Gasselt](https://github.com/ZharX)
- [Mario d'Amore](https://github.com/kidpixo)
- [Trent Hare](https://github.com/thareUSGS)
- [Nicola Tosi](https://github.com/nicola-tosi)
- [Sebastiano Padovan](https://github.com/SebastianoPadovan)
- ...

## Requirements
Use of Anaconda python advised. Parameter file for [creating a conda virtual environment](https://conda.io/docs/using/envs.html#create-environment-file-by-hand) (to be checked if it covers all notebooks...)

for nbexntensions, see [conda nb extension guide](https://docs.anaconda.com/anaconda/user-guide/tasks/use-jupyter-notebook-extensions)
```
name: pgbook
dependencies:
  - python=3.4
  - bokeh=0.9.2
  - gdal
  - numpy=1.9.*
  - flask
  - jupyter
  - matplotlib (basemap)
  - pandas
channels:
  - conda-forge
dependencies:
  - jupyter_contrib_nbextensions
```

## Available notebooks
* [Common planetary map projections](https://github.com/openplanetary/planetarygeology-book/blob/master/cartography_map_projections.ipynb)
* [Hypsometry of the Terrestrial planets](hypsometry_terrestrial_planets.ipynb) (sample notebook)
* [Thermal emission spectral data](https://github.com/openplanetary/planetarygeology-book/blob/master/thermalemissionspectrometer_spectral_data.ipynb)
* [Planetary imaging basics](https://github.com/openplanetary/planetarygeology-book/blob/master/planetary-data-basics.ipynb)
* [Hyperspecral data](https://github.com/openplanetary/planetarygeology-book/blob/master/spectral.ipynb)

## Chapter <> Notebook 

**Part I: Methods and Tools**

2. Geologic Tools
3. Exploration Tools : 
* [Planetary imaging basics](https://github.com/openplanetary/planetarygeology-book/blob/master/planetary-data-basics.ipynb)
* [Hypsometry of the Terrestrial planets](https://github.com/openplanetary/planetarygeology-book/blob/master/hypsometry_terrestrial_planets.ipynb)
* [Hyperspecral data](https://github.com/openplanetary/planetarygeology-book/blob/master/spectral.ipynb)
* [Thermal emission spectral data](https://github.com/openplanetary/planetarygeology-book/blob/master/thermalemissionspectrometer_spectral_data.ipynb)
* [HRSC imagery and machine learning](https://github.com/openplanetary/planetarygeology-book/blob/master/HRSC_imaging_data_machine_learning_examples.ipynb)

4. Cartography Tools : 
* [Common planetary map projections](https://github.com/openplanetary/planetarygeology-book/blob/master/cartography_map_projections.ipynb)
5. Ground Truth

**Part II: Processes and Sources**

6. Meteorites
7. Impact Cratering
8. Endogenic Processes : 
* [Hypsometry of the Terrestrial planets](https://github.com/openplanetary/planetarygeology-book/blob/master/hypsometry_terrestrial_planets.ipynb)
9. Surface Processes
10. Interiors and Atmospheres
* [Interior structure](https://github.com/openplanetary/planetarygeology-book/blob/master/interior/interior_structure.ipynb)
* [Thermal evolution](https://github.com/openplanetary/planetarygeology-book/blob/master/interior/thermal_evolution.ipynb)

**Part III: Integration and Geological Syntheses**

11. The Terrestrial Planets: 
 * [Hypsometry of the Terrestrial planets](https://github.com/openplanetary/planetarygeology-book/blob/master/hypsometry_terrestrial_planets.ipynb)
12. Icy and Rocky–Icy Satellites
13. Small Bodies and Dwarf Planets

**Part IV: Frontiers**

14. Astrobiology, the Emergence of Life, and Planetary Exploration
15. Spaceand Planetary Resources

Appendix: Planetary Facts, Data and Tools
Part V Index Terms

## Input/Oputput and support files 
Eventual input files should be in a directory with the same name of the Jupyter notebook (or script, or alike) with the ```_input``` suffix, e.g.. Similar approach for outputs, i.e. ```_output```.

```
├── hypsometry_terrestrial_planets.ipynb
└── hypsometry_terrestrial_planets_input
    ├── data-sources.md
    └── topography
        ├── earth.etopo1.cea.tif
        ├── mars.mola.cea.tif
        ├── mars.mola.iau2000.cea.tif
        ├── mercury.mla.cea.tif
        ├── moon.lola.cea.tif
        └── venus.magellan.filled.cea.tif
```
