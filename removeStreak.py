# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:38:33 2016

@author: Chris Dilger
"""
from astropy.io import fits
import glob
from scipy.ndimage import median_filter
import os

directory = '.\fits'
outdir = '.\outfits'

target = 579
lineRemovedString = '-line-removed'

filelist = glob.glob(directory + '\*.fits')
if len(filelist) == 0:
    raise ValueError('No fits files in ' + directory)

for filename in filelist:
    hdulist = fits.open(filename)
    print 'processing ' + filename
    for i in range(len(hdulist[0].data[579])):
        hdulist[0].data[i][target] = (hdulist[0].data[i][target+1] + hdulist[0].data[i][target-1]) / 2
    hdulist[0].data = median_filter(hdulist[0].data, size=3)
    filename = filename.replace(directory, '')
    ensureExists(outdir)
    hdulist.writeto(outfilename)
    outfilename = outdir + filename + lineRemovedString + '.fits'
    

#print hdulist[0].data[579][0]
    
#hdulist = fits.open('fits/Initial Cyg X-1 P6_1325181_B_001.fits')

def ensureExists(directory):
    if (!os.path.exists(directory)):
        os.mkdir(directory)