# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:25:22 2016

@author: luciano
"""
###############################################################################
# LECTURA Y GRAFICADO DATOS GOES-E NASA (TIF format)
###############################################################################

import matplotlib.pyplot as plt
import numpy as np 
from time import clock
from mpl_toolkits.basemap import Basemap

###############################################################################

start_time = clock()

###############################################################################

# Nombre del archivo
filename = '1602262345G13I04.tif'

# Lectura del archivo
DN = plt.imread(filename)
DN = np.double(DN)
#DN = DN[:,0:900]

# Conversion DN ==> TB [K]
if (np.all(DN)<=175):
    TB = -0.5*DN+330
else:
    TB = -1*DN+243

###############################################################################

# Lectura archivo geolocation
nx=2
ny=600*1000
navfile = "argentina_1006011745_G13I04_M_float.nav"
nav     = np.fromfile(navfile, dtype='>2f')
nav     = np.double(nav)
lat = np.reshape(nav[:,0],(600,1000))
lon = np.reshape(nav[:,1],(600,1000))

m = Basemap(projection='cyl', llcrnrlon=-90, urcrnrlon=-30, llcrnrlat=-60, urcrnrlat=-10, resolution='c')

m.drawcoastlines()
m.drawcountries()
x,y = m(lon,lat)
imgplot=m.pcolormesh(x,y,TB-273.15,cmap='hsv')
cbar=plt.colorbar(imgplot, orientation='horizontal')
cbar.set_label('Degrees C')
plt.title('GOES-E IR4')
plt.axis([-75, -40, -45, -20])
plt.show()

# Agregar puntos en lat/lon especificas
lons = [-65, -40, -55]
lats = [-35, -28, -37]
x,y = m(lons, lats)
pts = m.scatter(x, y, c ='r', marker = 'o', s = 80, alpha = 1.0)


###############################################################################

# Graficado de la imagen
#imgplot = plt.imshow(TB-273.15,extent=[0, 900, 0, 600],cmap='hsv')
#plt.title('GOES-E IR4')
#plt.grid(True)
#plt.axis([0, 900, 0, 600])
#cbar=plt.colorbar(imgplot, orientation='horizontal')
#cbar.set_label('Degrees C')
#plt.show()

###############################################################################

end_time = clock()

print 'It took',end_time - start_time,'seconds'

###############################################################################