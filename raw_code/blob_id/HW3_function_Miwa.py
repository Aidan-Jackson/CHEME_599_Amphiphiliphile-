import matplotlib.pyplot as plt
import numpy as np
import skimage as sk
from skimage import io
from skimage.feature import blob_log
from skimage.color import rgb2gray
from skimage.util import pad, img_as_float
from skimage.filters import rank
from skimage.morphology import square, disk, star
from skimage.feature import blob_dog, blob_log, blob_doh

"""

Short Summary
-------------

Extended Summary
----------------

Parameters
----------
image_name: Name of the image.

Returns
-------

Examples
--------
find_blobs('t01.jpg')

"""
def find_blobs(image_name):

    original = io.imread(image_name)

    enhance = rgb2gray(original)
    enhance = img_as_float(enhance)
    enhance = rank.mean(enhance,square(10))

    manipulate = blob_doh(enhance,max_sigma=35,num_sigma=10,threshold=.01)

    fig, ax = plt.subplots(ncols=3, figsize=(15, 5))
    ax[0].imshow(original)
    ax[0].set_title('Original Image')
    ax[0].set_axis_off()
    ax[1].imshow(enhance,cmap='gray')
    ax[1].set_title('Enhanced Image')
    ax[1].set_axis_off()
    ax[2].imshow(original)
    ax[2].set_title('Processed Image with Edge Detection')
    ax[2].set_axis_off()

    for blob in manipulate:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
        ax[2].add_patch(c)


    plt.show()