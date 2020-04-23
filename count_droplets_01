def count_droplets(test_img, low_thresh = 0.9):
    
    # Short summary: This function will count the number of bright circles in a image.

    #Extended summary: This function can count the number of objects in image using region based segmentation with an 
    #intensity threshold defined by the user.

    #Inputs: Image (preferability in .jpg or .tif format), lower threshold (value from 0 to 1)

    #Outputs: The number of bright objects

    #Example: For our team project we want to identify the number of lenses in fluorescent microscopy images. 
    #Lenses are the objects that contain an envelop of oil within a membrane. 
    #In the images, these are the objects that appear as a bright blob within a highlighted dark circle. 
    #To start identifying these objects, we can use the function count_droplets to first identify all of the bright oil droplets.
    
    import numpy as np
    import matplotlib.pyplot as plt

    from skimage import data
    from skimage.exposure import histogram
    from skimage.filters import rank
    from skimage.segmentation import watershed
    from scipy import ndimage as ndi
    
    #Convert image from color to color to grayscale & plot histogram
    test_img_gray = rgb2gray(test_img)
    hist, bins = histogram(test_img_gray)

    #Set threshold to identify objects
    fig, axes = plt.subplots(1, 3, figsize=(20, 10))
    axes[0].imshow(test_img, cmap=plt.cm.gray)
    axes[0].axis('off')
    axes[1].plot(bins, hist, lw=2)
    axes[2].imshow(test_img_gray>low_thresh, cmap=plt.cm.gray)
    
    #Use watershed segmentation to count the number of objects detected
    droplets = test_img_gray>.9
    label = rank.gradient(droplets, disk(2))
    labelled_droplets = ndi.label(label)[0]
    gradient = rank.gradient(droplets, disk(2))
    plt.imshow(gradient)
    count = watershed(gradient, labelled_droplets)
    number_of_drops = str(np.max(count)) #string to return droplet count
    return;

print(number_of_drops)
