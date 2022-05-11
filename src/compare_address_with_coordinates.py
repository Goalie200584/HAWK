from tqdm import tqdm
import utils

def compare(input_coord:str, input_address:str, outputfile:str):
    
    with open(input_coord) as file:
        number_place = 2
        street_place = 3
        with open(input_address) as file2:
            with open(outputfile, "x+") as outputfile:
                outputfile.write("NAME, BILLING_ADDRESS, HOME_ADDRESS, LON, LAT\n")
                lines1 = file.readlines()
                name = 0
                billing = 1
                home_address = 2
                lines2 = file2.readlines()
                
                file_address = ''
                file2_address = ''
                nums = 0
                nums2 = 0
                

                for x in tqdm(lines1):
                    if nums == 0:
                        nums += 1
                        continue
                    
                    else:
                        x = x.split(",")

                        file_address = x[number_place] + x[street_place]

                        
                        nums += 1
                        

                    for i in lines2:
                        if nums2 == 0:
                            nums2 += 1
                            continue
            
                        else:
                            f = i
                            i = i.split(",")

                            file2_address = i[home_address]

                            nums2 += 1
                        file_address = utils.format_addresses(file_address)
                        file2_address = utils.format_addresses(file2_address)
                        
                        # file_address = file_address.lower()
                        # file2_address = file2_address.lower()

                        file_address = utils.remove_whitespace(file_address)
                        file2_address = utils.remove_whitespace(file2_address)
                        
                        
                        if file_address == file2_address:
                            f = f.replace("\n", '')
                            outputfile.write(f + ", " + x[name] + ", " + x[billing] + "\n")
                        



                        
                    


            













compare("../Output/Address_Coordinates/coords.csv", "../Output/Img_to_Text/output.csv", "../Output/address_and_coords/all_together.csv" )