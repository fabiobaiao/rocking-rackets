#!/usr/bin/python

import sys
import decimal
import requests
from termcolor import cprint
from tabulate import tabulate
from urlparse import parse_qs
from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup

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
    list.append("TE")
    list.append("SS")
    list.append("TESS")
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
    player.setTalent(decimal.Decimal(value(talenthtml)))
    strengthhtml = talenthtml.nextSibling
    player.setStrength(decimal.Decimal(value(strengthhtml)))
    speedhtml = strengthhtml.nextSibling
    player.setSpeed(decimal.Decimal(value(speedhtml)))
    mentalityhtml = speedhtml.nextSibling
    player.setMentality(float(value(mentalityhtml)))
    endurancehtml = mentalityhtml.nextSibling
    player.setEndurance(decimal.Decimal(value(endurancehtml)))
    skillhtml = endurancehtml.nextSibling
    player.setSkill(decimal.Decimal(value(skillhtml)))
    servicehtml = skillhtml.nextSibling
    player.setService(decimal.Decimal(value(servicehtml)))
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

    def getTE(self):
        return self.te[1]

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

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def calculateStats(self):
        self.maxStrength = (
            ((self.strength - decimal.Decimal('0.05')) / self.agePercentage).quantize(decimal.Decimal('1.0')),
            (self.strength / self.agePercentage).quantize(decimal.Decimal('1.0')),
            ((self.strength + decimal.Decimal('0.049')) / self.agePercentage).quantize(decimal.Decimal('1.0'))
            )
        self.maxSpeed = (
            ((self.speed - decimal.Decimal('0.05')) / self.agePercentage).quantize(decimal.Decimal('1.0')),
            (self.speed / self.agePercentage).quantize(decimal.Decimal('1.0')),
            ((self.speed + decimal.Decimal('0.049')) / self.agePercentage).quantize(decimal.Decimal('1.0'))
            )
        self.maxEndurance = (
            ((self.endurance - decimal.Decimal('0.05')) / self.agePercentage / self.agePercentage).quantize(decimal.Decimal('1.0')),
            (self.endurance / self.agePercentage / self.agePercentage).quantize(decimal.Decimal('1.0')),
            ((self.endurance + decimal.Decimal('0.049')) / self.agePercentage / self.agePercentage).quantize(decimal.Decimal('1.0'))
            )
        self.maxSkill = (
            ((self.skill - decimal.Decimal('0.05')) / self.agePercentage).quantize(decimal.Decimal('1.0')),
            (self.skill / self.agePercentage).quantize(decimal.Decimal('1.0')),
            ((self.skill + decimal.Decimal('0.049')) / self.agePercentage).quantize(decimal.Decimal('1.0'))
            )
        self.maxService = (
            ((self.service - decimal.Decimal('0.05')) / self.agePercentage).quantize(decimal.Decimal('1.0')),
            (self.service / self.agePercentage).quantize(decimal.Decimal('1.0')),
            ((self.service + decimal.Decimal('0.049')) / self.agePercentage).quantize(decimal.Decimal('1.0'))
            )
        self.skillPoints = (
            int(self.maxSkill[0] * 20),
            int(self.maxSkill[1] * 20),
            int(self.maxSkill[2] * 20)
            )
        self.servicePoints = (
            int(self.maxService[0] * 20),
            int(self.maxService[1] * 20),
            int(self.maxService[2] * 20)
            )
        self.doublesPoints = int(self.doubles * 20)

    def calculateTotal(self):
        self.te = (self.talent + self.maxEndurance[0], self.talent + self.maxEndurance[1], self.talent + self.maxEndurance[2])
        self.ss = (self.maxStrength[0] + self.maxSpeed[0], self.maxStrength[1] + self.maxSpeed[1], self.maxStrength[2] + self.maxSpeed[2])
        self.total = 100 * self.te[1] + self.ss[1] #(100 * self.te[0] + self.ss[0], 100 * self.te[1] + self.ss[1], 100 * self.te[2] + self.ss[2])
        #self.total = talentweight * self.talent + strengthweight * self.maxStrength + speedweight * self.maxSpeed + mentalityweight * self.mentality + enduranceweight * self.maxEndurance

    def toList(self):
        list = []
        list.append(self.name)
        list.append(self.country)
        list.append("{}".format(self.years))
        #list.append("{} ({}%)".format(self.years, int(self.agePercentage * 100)))
        list.append(self.age)
        list.append("{}".format(self.talent))
        #list.append("{} ({})".format(self.talent, self.talentOrder))
        list.append("[{}, {}]".format(self.maxStrength[0], self.maxStrength[2]))
        #list.append("{} ({} ({}))".format(self.strength, self.maxStrength, self.maxStrengthOrder))
        list.append("[{}, {}]".format(self.maxSpeed[0], self.maxSpeed[2]))
        #list.append("{} ({} ({}))".format(self.speed, self.maxSpeed, self.maxSpeedOrder))
        list.append("{}".format(self.mentality))
        #list.append("{} ({})".format(self.mentality, self.mentalityOrder))
        list.append("[{}, {}]".format(self.maxEndurance[0], self.maxEndurance[2]))
        #list.append("{} ({} ({}))".format(self.endurance, self.maxEndurance, self.maxEnduranceOrder))
        list.append("[{}, {}]".format(self.skillPoints[0], self.skillPoints[2]))
        list.append("[{}, {}]".format(self.servicePoints[0], self.servicePoints[2]))
        list.append("{}".format(self.doublesPoints))
        list.append("{}".format(self.cost))
        #list.append("{} ({})".format(self.maxStrength, self.maxStrengthOrder))
        #list.append("{} ({})".format(self.maxSpeed, self.maxSpeedOrder))
        #list.append("{} ({})".format(self.maxEndurance, self.maxEnduranceOrder))
        #list.append(self.maxSkill)
        #list.append(self.maxService)
        list.append("[{}, {}]".format(self.te[0], self.te[2]))
        list.append("[{}, {}]".format(self.ss[0], self.ss[2]))
        list.append("[{}, {}]".format(self.te[0] + self.ss[0], self.te[2] + self.ss[2]))
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
            player.setAgePercentage(decimal.Decimal(ageInfos[1].replace("(", "").replace(")", "").replace("%", "")) / 100)

def search(subpage, subsubpage, max_cost = ''):
    #category = input("Category ([1] All; [2] Free): ")
    #subpage = subpages[category]

    #subcategory = input("Sub-category ([1] 14-; [2] 15_16; [3] 17_18; [4] 19_20; [5] 21_23; [6] 24_26; [7] 27): ")
    #subsubpage = subsubpages[subcategory]

    start = 1
    end = False
    while not end:
        sortparam = 'talent'
        searchparams = {'max_cost': max_cost, 'player_name': '', 'nation_id': 'all', 'search': 'Search'}
        playersparams = {'page':'players', 'subpage': subpage, 'subsubpage':subsubpage, 'start':start, 'sort':sortparam}
        playersparams.update(searchparams)
        playersrequest = requests.get("http://" + gameworld + "." + mainurl, params = playersparams, cookies = loginrequest.cookies)
        playershtml = BeautifulSoup(playersrequest.text, convertEntities=BeautifulSoup.HTML_ENTITIES, fromEncoding='windows-1252')
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
                    if subpage is 'all':
                        tree = content
                        break
                    else:
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
            if float(player.getTalent()) < 3.0:
                end = True
                break

            if player.getExtra() not in playersdict:
                playersdict[player.getExtra()] = player
                player.setStatus(subpage)
                fetchPlayerInfo(player, loginrequest.cookies)
                player.calculateStats()
                player.calculateTotal()
        start += 1

def simpleShow():
    players = playersdict.values()
    list.sort(players, key = lambda player: player.getTotal())
    printPlayers(players, headers = headerList())

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

    list.sort(players, key = lambda player: player.getTotal())
    #table = []
    #for player in players:
    #    table.append(player.toList())

    printPlayers(players, headers = headerList())

def printPlayers(players, headers = []):
    columnswidth = []
    for j in range(len(headers)):
        columnswidth.append(0)
        columnswidth[j] = max(columnswidth[j], len(str(headers[j])))

    for i in range(len(players)):
        player = players[i]
        playerlist = player.toList()
        for j in range(len(playerlist)):
            if len(columnswidth) < j:
                columnswidth.append(0)
            columnswidth[j] = max(columnswidth[j], len(playerlist[j]))

    te = 0.0
    for i in range(len(players)):
        player = players[i]
        if player.getTE() != te:
            printSeparator(columnswidth)
            te = player.getTE()

        playerList = player.toList()
        if player.getStatus() is 'free':
            if player.getCost() == 0:
                for j in range(len(playerList)):
                    cprint(u"{0:{1}}".format(playerList[j], columnswidth[j]), 'grey', 'on_white', end='')
                    cprint("   ", end='')
            else:
                for j in range(len(playerList)):
                    cprint(u"{0:{1}}".format(playerList[j], columnswidth[j]), attrs = ['reverse'], end='')
                    cprint("   ", end='')
        else:
            for j in range(len(playerList)):
                cprint(u"{0:{1}}".format(playerList[j], columnswidth[j]), end='')
                cprint("   ", end='')
        print ""

    printSeparator(columnswidth)
    printSeparator(columnswidth)

    for j in range(len(headers)):
        cprint("{0:{1}}".format(headers[j], columnswidth[j]), end='')
        cprint("   ", end='')
    print ""

def printSeparator(columnswidth):
    for j in range(len(columnswidth)):
        for k in range(columnswidth[j]):
            cprint("-", end='')
        cprint("   ", end='')
    print ""

def clear():
    global playersdict
    playersdict = {}

# -- main --

mainurl = "rockingrackets.com/index.php"

loginformdata = {'username':'usinegEs', 'password':'JrGxd82ej7xazJ', 'login':'Login'}
loginrequest = requests.post("http://" + mainurl, data = loginformdata)

playersdict = {}

subpages = {1: "all", 2: "free"}
subsubpages = {1: "14-", 2: "15_16", 3: "17_18", 4: "19_20", 5: "21_23", 6: "24_26", 7: "27"}

gameworld = "rr" + str(input("Game World: "))

search('free', '14-')
search('free', '15_16')

search('all', '14-')
search('all', '15_16')

#search('all', '17_18')

simpleShow()

while True:
    raw_input()
    search('free', '14-', max_cost = 0)
    search('free', '15_16', max_cost = 0)

    search('all', '14-', max_cost = 0)
    search('all', '15_16', max_cost = 0)
    simpleShow()
