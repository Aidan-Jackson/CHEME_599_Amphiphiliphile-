def miwa_blob_detection(image_name):

    import numpy as np
    import skimage as sk
    from skimage import io

    from skimage.color import rgb2gray
    from skimage.util import pad, img_as_float, img_as_ubyte
    from skimage.filters import rank
    from skimage.morphology import square, disk, star
    from skimage.morphology import opening as gs_opening
    from skimage.morphology import closing as gs_closing

    from skimage.feature import blob_dog, blob_log, blob_doh

    import matplotlib.pyplot as plt

    original = io.imread(image_name)
    fig, axes = plt.subplots(ncols=2,figsize=(10,15))
    for ax in axes:
        ax.axis('off')
    axes[0].imshow(original, cmap='gray')
    axes[0].title.set_text('Original Image')
    axes[1].imshow(1-original, cmap='gray')
    axes[1].title.set_text('Original Image Inverted')
    plt.show()

    grayscale = rgb2gray(original)
    byte = img_as_ubyte(grayscale)

    opened = gs_opening(byte, disk(7))
    inverted = 1-opened
    fig, axes = plt.subplots(ncols=2,figsize=(10,15))
    for ax in axes:
        ax.axis('off')
    axes[0].imshow(1-original, cmap='gray')
    axes[0].title.set_text('Original Image Inverted')
    axes[1].imshow(inverted, cmap='gray')
    axes[1].title.set_text('Opened Image Inverted')
    plt.show()

    blurred = rank.mean(inverted,square(8))
    fig, axes = plt.subplots(ncols=2,figsize=(10,15))
    for ax in axes:
        ax.axis('off')
    axes[0].imshow(1-original, cmap='gray')
    axes[0].title.set_text('Original Image Inverted')
    axes[1].imshow(blurred, cmap='gray')
    axes[1].title.set_text('Opened, Inverted, and Blurred Image')

    maximum=max(map(max,blurred))
    minimum=min(map(min,blurred))
    ordinal=np.linspace(minimum,maximum,15)
    plt.hist(blurred,bins=ordinal)
    plt.show()

    clipped=blurred
    for i in range(0,512):
        for j in range(0,512):
            if clipped[i][j] > 140:
                clipped[i][j] = 250

    fig, axes = plt.subplots(ncols=2,figsize=(10,15))
    for ax in axes:
        ax.axis('off')
    axes[0].imshow(1-original, cmap='gray')
    axes[0].title.set_text('Original Image Inverted')
    axes[1].imshow(clipped, cmap='gray')
    axes[1].title.set_text('Opened Image Inverted')
    plt.show()

    manipulate = blob_doh(clipped,max_sigma=35,num_sigma=10,threshold=.01)

    fig, ax = plt.subplots(ncols=3, figsize=(15, 5))
    ax[0].imshow(original)
    ax[0].set_title('Original Image')
    ax[0].set_axis_off()
    ax[1].imshow(clipped,cmap='gray')
    ax[1].set_title('Enhanced Image')
    ax[1].set_axis_off()
    ax[2].imshow(original)
    ax[2].set_title('Processed Image with Edge Detection')
    ax[2].set_axis_off()

    blob_list=[]
    for blob in manipulate:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
        blob_list.append(r)
        ax[2].add_patch(c)
    plt.show()

    count=len(blob_list)
    avg_rad=(sum(blob_list)/count)
    avg_dia=2*avg_rad

    print('The number of detected blobs is {}.'.format(count))
    print('The average diameter of these blobs is {}.'.format(round(avg_dia,1)))
