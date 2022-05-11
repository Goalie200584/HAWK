from email.mime import image
from pyexpat import XML_PARAM_ENTITY_PARSING_ALWAYS
from Startup.lake_extractor import csv_write_lake_coords
from Startup.address_extractor import csvwrite_address_lines
from pdf_to_img import Convert_to_PNG
from img_cropper import cropPNG
from img_to_text import format_text
from compare_address_with_coordinates import compare

kml = "../Input/lake_extractor/Kezar.kml" # should be .kml of the google earth lake at the end 

lake_coords_dir = "../Output/Lake_Coordinates/" # should be dir of the lake coordinates at the end
statewide_address = "../Input/address_extractor/me_statewide.csv" # should be .csv at the end of this
address_coords_dir = "../Output/Address_Coordinates/" # should be dir at the end of this
zip_code = "04364" # Should be the postal code
commitment_pdf = '../Input/img_to_text/Winthrop_Commitment.pdf' # should be a .pdf file of a tax commitment book at the end
pdf_to_png = '../Temp_Files/Convert_to_PNG/' # should be a dir of the converted from pdf to png at the end
image_cropped = '../Temp_Files/Img_Cropper/' # shoudld be the dir of the cropped images at the end 
img_text = "../Output/Img_to_Text/im_to_txt_output.csv" # should be the .csv file of the 

if __name__ == "__main__":
    
    csv_write_lake_coords(kml, lake_coords_dir)
    csvwrite_address_lines(statewide_address, address_coords_dir, zip_code)
    Convert_to_PNG(commitment_pdf, pdf_to_png)
    cropPNG(pdf_to_png, image_cropped)
    format_text(image_cropped, img_text)



