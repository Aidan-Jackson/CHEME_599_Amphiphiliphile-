def blobs (project_image,sig_max,min_thr): 

    '''
    Short Summary
    -------------
    This function identifies the number, location, and size of white blobs within a single image by using one of the skimage.feature blob detection functions. Lenses, a white particle on top of a black one, are also counted individually and the same values are tracked. Function is passed an image [project_image] as a 2D array, the maximum standard deviation [sig_max] to accept when searching for a blob (which is analogous to maximum allowable blob size), and the intensity threshold at which it will first consider blob to be found at [min_thr] computed as a fraction of the maximum intensity in the image. The position, size, and number of blobs in an image.

    Position information is given as the x and y coodinates of the local maximum, assumed to be the center, of each blob found. Size is the average radius of the blob from the center to its  detected edge.

    Parameters
    ----------
    project_image : 2D array
                   image to be analyzed by the function
    sig_max : int
              maximum standard deviation for use in finding the Gaussian matrix of the image.
              Proportional to the maximum allowable size of blobs that can be detected.
     min_thr : float
             minimum intensity threshold for which the function determines the local maxima (center) of the blob 
    
    Returns
    -------
    x : list 
                 X-Coordinate of detected blobs
    y : list 
                 Y-Coordinate of detected blobs
                 
    r : list 
                 radius (size) of detected blobs
               
    blob_count : int
                 Number of blobs found in the image
    '''

    import numpy as np
    import skimage
    from skimage.feature import blob_dog
    from skimage.util import invert
    from skimage.color import rgb2gray
    
    blobs_dog = blob_dog(project_image, max_sigma=sig_max, threshold=min_thr) 
    #uses the built in 'Blob Detection' function that computes the Laplace of the Gaussian matrix of the image to identify, locate, and size blobs.dw
    x = blobs_dog[:,1] #extracts the x coordinate information for each blob
    y = blobs_dog[:,0] #extracts the y coordinate information for each blob
    r = blobs_dog[:,3] #extracts the radius information for each blob
    
    lens_count = 0 #number of white particles on top of dark particles, starts at zero
    xl = [] #empty list for x coordinates of lenses
    yl = [] #empty list of y coordinates of lenses
    rl = [] #empty list of radius values for lenses
    
    mean = np.mean(r)
    
    for i in range(len(r)): #for loop to check each white blob to determine if it
                                         #is also a lens (white on black blob)
        if r[i-lens_count] < mean: #checks for a lens by comparing its size to the average of all 
                                 #blobs in the image (lenses can be seen to be smaller on average)
           
            xl.append(x[i-lens_count]) #adds detected lens to its separate list
            yl.append(y[i-lens_count])
            rl.append(r[i-lens_count])
            x = np.delete(x,i-lens_count) #deletes entry from the white blob list,
            y = np.delete(y,i-lens_count) #accounting for previous deletions
            r = np.delete(r,i-lens_count)
            lens_count = lens_count + 1
            
    blob_count = len(r) #determines white blob count by 
    
    image_gray = rgb2gray(invert(project_image))

    markers = np.zeros_like(image_gray)
    markers[image_gray > 0.86] = 1
    markers[image_gray <= 0.86] = 0

    blobs_dog = blob_dog(markers, max_sigma=sig_max, threshold=3*min_thr) #uses the 
    #built in 'Blob Detection' function that computes the Laplace of the Gaussian matrix 
    #of the image to identify, locate, and size blobs.

    xd = blobs_dog[:,1] #extracts the x coordinate information for each blob

    yd = blobs_dog[:,0] #extracts the y coordinate information for each blob

    rd = blobs_dog[:,2] #extracts the radius information for each blob

    numd = len(rd) #determines white blob count by 
    
    return x, y, r, blob_count, xl, yl, rl, lens_count, xd, yd, rd, numd

def graph_blobs(image, x, y, r, xl, yl, rl, xd, yd, rd):
    
    '''
    Short Summary
    -------------
    This function graphs the blobs over the original image as found from the function *blobs* 

    Position information is given as the x and y coodinates of the local maximum, assumed to be the center, of each blob found. Size is the average radius of the blob from the center to its  detected edge.

    Parameters
    ----------
    image : 2D array
                   image to be analyzed by the function
    x : list
              x position information of detected white blobs
    y : list
              y position information of detected white blobs
    r : list
              radius (size) information of detected white blobs       
    xl : list
              x position information of detected lenses
    yl : list
              y position information of detected lenses
    rl : list
              radius (size) information of detected lenses
    xd : list
              x position information of detected black blobs
    yd : list
              y position information of detected black blobs
    rd : list
              radius (size) information of detected black blobs
    
    Returns
    -------
    None
               
    '''
    
    import matplotlib.pyplot as plt
    import matplotlib.patches as pt
    from matplotlib.collections import PatchCollection
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True, sharey=True)
    titles = ['White Blobs','Lenses','Black Blobs']
    axes = axes.flatten()
    
    for title, ax in zip(titles,axes):
        ax.axis('off')
        ax.set_title('Image with Detected ' + str(title),fontsize=18)
        ax.imshow(image, cmap='gray')
    axes[3].axis('off')

    patch_list = []
    for x1, y1, r1 in zip(x, y, r):
        circle = pt.Circle((x1, y1), r1, color='lightgreen', linewidth=2, fill=True)
        patch_list.append(circle)
    p = PatchCollection(patch_list, alpha=0.4)
    axes[0].add_collection(p)

    patch_list2 = []
    for x2, y2, r2 in zip(xl, yl, rl):
        circle = pt.Circle((x2, y2), r2, color='lightgreen', linewidth=2, fill=True)
        patch_list2.append(circle)
    p2 = PatchCollection(patch_list2, alpha=0.4)
    axes[1].add_collection(p2)
    
    patch_list3 = []
    for x3, y3, r3 in zip(xd, yd, rd):
        circle = pt.Circle((x3, y3), r3, color='lightgreen', linewidth=2, fill=True)
        patch_list3.append(circle)
    p3 = PatchCollection(patch_list3, alpha=0.4)
    axes[2].add_collection(p3)
    
    return 
