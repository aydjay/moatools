import urllib.request
import re
import json

# todo: Caching for corporation and alliance ESI Calls


class Tools():

    i = 0

    characterIdCache = {}
    allianceIdCache = {}
    corpIdCache = {}
    typeIdCache = {}

    """Provides methods to solve small units of work"""

    def __init__(self):
        super(Tools).__init__()

    def GetCharacterAllegianceFromEsi(self, characterId):

        characterInfoUrl = "https://esi.tech.ccp.is/latest/characters/{}/?datasource=tranquility"
        corporationInfoUrl = "https://esi.tech.ccp.is/latest/corporations/{}/?datasource=tranquility"
        allianceInfoUrl = "https://esi.tech.ccp.is/latest/alliances/{}/?datasource=tranquility"

        response = self.GetResponseFromUrl(characterInfoUrl.format(characterId))
        data = json.loads(response)
        characterName = data['name']
        corpId = data['corporation_id']

        if corpId not in self.corpIdCache:
            response = self.GetResponseFromUrl(corporationInfoUrl.format(corpId))
            data = json.loads(response)
            self.corpIdCache[corpId] = [data['ticker'], data['alliance_id']]

        corpTicker = self.corpIdCache[corpId][0]
        allianceId = self.corpIdCache[corpId][1]

        if allianceId not in self.allianceIdCache:
            response = self.GetResponseFromUrl(allianceInfoUrl.format(allianceId))
            data = json.loads(response)
            self.allianceIdCache[allianceId] = data['alliance_name']

        allianceName = self.allianceIdCache[allianceId]

        return "{0} [{1}] {2}".format(characterName, corpTicker, allianceName)

    def GetPrettyPrintTypeId(self, typeId):
        "Get human readable translation of a typeId"
        if typeId not in self.typeIdCache:
            response = self.GetResponseFromUrl("https://esi.tech.ccp.is/latest/universe/types/{}/?datasource=tranquility&language=en-us".format(typeId))
            data = json.loads(response)
            self.typeIdCache[typeId] = data['name']

        name = self.typeIdCache[typeId]
        return "{}".format(name)

    def GetNamesFromZkillLinks(self, mail):
        "If someone mails you a load of zKill links, get the names of the victims for SRP purposes"
        for link in mail.splitlines():
            if "zkillboard.com/kill" not in link:
                continue

            killId = re.findall(r'\d+', link)

            newUrl = "https://zkillboard.com/api/killID/{}/no-attackers/no-items/".format(
                killId[0])

            killData = self.GetResponseFromUrl(newUrl)
            data = json.loads(killData)

            characterId = data[0]['victim']['character_id']
            typeId = data[0]['victim']['ship_type_id']

            print(self.GetCharacterAllegianceFromEsi(characterId) +
                  " " + self.GetPrettyPrintTypeId(typeId))

        print(self.i)

    def GetResponseFromUrl(self, link):
        self.i = self.i + 1
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2010021910 Firefox/3.0.7'
        headers = {'User-Agent': user_agent, }

        request = urllib.request.Request(link, None, headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        return data.decode("utf-8")

    def ShowNames(self, names):
        "Newline seperated names will return their allegiances"
        characterInFourl = "https://api.eveonline.com/eve/CharacterID.xml.aspx?names="
        seperated = names.splitlines()
        namesForUrl = ""

        for name in seperated:
            if " " in name:
                name = name.replace(" ", "%20")

            namesForUrl += name + ","

        namesForUrl = namesForUrl.strip(',')

        print(namesForUrl)

        characterInFourl += namesForUrl

        characterIdXml = self.GetResponseFromUrl(characterInFourl)
        print(characterIdXml)
        return
