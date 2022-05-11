def remove_whitespace(inputstr:str) -> str:
    '''Removes all whitespace in a string and
       returns the new string.
    '''
    inputstr = inputstr.replace(' ', '').replace('\t', '').replace('\n', '')
    return inputstr

def format_addresses(inputstr:str) -> str:
    
    inputstr = inputstr.upper().replace("STREET", "st").replace("AVENUE", "ave").replace("ROAD", "rd").replace("LANE", "ln").replace("DRIVE", "dr")
    inputstr = inputstr.upper().replace("EAST", 'e ').replace("SOUTH", "s ").replace("WEST", 'w ').replace("NORTH", 'n ')
    inputstr = inputstr.upper().replace("COURT", "ct").replace("TRAIL", "trl").replace("ISLAND", 'is').replace("\s", '').replace("ALLEY", "aly")
    inputstr = inputstr.upper().replace("US ROUTE", "us").replace("BOULEVARD", "BLVD").replace("CAUSEWAY", "cswy").replace("CENTER", "ctr").replace("CIRLCE", "cir")
    inputstr = inputstr.upper().replace("COVE", "cv").replace("CROSSING", "xing").replace("EXPRESSWAY", "expy").replace("EXTENSION", "ext").replace("FREEWAY", "fwy")
    inputstr = inputstr.upper().replace("GROVE", "grv").replace("HIGHWAY", "hwy").replace("HOLLOEW", "holw").replace("JUNCTION", "jct").replace("MOTORWAY", "mtwy").replace("OVERPASS", "opas")
    inputstr = inputstr.upper().replace("PARKWAY", "pkwy").replace("PLACE", "pl").replace("PLAZA", 'plz').replace("POINT", "pt").replace("SKYWAY", "skwy").replace("SQUARE", "sq").replace("TERRACE", "ter")
    inputstr = inputstr.lower()
    
    return inputstr


    