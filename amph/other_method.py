class other_method:
    
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
    
    def find_bright_spots(img2,lower = 0.8, upper = 0.1):
        # Short summary: Count the number of bright balls in an image
        
        # Extended summary: Take an image, and count the number of bright balls (dyed aqeous regions).
        
        
        # Parameters
        #   img2 should be a 2d array with pixel values between 0 and 255
        #   lower should be the fraction of pixels that certainly correspond to the background
        #   upper should be the fraction of pixels that certainly correspond to the bright dots
    
        # Returns
        #   a string that spits out the counted number of bright regions will be returned
        #   an image with the identified balls shown will also be returned
        
        upper1=1-upper
        
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        from skimage.filters import sobel
        from skimage.segmentation import watershed
        from scipy.ndimage import label, generate_binary_structure
        from skimage.color import label2rgb
        from scipy import ndimage as ndi
        
        total_pixel_number=np.shape(img2)[0]*np.shape(img2)[1]
        hist,bins= np.histogram(img2,bins=np.linspace(np.min(img2),np.max(img2),32))
        background_thresh= bins[np.argmax(np.cumsum(hist/total_pixel_number)>lower)] #find pxel intensity value that (lower*100)% of pixels are <=
        bright_thresh=bins[np.argmax(np.cumsum(hist/total_pixel_number)> upper1)] #find pxel intensity value that (upper*100)% of pixels are <=
        
        markers = np.zeros_like(img2)
        markers[img2 < background_thresh] = 1
        markers[img2 > bright_thresh] = 2
        elevation_map = sobel(img2)
        segmentation = watershed(elevation_map, markers)
        segmentation = ndi.binary_fill_holes(segmentation - 1)
        labeled_coins, _ = ndi.label(segmentation)
    
        figABC,axABC=plt.subplots(ncols=1,figsize=(17,6))
        axABC.imshow(img2, cmap='gray')
        axABC.contour(segmentation, [0.5], linewidths=1.2, colors='y')
        return('number of aqeous drops detected= '+ str(np.max(labeled_coins)))

    def identify_lenses(image_name):
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
        
        image_time0 = plt.imread(image_name)
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
