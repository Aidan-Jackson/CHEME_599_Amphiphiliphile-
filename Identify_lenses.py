'''This code will identify the number of distictly bright objects in an image and count them.

Extended Summary: 
Experiment - Aquaous solution containing a bright dye is encaplusated in a double emulsion. 
Images - The product of this experimetn results in imagaes contianing two distict features; 
Oil droplets (dark) and Lens vesicles (bright).

Paramaters
Need an image

Returns
Number of bright regions

'''

# Import all the packages necessary

import numpy as np
import matplotlib.pyplot as plt
from skimage import data 
from skimage import transform
from skimage.exposure import histogram
from skimage.util import img_as_float, img_as_ubyte
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.filters import threshold_otsu
from scipy import ndimage as ndi
from skimage.morphology import disk
from skimage.filters import rank
from skimage.segmentation import watershed

#Import the image in a usable format. Convert it from a color image to black and white

image_time0 = plt.imread('Images/t01.tif')
im_t0 = img_as_float(image_time0)
im_color = img_as_ubyte(im_t0)
im = rgb2gray(im_color)

#Filter the image to edge detect objects within it

edge_sobel = sobel(im)

#Threshold the image to differentiate bright objects (lenses) from all else (background, oil droplets)

thresh_lens = threshold_otsu(edge_sobel)
binary_lens = edge_sobel > thresh_lens

#segment the image so that we can count the number of bright spots

markers = rank.gradient(binary_lens, disk(6)) < 10
markers = ndi.label(markers)[0]
gradient = rank.gradient(binary_lens, disk(2))
labelled_lens = watershed(gradient, markers)

return('total number of lenses= '+ str(np.max(labelled_lens)))












