#!/usr/bin/python

import requests
from tabulate import tabulate
from urlparse import parse_qs
from BeautifulSoup import BeautifulSoup

def headerList():
    list = []
    list.append("Name")
    list.append("Country")
    list.append("Years")
    list.append("A.F.")
    list.append("Talent")
    list.append("Strength")
    list.append("Speed")
    list.append("Mentality")
    list.append("Endurance")
    list.append("Skill")
    list.append("Service")
    list.append("Doubles")
    list.append("Cost")
    #list.append("{} ({})".format("Max Strength", "Order"))
    #list.append("{} ({})".format("Max Speed", "Order"))
    #list.append("{} ({})".format("Max Endurance", "Order"))
    #list.append("Max Skill")
    #list.append("Max Service")
    list.append("Trainer")
    return list


def createPlayer(playerhtml):
    player = Player()
    namehtml = playerhtml.next
    player.setExtra(parse_qs(namehtml.next.next['href'])['extra'][0])
    player.setName(namehtml.next.next.string)
    countryhtml = namehtml.nextSibling
    player.setCountry(countryhtml.next.next['title'])
    yearshtml = countryhtml.nextSibling
    player.setYears(yearshtml.string)
    agehtml = yearshtml.nextSibling
    player.setAge(agehtml.string)
    talenthtml = agehtml.nextSibling
    player.setTalent(float(value(talenthtml)))
    strengthhtml = talenthtml.nextSibling
    player.setStrength(float(value(strengthhtml)))
    speedhtml = strengthhtml.nextSibling
    player.setSpeed(float(value(speedhtml)))
    mentalityhtml = speedhtml.nextSibling
    player.setMentality(float(value(mentalityhtml)))
    endurancehtml = mentalityhtml.nextSibling
    player.setEndurance(float(value(endurancehtml)))
    skillhtml = endurancehtml.nextSibling
    player.setSkill(float(value(skillhtml)))
    servicehtml = skillhtml.nextSibling
    player.setService(float(value(servicehtml)))
    doubleshtml = servicehtml.nextSibling
    player.setDoubles(float(value(doubleshtml)))
    costhtml = doubleshtml.nextSibling
    player.setCost(int(cost(costhtml)))
    return player


def value(entry):
    if len(entry.contents) == 1:
        return entry.next.string
    else:
        return entry.next.string + entry.next.next.string

def cost(entry):
    if not entry.string:
        return entry.next.string
    else:
        return entry.string

class Player:
    def __init__(self):
        pass

    def getExtra(self):
        return self.extra

    def setExtra(self, extra):
        self.extra = extra

    def setName(self, name):
        self.name = name

    def setCountry(self, country):
        self.country = country

    def setYears(self, years):
        self.years = years

    def setAge(self, age):
        self.age = age

    def getTalent(self):
        return self.talent

    def setTalent(self, talent):
        self.talent = talent

    def setStrength(self, strength):
        self.strength = strength

    def setSpeed(self, speed):
        self.speed = speed

    def getMentality(self):
        return self.mentality

    def setMentality(self, mentality):
        self.mentality = mentality

    def setEndurance(self, endurance):
        self.endurance = endurance

    def setSkill(self, skill):
        self.skill = skill

    def setService(self, service):
        self.service = service

    def getDoubles(self):
        return self.doubles

    def setDoubles(self, doubles):
        self.doubles = doubles

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

    def setAgePercentage(self, agePercentage):
        self.agePercentage = agePercentage

    def getMaxStrength(self):
        return self.maxStrength

    def getMaxSpeed(self):
        return self.maxSpeed

    def getMaxEndurance(self):
        return self.maxEndurance

    def getTrainer(self):
        return self.trainer

    def getTotal(self):
        return self.total

    def setTalentOrder(self, order):
        self.talentOrder = order

    def setMentalityOrder(self, order):
        self.mentalityOrder = order

    def setMaxStrengthOrder(self, order):
        self.maxStrengthOrder = order

    def setMaxSpeedOrder(self, order):
        self.maxSpeedOrder = order

    def setMaxEnduranceOrder(self, order):
        self.maxEnduranceOrder = order

    def calculateStats(self):
        self.maxStrength = round(self.strength / self.agePercentage, 1)
        self.maxSpeed = round(self.speed / self.agePercentage, 1)
        self.maxEndurance = round(self.endurance / self.agePercentage / self.agePercentage, 1)
        self.maxSkill = round(self.skill / self.agePercentage, 1)
        self.maxService = round(self.service / self.agePercentage, 1)
        self.skillPoints = self.maxSkill * 20
        self.servicePoints = self.maxService * 20
        self.doublesPoints = self.doubles * 20
        self.trainer = round((self.maxSkill + 0.75 * self.maxService + 0.33 * self.doubles)/2.3, 1)

    def calculateTotal(self):
        #self.total = 3 * self.talentOrder + 0.5 * self.mentalityOrder + 1.5 * self.maxStrengthOrder + self.maxSpeedOrder + 3 * self.maxEnduranceOrder
        pass

    def toList(self):
        list = []
        list.append(self.name)
        list.append(self.country)
        list.append("{} ({}%)".format(self.years, int(self.agePercentage * 100)))
        list.append(self.age)
        list.append("{} ({})".format(self.talent, self.talentOrder))
        list.append("{} ({} ({}))".format(self.strength, self.maxStrength, self.maxStrengthOrder))
        list.append("{} ({} ({}))".format(self.speed, self.maxSpeed, self.maxSpeedOrder))
        list.append("{} ({})".format(self.mentality, self.mentalityOrder))
        list.append("{} ({} ({}))".format(self.endurance, self.maxEndurance, self.maxEnduranceOrder))
        list.append("{} ({} - {})".format(self.skill, self.maxSkill, int(self.skillPoints)))
        list.append("{} ({} - {})".format(self.service, self.maxService, int(self.servicePoints)))
        list.append("{} - {}".format(self.doubles, int(self.doublesPoints)))
        list.append(self.cost)
        #list.append("{} ({})".format(self.maxStrength, self.maxStrengthOrder))
        #list.append("{} ({})".format(self.maxSpeed, self.maxSpeedOrder))
        #list.append("{} ({})".format(self.maxEndurance, self.maxEnduranceOrder))
        #list.append(self.maxSkill)
        #list.append(self.maxService)
        list.append(self.trainer)
        return list


def fetchPlayerInfo(player, cookies):
    playerparams = {'page': 'player', 'extra': player.getExtra()}
    playerrequest = requests.get("http://" + gameworld + "." + mainurl, params = playerparams, cookies = cookies)

    playerhtml = BeautifulSoup(playerrequest.text)
    tree = playerhtml.body

    for content in tree:
        if not content.string:
            if content.name == 'div' and content['class'] == 'body':
                tree = content
                break

    for content in tree:
        if not content.string:
            if content.name == 'div' and content['class'] == 'content':
                tree = content
                break

    for content in tree:
        if not content.string:
            if content.name == 'form': #and content['class'] == 'content':
                tree = content
                break

    for content in tree:
        if not content.string:
            if content.name == 'p' and content['class'] == 'doubles_partner':
                tree = content
                break

    for content in tree:
        if not content.string:
            if content.name == 'table' and content['class'] == 'player_infotable':
                tree = content
                break

    playerhtml = tree
    for infohtml in playerhtml:
        if infohtml.next.string == "Age":
            ageInfos = infohtml.contents[1].string.split(" ")
            player.setYears(ageInfos[0])
            player.setAgePercentage(round(float(ageInfos[1].replace("(", "").replace(")", "").replace("%", "")) / 100, 2))

def search():
    category = input("Categories ([1] 14-; [2] 15_16; [3] 17_18; [4] 19_20; [5] 21_23; [6] 24_26; [7] 27): ")
    subsubpage = subsubpages[category]

    start = 1
    doubles = True
    while doubles:
        sortparam = 'doubles'
        playersparams = {'page':'players', 'subpage':'free', 'subsubpage':subsubpage, 'start':start, 'sort':sortparam}
        playersrequest = requests.get("http://" + gameworld + "." + mainurl, params = playersparams, cookies = loginrequest.cookies)

        playershtml = BeautifulSoup(playersrequest.text)
        tree = playershtml.body

        for content in tree:
            if not content.string:
                if content.name == 'div' and content['class'] == 'body':
                    tree = content
                    break

        for content in tree:
            if not content.string:
                if content.name == 'div' and content['class'] == 'content':
                    tree = content
                    break

        first = False
        for content in tree:
            if not content.string:
                if content.name == 'table' and content['class'] == 'realtable':
                    #tree = content
                    #break
                    if first is False:
                        first = True
                    else:
                        tree = content
                        break

        playershtml = tree
        headerhtml = playershtml.next
        headerhtml.extract()

        for playerhtml in playershtml:
            player = createPlayer(playerhtml)
            if float(player.getDoubles() < 5):
                doubles = False
                break

            if player.getExtra() not in playersdict:
                fetchPlayerInfo(player, loginrequest.cookies)
                player.calculateStats()
                playersdict[player.getExtra()] = player
        start += 1

def show():
    players = playersdict.values()

    list.sort(players, key = lambda player: player.getMaxStrength(), reverse = True)
    order = 0
    acc = 1
    previousPlayerMaxStrength = 5.0
    for player in players:
        currentPlayerMaxStrength = player.getMaxStrength()
        if currentPlayerMaxStrength == previousPlayerMaxStrength:
            acc += 1
        else:
            previousPlayerMaxStrength = currentPlayerMaxStrength
            order += acc
            acc = 1
        player.setMaxStrengthOrder(order)

    list.sort(players, key = lambda player: player.getMaxSpeed(), reverse = True)
    order = 0
    acc = 1
    previousPlayerMaxSpeed = 5.0
    for player in players:
        currentPlayerMaxSpeed = player.getMaxSpeed()
        if currentPlayerMaxSpeed == previousPlayerMaxSpeed:
            acc += 1
        else:
            previousPlayerMaxSpeed = currentPlayerMaxSpeed
            order += acc
            acc = 1
        player.setMaxSpeedOrder(order)


    list.sort(players, key = lambda player: player.getMaxEndurance(), reverse = True)
    order = 0
    acc = 1
    previousPlayerMaxEndurance = 5.0
    for player in players:
        currentPlayerMaxEndurance = player.getMaxEndurance()
        if currentPlayerMaxEndurance == previousPlayerMaxEndurance:
            acc += 1
        else:
            previousPlayerMaxEndurance = currentPlayerMaxEndurance
            order += acc
            acc = 1
        player.setMaxEnduranceOrder(order)

    list.sort(players, key = lambda player: player.getMentality(), reverse = True)
    order = 0
    acc = 1
    previousPlayerMentality = 5.0
    for player in players:
        currentPlayerMentality = player.getMentality()
        if currentPlayerMentality == previousPlayerMentality:
            acc += 1
        else:
            previousPlayerMentality = currentPlayerMentality
            order += acc
            acc = 1
        player.setMentalityOrder(order)

    list.sort(players, key = lambda player: player.getTalent(), reverse = True)
    order = 0
    acc = 1
    previousPlayerTalent = 5.0
    for player in players:
        currentPlayerTalent = player.getTalent()
        if currentPlayerTalent == previousPlayerTalent:
            acc += 1
        else:
            previousPlayerTalent = currentPlayerTalent
            order += acc
            acc = 1
        player.setTalentOrder(order)

    for player in players:
        player.calculateTotal()

    list.sort(players, key=lambda player: player.getTrainer(), reverse=True)
    table = []
    for player in players:
        table.append(player.toList())

    print tabulate(table, headers = headerList())

def clear():
    global playersdict
    playersdict = {}

# -- main --

mainurl = "rockingrackets.com/index.php"

loginformdata = {'username':'usinegEs', 'password':'JrGxd82ej7xazJ', 'login':'Login'}
loginrequest = requests.post("http://" + mainurl, data = loginformdata)

playersdict = {}

subsubpages = {1: "14-", 2: "15_16", 3: "17_18", 4: "19_20", 5: "21_23", 6: "24_26", 7: "27"}

gameworld = "rr" + str(input("Game World: "))

actions = {1: search, 2: show, 3: clear}
while True:
    action = input("Action ([1] Search [2] Show; [3] Clear): ")
    actions[action]()
