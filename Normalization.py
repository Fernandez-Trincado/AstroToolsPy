import pylab as plt
from pylab import *
import pyfits
import numpy as np
import scipy as sc
import matplotlib.lines as lines
                                                                              
input_obs   = Observed spectrum here 
input_model = Model spectrum here from Turbospectrum or etc ...                                                                                                                          

# Apogee lambda ...

wl = np.array([])
for i in np.arange(8575):
        wl = np.append(wl, 4.179 + 6.E-6*i)
wl = 10.**(wl)


plt.plot(wl/1E4, input_obs,lw=2,color='black', fillstyle='none')
plt.plot(wl/1E4, input_model,lw=2,color='red', fillstyle='none')

mask  = (input_obs   > np.median(input_obs) )
mask2 = (input_model > np.median(input_model) )

obs   = np.mean(input_obs[mask])
model = np.mean(input_model[mask2])

diff1 = (obs - model)

if diff1 < 0:

        factor  = np.abs(diff1)
        newflux = input_model - factor

else:
        factor  = np.abs(diff1)
        newflux = input_model + factor

plt.plot(wl/1E4, newflux,lw=2,ls='--',color='red')

# Windows here ...
plt.xlim((16715.)/1E4,(16780.)/1E4)

plt.show()
