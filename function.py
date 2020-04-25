test_image = plt.imread('project_image.jpg') #Reads in an example test image

#This function identifies the number, location, and size of white blobs within a single image by
#using one of the skimage.feature blob detection functions. 
#Lenses, a white particle on top of a black one, are also counted individually and the same
#values are tracked. 
#Function is passed an image [project_image] as a 2D array, the maximum standard deviation 
# [sig_max] to accept when searching for a blob (which is analogous to maximum allowable 
# blob size), and the intensity threshold at which it will first consider a blob to be found
# at [min_thr] computed as a fraction of the maximum intensity in the image. 
def blobs (project_image,sig_max,min_thr): 
    
    #The position, size, and number of blobs in an image
    
#Position information is given as the x and y coodinates of the local maximum, assumed to be the
#center, of each blob found. Size is the average radius of the blob from the center to its  detected edge. 

#Parameters
#-----------
#project_image : 2D array
#               image to be analyzed by the function
                
#sig_max : int
#          maximum standard deviation for use in finding the Gaussian matrix of the image.
#          Proportional to the maximum allowable size of blobs that can be detected.
          
# min_thr : float
#         minimum intensity threshold for which the function determines the local maxima (center)
#          of the blob 

#Returns
#-------

#x : list 
#             X-Coordinate of detected blobs
             
#y : list 
#             Y-Coordinate of detected blobs
             
#r : list 
#             radius (size) of detected blobs
           
#blob_count : int
#             Number of blobs found in the image
    
    
    blobs_dog = blob_dog(project_image, max_sigma=sig_max, threshold=min_thr) #uses the 
    #built in 'Blob Detection' function that computes the Laplace of the Gaussian matrix 
    #of the image to identify, locate, and size blobs.
    
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
    
    return x, y, r, blob_count, xl, yl, rl, lens_count
    #returns the x,y position and radius r size information,
    #and the number of total blobs. Radius is the computed
    #blob size if it were to form a perfect circle
