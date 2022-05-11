from PIL import Image
import numpy as np
import os 
from tqdm import tqdm

def cropPNG(inputdir:str, outputdir:str):
    '''inputdir should just be the folder you want to extract all of the pgn images from, or in other words, it should be
    the outputdir from Convert_to_PNG() '''
    
    print("Now Cropping all PNG Files")
    address_num = 0
    for x in tqdm(os.listdir(inputdir)):
    
        im = Image.open(inputdir + x).convert('L')
        region = np.asarray(im.crop([220, 192, 581, 2000]))
        #toShow = im.crop([220, 192, 581, 2000]).save('image.png')
        # Find the row numbers of the black lines
        i = 0
        row_nums = []
        for row in region:
            if (row < 100).all():
                row_nums.append(i)
            i += 1

        # Get rid of duplicate row numbers
        row_nums = np.asarray(row_nums)
        rows = []
        for numCheck in row_nums:
            diff = row_nums - np.full(row_nums.shape, numCheck)
            diff = diff[diff != 0]

            if -1 not in diff:
                rows.append(numCheck)

        # Crop the images using the row numbers
        croppedImages = []
        i = 0
        for row in rows:

            if not i + 1 >= len(rows):
                croppedImages.append(Image.fromarray(region).crop([0, row + 2, 361, rows[i+1]]))
                i += 1
            else:
                croppedImages.append(Image.fromarray(region).crop([0, row + 2, 361, 1808]))

        # Save the cropped address images
    
        for image in croppedImages:
            image.save(outputdir + 'address_' + str(address_num) + '.png')
            address_num += 1
        number_of_addresses = "There are "+ str(address_num) + "Addresses"
        
    return number_of_addresses

    
# cropPNG('PNG_Images/', '../Output/Img_Cropper/Cropped_PNG/')

    


    
    
            





