# import module
from pdf2image import convert_from_path
from tqdm import tqdm
 
def Convert_to_PNG(inputdir:str, outputdir:str):
    filename = inputdir.split('/')[-1]
    filename = filename.split('.')[0]
    # Store Pdf with convert_from_path function
    print("Starting to convert to PNG")
    images = convert_from_path(inputdir)
    print("Done with Convert, Now Creating and Pasting")
    



    for i in tqdm(range(len(images))):
    
        # Save pages as images in the pdf
        images[i].save(outputdir + filename + str(i) + '.png', 'PNG')





    