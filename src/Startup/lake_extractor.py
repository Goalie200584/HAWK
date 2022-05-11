#Coord_Lines is where the line numbers for the coordinates from the .kml file are stored
coord_lines = []

def find_coordinates_line(filedir:str):
    '''Finds the line numbers of the line in the .kml file that houses all the coordinates
    so it can then be written onto a .csv file'''
    with open(filedir) as file:
        lines = file.readlines()
        line_num = 1
        for x in lines:
            if line_num == 1:
                assert x == '<?xml version="1.0" encoding="UTF-8"?>\n', "Improper encoding found in lake polygon file."
            if x.endswith("<coordinates>\n"):
                line_num += 1
                coord_lines.append(line_num)
                
            else:
                line_num += 1 



def csv_write_lake_coords(filedir:str, outputdir:str):
    '''Takes the line numbers from find_coordinates_line and takes all of the coordinates and writes to to a .csv
    in the order "Lon, Lat, Alt"'''
    find_coordinates_line(filedir)
    number_of_indents = 0
    
    if len(coord_lines) == 1:
        number_of_indents = 0
    elif len(coord_lines) >= 2:
        number_of_indents = 1

    with open(filedir) as file:
        lines = file.readlines()
        csv_writes = 0  #The number of csv files written so far
        
        for x in coord_lines:
            coordinates = lines[x - 1]
            coordinates = coordinates.split(" ")
            
            if csv_writes == 0:
                with open(outputdir + "lake_coords.csv", "x+") as file2:
                    file2.write("Longitude,Latitude,Altitude\n")
                    for i in coordinates:
                        if i == coordinates[0]:
                            file2.write(i[6 + number_of_indents:] + "\n")
                        else:
                            file2.write(i + "\n")
                    csv_writes += 1

            else:
                with open(outputdir + "lake_coords_is" + str(csv_writes) + ".csv", "x+") as file2:
                    file2.write("Longitude,Latitude,Altitude\n")
                    for i in coordinates:
                        if i == coordinates[0]:
                            file2.write(i[6 + number_of_indents:] + "\n")
                        else:
                            file2.write(i + "\n")
                    csv_writes += 1

                    












