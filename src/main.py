from Startup.lake_extractor import csv_write_lake_coords
from Startup.address_extractor import csvwrite_address_lines
from pdf_to_img import Convert_to_PNG
from img_cropper import cropPNG
from img_to_text import format_text

if __name__ == "__main__":
    csv_write_lake_coords("../Input/lake_extractor/Kezar.kml", "../Output/Lake_Coordinates/")
    csvwrite_address_lines("../Input/address_extractor/me_statewide.csv","../Output/Address_Coordinates/",  "04364")
    Convert_to_PNG('../Input/img_to_text/Winthrop_Commitment.pdf', '../Temp_Files/Convert_to_PNG/')
    cropPNG('../Temp_Files/Convert_to_PNG/', '../Temp_Files/Img_Cropper/')
    format_text('../Temp_Files/Img_Cropper/', "../Output/Img_to_Text/output.csv")

