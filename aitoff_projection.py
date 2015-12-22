

#!/usr/bin/python                                                                                                                                                                                           

# Created by: J. G. Fernandez-Trincado                                                                                                                                                                      
# Date: 2015, December                                                                                                                                                                                      

import numpy as np
import scipy as sc
import pylab as plt

data = sc.genfromtxt('Input data here',comments='#',names=True)#'Input data here'                                                                                                                           


RA  = data['RA']
DEC = data['DEC']

# Important: You need defined the grid size in RA, and DEC. I have assumed 2 degrees in RA (e.g., size_RA = 2 degrees), and 2 degrees in DEC (e.g., size_DEC = 2 degrees).                                  

size_RA, size_DEC = 2., 2.
bin_RA  = int(360./2.)
bin_DEC = int((np.max(DEC) - np.min(DEC))/2.)

H, xedges, yedges = np.histogram2d(RA, DEC, bins=(bin_RA, bin_DEC))

RA, DEC, Z = [], [], []
for i in np.arange(len(xedges[:-1])):
        for j in np.arange(len(yedges[:-1])):
                RA, DEC, Z = np.append(RA, xedges[:-1][i]), np.append(DEC,yedges[:-1][j]), np.append(Z, H.T[j,i])


# Optional: uncomment the following two lines if you not need print zero values in the third component, see Figure2.png                                                                                     
mask       = (Z >0)
RA, DEC, Z = RA[mask], DEC[mask], Z[mask]

# convert coordinates to degrees                                                                                                                                                                            
RA -= 180
RA *= np.pi / 180
DEC *= np.pi / 180

ax = plt.axes(projection='mollweide')
plt.scatter(RA, DEC, s=30, c=Z, cmap=plt.cm.jet, edgecolors='none')#, linewidths=3)                                                                                                                         
plt.grid(True)

# Bar color                                                                                                                                                                                                 

plt.title('ADD NAME HERE)')
cb = plt.colorbar(cax=plt.axes([0.05, 0.1, 0.9, 0.05]),
                  orientation='horizontal',
                  ticks=np.linspace(0, np.max(Z), 10))

cb.set_label('ADD NAME BAR COLOR HERE')

plt.show()
