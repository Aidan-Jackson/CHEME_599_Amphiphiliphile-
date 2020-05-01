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
