from lzma import FILTER_LZMA1
from tqdm import tqdm

def compare(input_coord:str, input_address:str, outputfile:str):
    
    with open(input_coord) as file:
        number_place = 2
        street_place = 3
        with open(input_address) as file2:
            with open(outputfile, "w+") as outputfile:
                outputfile.write("NAME, BILLING_ADDRESS, HOME_ADDRESS, LON, LAT\n")
                lines1 = file.readlines()
                name = 0
                billing = 1
                home_address = 2
                lines2 = file2.readlines()
                digit1 = ''
                digit2 = ''
                
                file_address = ''
                file2_address = ''
                nums = 0
                nums2 = 0
                print(lines2[944])
                print(lines1[1])

                lines1 = lines1[1].split(",")
                lines2 = lines2[944].split(",")

                file_address = lines1[number_place] + " " + lines1[street_place]
                file2_address = lines2[home_address]

                print(file_address, file2_address)

                file2_address = file2_address.replace("STREET", "St")
                

                print(file_address, file2_address)
            
                # for x in file_address:
                #     if not x == ' ':
                #         file_address += x

                # for x in file2_address: 
                #     if not x == ' ':
                #         file2_address += x
                
                

                file_address = file_address.upper()
                file2_address = file2_address.upper()

                print(file_address, file2_address)
            

                if file_address == file2_address:
                    print("Correct")
                elif file_address != file2_address:
                    print("BAD")
                    outputfile.write(file_address)
                    outputfile.write(file2_address)

                # for x in tqdm(lines1):
                #     if nums == 0:
                #         nums += 1
                #         continue
                    
                #     else:
                #         x = x.split(",")

                #         file_address = x[number_place] +  " " + x[street_place]

                        
                #         nums += 1
                        

                #     for i in lines2:
                #         if nums2 == 0:
                #             nums2 += 1
            
                #         else:
                #             f = i
                #             i = i.split(",")

                #             file2_address = i[home_address]

                #             nums2 += 1
                            
                #         file2_address = file2_address.replace("STREET", "St")
                #         print(file_address.upper(), "\n", file2_address.upper())
                #         if file_address.upper() == file2_address.upper():
                #             outputfile.write(f + ", " + x[0] + ", " + x[1] + "\n")
                #         break



                        
                    


            













compare("../Output/Address_Coordinates/coords.csv", "../Output/Img_to_Text/output.csv", "../Output/address_and_coords/all_together.csv" )