from Startup.lake_extractor import csv_write_lake_coords
from Startup.address_extractor import csvwrite_address_lines
from pdf_to_img import Convert_to_PNG
from img_cropper import cropPNG
from img_to_text import format_text
from compare_address_with_coordinates import compare

kml = "../Input/lake_extractor/Given/Kezar.kml" # should be .kml of the google earth lake at the end 

lake_coords_dir = "../Output/Lake_Coordinates/" # should be dir of the lake coordinates at the end
statewide_address = "../Input/address_extractor/Already Had/me_statewide.csv" # should be .csv at the end of this
address_coords_file_output = "../Output/Address_Coordinates/coords.csv" # should be file at the end of this
zip_code = "04364" # Should be the postal code
commitment_pdf = '../Input/img_to_text/Given/Winthrop_Commitment.pdf' # should be a .pdf file of a tax commitment book at the end
pdf_to_png = '../Temp_Files/Convert_to_PNG/' # should be a dir of the converted from pdf to png at the end
image_cropped = '../Temp_Files/Img_Cropper/' # shoudld be the dir of the cropped images at the end 
img_text = "../Output/Img_to_Text/im_to_txt_output.csv" # should be the .csv file of the 
output_for_address_compare = "../Output/address_and_coords/addresses_together.csv" # should be a file in the output folder at the end of this

if __name__ == "__main__":
    
    csv_write_lake_coords(kml, lake_coords_dir)
    csvwrite_address_lines(statewide_address, address_coords_file_output, zip_code)
    Convert_to_PNG(commitment_pdf, pdf_to_png)
    cropPNG(pdf_to_png, image_cropped)
    format_text(image_cropped, img_text)
    compare(address_coords_file_output, img_text, output_for_address_compare)



