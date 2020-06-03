{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Detect_bright_spots(test_img, low_thresh = 0.9):\n",
    "    '''\n",
    "    Short summary: This function will count the number of bright spots in a image.\n",
    "\n",
    "    Extended summary: This function can count the number of objects in image using region based segmentation with an \n",
    "    intensity threshold defined by the user.\n",
    "\n",
    "   Parameters:\n",
    "    test_img should be a 3d array \n",
    "    lower_thresh should be the fraction of pixels that certainly correspond to the background\n",
    "\n",
    "    Returns:\n",
    "    a string that spits out the counted number of bright regions will be returned\n",
    "    an image with the bright spots outlined in magenta shown will also be returned\n",
    "\n",
    "    Example: For our project we want to identify the number of lenses in fluorescent microscopy images. Lenses are the objects that contain an envelop of oil within a membrane. In the images, these are the objects that appear as a bright blob within a highlighted dark circle. \n",
    "    To start identifying these objects, we can use the function count_droplets to first identify all of the bright oil droplets.\n",
    "    '''\n",
    "    #import scikit tools\n",
    "    import numpy as np\n",
    "    import matplotlib.pyplot as plt\n",
    "    from skimage import data\n",
    "    from skimage.exposure import histogram\n",
    "    from skimage.filters import rank\n",
    "    from skimage.color import rgb2gray\n",
    "    from skimage.segmentation import watershed\n",
    "    from skimage.morphology import square, disk\n",
    "    from scipy import ndimage as ndi\n",
    "    \n",
    "    #Import and read image (Image should be color i.e 3D array)\n",
    "    test_img = plt.imread('t01.jpg')\n",
    "    \n",
    "    #Define a threshold for identifying bright objects\n",
    "    low_thresh = 0.9\n",
    "\n",
    "    #Convert image from color (3D) to grayscale (2D)\n",
    "    test_img_gray = rgb2gray(test_img)\n",
    "    \n",
    "    #Plot historgram of intensities\n",
    "    hist, bins = histogram(test_img_gray)\n",
    "\n",
    "    #Plot images to check for accuracy of user-defined threshold\n",
    "    fig, axes = plt.subplots(1, 3, figsize=(20, 10))\n",
    "    for ax in axes:\n",
    "        ax.axis('off')\n",
    "    \n",
    "    axes[0].imshow(test_img, cmap=plt.cm.gray)\n",
    "    axes[0].set_title(\"Original Image\")\n",
    "    axes[1].imshow(test_img_gray>low_thresh, cmap=plt.cm.gray)\n",
    "    axes[1].set_title(\"Threhsold-detected Spots\")\n",
    "    #axes[2].plot(bins, hist, lw=2)\n",
    "    axes[2].set_title(\"Create a mask with \")\n",
    "\n",
    "    #Use watershed segmentation to count the number of birght objects detected\n",
    "    \n",
    "    droplets = test_img_gray>.9 #Define droplet as any pixel greater than the threshold\n",
    "    label = rank.gradient(droplets, disk(2)) #Use gradient to define area betwen background and bright spot\n",
    "    labelled_droplets = ndi.label(label)[0]\n",
    "    plt.imshow(gradient)\n",
    "    count = watershed(gradient, labelled_droplets) #Use watershed to \"mark\" regions and count spots\n",
    "    number_of_drops = str(np.max(count)) #string to return droplet count\n",
    "\n",
    "    return;\n",
    "\n",
    "print(number_of_drops)\n",
    "fig, ax = plt.subplots(figsize=(15, 9), sharey=True)\n",
    "ax.imshow(test_img, cmap=plt.cm.gray)\n",
    "ax.contour(labelled_droplets, [0.5], linewidths=1.2, colors='m', alpha=0.7)\n",
    "plt.title('Threshold Overlay')\n",
    "plt.axis('off')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
