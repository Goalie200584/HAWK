from turtle import home
from PIL import Image
import numpy as np
import pytesseract as pt
import os 
import re
from tqdm import tqdm



text = []
def get_text(inputdir:str):
    files = os.listdir(inputdir) 
    num_of_images = len(files)
    
    img_counter = 0
    print("Extracting the text from the cropped images")
    for image in tqdm(range(num_of_images)):
        filename = inputdir + 'address_' + str(img_counter) + '.png'
        text_from_img = pt.image_to_string(filename)
        text.append(text_from_img)
        img_counter += 1
    return text
    # text_from_img = pt.image_to_string(inputdir + "address_1733.png")
    # text.append(text_from_img)
    # return text
    
    


    

def format_text(inputdir:str, outputdir:str):
    text = get_text(inputdir) 
    with open(outputdir, "w+") as file:
        file.write("NAME,BILLING_ADDRESS,HOME_ADDRESS\n")
        for image_text in tqdm(text):
            lines = 0
            indicator = -1
            home_line = 0
            zip_line = 0
            billing_line = 0
            name_list = []
            name = ''
            billing = ''
            home_address = ''
            image_text = image_text.split("\n")

            for line_text in image_text:
                if line_text == '':
                    lines += 1
                    continue

                #searches for zip_code in the line
                elif re.search('\s?[0-9]{5}(?:-[0-9]{1,4})?(\s.*)?$', line_text):
                    zip_line = lines
                    billing_line = lines - 1
                    indicator = 1
                
                elif not line_text == ""     and indicator == 1:
                    home_line = lines
                    indicator = -1


                lines += 1
            if image_text[billing_line] == '':
                billing_line -= 1


            if not re.search(";:!@#$%^&*()-+=", image_text[billing_line - 1]):
                name_list = image_text[0:billing_line]
            elif re.search(";:!@#$%^&*()-+=", image_text[billing_line - 1]):
                name_list = image_text[0:billing_line - 1]
            
            i = 0
            for j in name_list:
                if name_list[i] == name_list[-1]:
                    name += j
                    i += 1
                else:
                    name += j + " "
                    i += 1


            billing = image_text[billing_line] + ' '+ image_text[zip_line]
            home_address = image_text[home_line] + ""


            name = name.replace(",", ";")
            billing = billing.replace(",", ";")
            home_address = home_address.replace(",", ";")
            writing = name + "," + billing + ',' + home_address + "\n"

            file.write(writing)

            
image_cropped = '../Temp_Files/Img_Cropper/'
img_text = "../Output/Img_to_Text/im_to_txt_output.csv"
        

format_text(image_cropped, img_text)
        






        



        
                    
    

                    


        








