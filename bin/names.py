import urllib.request
import string
from lxml import etree
from io import StringIO, BytesIO

def ParseHtmlWithXPath(htmlPagem,xpath):
    print("Called Successfully")
    return

def GetNamesFromZkillLinks(mail):
    "If someone mails you a load of zKill links, get the names of the victims for SRP purposes"
    for link in mail.splitlines():
        if "zkillboard.com/kill" not in link:
            continue
        print(GetResponseFromUrl(link))


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

def GetResponseFromUrl(link):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(link,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    return data