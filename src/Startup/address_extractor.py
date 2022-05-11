# This program will extract the line numbers with the specific zip code, or zip codes from the statewide.csv file 
# then have another function that takes
# said line numbers and prints the lines from each of those into another csv file so its ready to compare with 
# the tax commitment books for the coordinates of a specific address
lines_with_postcode = []
def line_numbers(post_code:str, statewide_csv_dir:str):
    
    with open(statewide_csv_dir) as file:
        lines = file.readlines()
        index_needed_for_find = 8 
        line_num = 1

        for x in lines:
            if line_num == 1:
                line_num += 1
                continue
            elif line_num > 1:
                x = x.split(",")
                if x[8] == post_code:
                    lines_with_postcode.append(line_num)
                line_num += 1

            
def csvwrite_address_lines( statewide_csv_dir:str, outputfile:str, post_code:str):
    line_numbers(post_code, statewide_csv_dir)
    output_file = outputfile
    with open(statewide_csv_dir) as file:
        lines = file.readlines()
        with open(output_file, "x+") as file2:
            file2.write("LON,LAT,NUMBER,STREET,UNIT,CITY,DISTRICT,REGION,POSTCODE,ID,HASH\n")
            for x in lines_with_postcode:
                file2.write(lines[x - 1])
    
    
    


        
        
         
            






