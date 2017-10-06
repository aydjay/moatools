import urllib.request
import string
import bin.xmlutil

def ShowNames(names):
    "Newline seperated names will return their allegiances"
    characterIdUrl = "https://api.eveonline.com/eve/CharacterID.xml.aspx?names="
    characterAffiliationUrl = "https://api.eveonline.com/eve/CharacterAffiliation.xml.aspx?ids="
    seperated = names.splitlines()
    namesForUrl = ""

    for name in seperated:
        if " " in name:
            name = name.replace(" ", "%20")
        
        namesForUrl += name + ","

    namesForUrl = namesForUrl.strip(',')

    print(namesForUrl)
    
    characterIdUrl += namesForUrl

    characterIdXml = GetResponseFromUrl(characterIdUrl)
    print(characterIdXml)
    return

def GetResponseFromUrl(characterIdUrl):
    return urllib.request.urlopen(characterIdUrl).read()