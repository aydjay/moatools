import urllib
import string






def ShowNames(names):
    "Newline seperated names will return their allegiances"
    seperated = names.splitlines()

    for name in seperated:
        if " " in name:
            name = name.replace(" ", "%20")
        
        print(name)



    
    return



