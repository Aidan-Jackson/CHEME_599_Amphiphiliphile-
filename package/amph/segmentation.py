#Class for functions using the segmentation method. Cannot be used to track particles across frames.
class segmentation: 
    def Detect_bright_spots(test_img, low_thresh = 0.9):
        '''
        Short summary: This function will count the number of bright spots in a image.

        Extended summary: This function can count the number of objects in image using region based segmentation with an 
        intensity threshold defined by the user.

       Parameters:
        test_img should be a 3d array 
        lower_thresh should be the fraction of pixels that correspond to the background

        Returns:
        a string that spits out the counted number of bright regions will be returned
        an image with the bright spots outlined in magenta shown will also be returned

        Example: For our project we want to identify the number of lenses in fluorescent microscopy images. Lenses are the objects that contain an envelop of oil within a membrane. In the images, these are the objects that appear as a bright blob within a highlighted dark circle. 
        To start identifying these objects, we can use the function count_droplets to first identify all of the bright oil droplets.
        '''
        #import scikit tools
        import numpy as np
        import matplotlib.pyplot as plt
        from skimage import data
        from skimage.exposure import histogram
        from skimage.filters import rank
        from skimage.color import rgb2gray
        from skimage.segmentation import watershed
        from skimage.morphology import square, disk
        from scipy import ndimage as ndi
        
        #Import and read image (Image should be color i.e 3D array)
        test_img = plt.imread('t01.jpg')
        
        #Define a threshold for identifying bright objects
        low_thresh = 0.9

        #Convert image from color (3D) to grayscale (2D)
        test_img_gray = rgb2gray(test_img)
        
        #Plot historgram of intensities
        hist, bins = histogram(test_img_gray)

        #Plot images to check for accuracy of user-defined threshold
        fig, axes = plt.subplots(1, 3, figsize=(20, 10))
        for ax in axes:
            ax.axis('off')
        
        axes[0].imshow(test_img, cmap=plt.cm.gray)
        axes[0].set_title("Original Image")
        axes[1].imshow(test_img_gray>low_thresh, cmap=plt.cm.gray)
        axes[1].set_title("Threhsold-detected Spots")
        #axes[2].plot(bins, hist, lw=2)
        axes[2].set_title("Create a mask with ")

        #Use watershed segmentation to count the number of birght objects detected
        
        droplets = test_img_gray>.9 #Define droplet as any pixel greater than the threshold
        label = rank.gradient(droplets, disk(2)) #Use gradient to define area betwen background and bright spot
        labelled_droplets = ndi.label(label)[0]
        plt.imshow(gradient)
        count = watershed(gradient, labelled_droplets) #Use watershed to "mark" regions and count spots
        number_of_drops = str(np.max(count)) #string to return droplet count

        print(number_of_drops)
        fig, ax = plt.subplots(figsize=(15, 9), sharey=True)
        ax.imshow(test_img, cmap=plt.cm.gray)
        ax.contour(labelled_droplets, [0.5], linewidths=1.2, colors='m', alpha=0.7)
        plt.title('Threshold Overlay')
        plt.axis('off')
        
        return;

        
