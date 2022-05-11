import os
import math


def find_water_front(inputadd: str, inputlake_dir: str, outputdir: str, distance: float) -> None: # distance in meters
    num_of_files = os.listdir(inputlake_dir)
    

    with open(inputadd) as file:
        with open(outputdir, "x+") as outputfile:
            outputfile.write("NAME, BILLING_ADDRESS, HOME_ADDRESS, LON, LAT")
            for i in range(len(num_of_files)):
                if i == 0:
                    csv_name = "lake_coords.csv"
                elif i > 0:
                    csv_name = "lake_coords_is_" + str(i) + ".csv"
                
                with open(inputlake_dir + csv_name) as file2:
                    lines1 = file.readlines()
                    lines2 = file2.readlines()
                    p = 0
                    for x in lines1:
                        if p == 0:
                            continue
                        x = x.split(",")
                        lon1 = float(x[-2])
                        lat1 = float(x[-1])
                        for v in lines2:
                            
                            lakelon = float(v[0])
                            lakelat = float(v[1])
                            true_or_false = determine_water_front(lon1, lat1, lakelon, lakelat, distance)

                            if true_or_false == True:
                                outputfile.write(x)
                            elif true_or_false == False:
                                print("BAD")
                                break
                        
                        p += 1

                        

                        

def determine_water_front(lon1: float, lat1: float, lakelon: float, lakelat: float, distance: float) -> bool:
    EARTHRADIUS_M = 6371000
    PI = math.pi

    lon1 = float(lon1) * PI/180
    lon2 = float(lakelon) * PI/180
    lat1 = float(lat1) * PI/180
    lat2 = float(lakelat) * PI/180

    deltaLon = lon2 - lon1
    deltaLat = lat2 - lat1

    a = math.sin(deltaLat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(deltaLon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = EARTHRADIUS_M * c

    if d < distance:
        return True
    elif d > distance:
        return False

                        

                
            
            
find_water_front("../Output/address_and_coords/addresses_together.csv", "../Output/Lake_Coordinates/", "../Lakefront_Properties/lakefront_properties.csv", 100)
