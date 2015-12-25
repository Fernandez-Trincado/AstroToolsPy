

# Instructions run the Python program: python -W ignore BPT.py
# Program to reproduce the BPT diagram using PyFits and FITS format. 

import numpy as np
import scipy as sc
import pylab as plt
import urllib2
from astropy.io import fits

try: 
	import pyfits

except ImportError:
	print '\n PyFITS is no installed, Try from your console one of the following options: \n [1] pip install pyfits \n [2] sudo apt-get install python-pyfits (for Python2) \n [3] sudo apt-get install python3-pyfits (for Python3)'

# Input data 

#FITS = fits.open('http://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/Data/gal_line_dr7_v5_2.fit.gz') # Input data taken from XXX in its original format. 
# Download the data here: http://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/Data/gal_line_dr7_v5_2.fit.gz

FITS = fits.open('gal_line_dr7_v5_2.fit.gz')  # Read the compress data

Hbeta  = FITS[1].data['H_BETA_FLUX']          # Reading the column with Hbeta line 
OIII   = FITS[1].data['OIII_5007_FLUX']       # Reading the column with OIII line
Halpha = FITS[1].data['H_ALPHA_FLUX']         # Reading the column with Halpha line
NII    = FITS[1].data['NII_6584_FLUX']        # Reading the column with NII line


f      = plt.figure(1)
xx     = np.log10(  NII / Halpha )      # log10(NII/Halpha)
yy     = np.log10( OIII /  Hbeta )      # log10(OIII/Hbeta)

ax                 = f.add_subplot(1,1,1)
bins_X, bins_Y     =  60., 60.   # Define the number of bins in X- and Y- axis
Xmin, Xmax         = -1.2, 1.2   # Define the maximum and minimum limit in X-axis
Ymin, Ymax         = -1.5, 1.0   # Define the maximum and minimum limit in Y-axis
Nlevels            = 6           # Define the number of levels of isocontour


hist,xedges,yedges = np.histogram2d(xx,yy,bins=(bins_X, bins_Y),range=[[Xmin,Xmax],[Ymin,Ymax]])
masked             = np.ma.masked_where(hist==0, hist)
plotting           = ax.imshow(masked.T,extent=[Xmin, Xmax, Ymin, Ymax],interpolation='nearest',origin='lower',cmap=plt.cm.gray_r)
levels             = np.linspace(0., np.log10(masked.max()), Nlevels)[1:]
CS                 = ax.contour(np.log10(masked.T), levels, colors='k',linewidths=1,extent=[Xmin,Xmax,Ymin,Ymax])


# Kewley+01 ------------------------------------------
X = np.linspace(-1.5,0.3)
Y = (0.61/( X  - 0.47  )) + 1.19

# Schawinski+07 --------------------------------------
X3 = np.linspace(-0.180,1.5)
Y3 = 1.05*X3 + 0.45

# Kauffmann+03 ---------------------------------------
Xk = np.linspace(-1.5,0.)
Yk = 0.61/(Xk -0.05) + 1.3

# Regions --------------------------------------------
ax.plot(X,   Y, '-' , color='blue', lw=3, label='Kewley+01'    ) # Kewley+01
ax.plot(X3, Y3, '-', color='blue', lw=5, label='Schawinski+07') # Schawinski+07
ax.plot(Xk, Yk, '--', color='blue', lw=5, label='Kauffmann+03' ) # Kauffmann+03

# Axi name here ...
Nsize = 25
ax.set_xlabel(r'log([NII] $\lambda$ 6583/H$\alpha$)',fontsize=Nsize)
ax.set_ylabel(r'log([OIII] $\lambda$ 5007/H$\beta$)',fontsize=Nsize)
ax.tick_params(labelsize = Nsize)
ax.set_ylim(Ymin, Ymax)
ax.set_xlim(Xmin, Xmax)

plt.show()
