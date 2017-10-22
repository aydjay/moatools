import urllib.request
import string
from io import StringIO, BytesIO
import re
import json

#todo: Caching for corporation and alliance ESI Calls


def GetCharacterAllegianceFromEsi(characterId):
    response = GetResponseFromUrl("https://esi.tech.ccp.is/latest/characters/{}/?datasource=tranquility".format(characterId))
    data = json.loads(response)
    characterName = data['name']
    corpId = data['corporation_id']

    response = GetResponseFromUrl("https://esi.tech.ccp.is/latest/corporations/{}/?datasource=tranquility".format(corpId))
    data = json.loads(response)
    corpName = data['corporation_name']
    corpTicker = data['ticker']
    allianceId = data['alliance_id']

    response = GetResponseFromUrl("https://esi.tech.ccp.is/latest/alliances/{}/?datasource=tranquility".format(allianceId))
    data = json.loads(response)
    allianceName = data['alliance_name']

    return "{0} [{1}] {2}".format(characterName, corpTicker, allianceName)

def GetPrettyPrintTypeId(typeId):
    response = GetResponseFromUrl("https://esi.tech.ccp.is/latest/universe/types/{}/?datasource=tranquility&language=en-us".format(typeId))
    data = json.loads(response)

    return "{}".format(data['name'])

def GetNamesFromZkillLinks(mail):
    "If someone mails you a load of zKill links, get the names of the victims for SRP purposes"
    for link in mail.splitlines():
        if "zkillboard.com/kill" not in link:
            continue

        killId = re.findall(r'\d+', link)

        newUrl = "https://zkillboard.com/api/killID/{}/no-attackers/no-items/".format(killId[0])

        killData = GetResponseFromUrl(newUrl)
        data =  json.loads(killData)

        characterId = data[0]['victim']['character_id']
        typeId = data[0]['victim']['ship_type_id']


        print(GetCharacterAllegianceFromEsi(characterId) + " " + GetPrettyPrintTypeId(typeId))




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
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2010021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}

    request=urllib.request.Request(link,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    return data.decode("utf-8")
