#!/usr/bin/python

import requests
from BeautifulSoup import BeautifulSoup

gameworld = "rr" + str(input("Game World: "))

newplayer = input("New Player: ")
myplayer = input("My Player: ")

mainurl = "rockingrackets.com/index.php"

loginformdata = {'username':'usinegEs', 'password':'JrGxd82ej7xazJ', 'login':'Login'}
loginrequest = requests.post("http://" + mainurl, data = loginformdata)

loop = True
while loop:

    #playerparams = {'page': 'player', 'extra': newplayer}
    hireformdata = {'player_id': newplayer, 'hire': ' '}
    #hire = requests.post("http://" + gameworld + '.' + mainurl, params = playerparams, data = hireformdata, cookies = loginrequest.cookies)
    tryrequest = True
    while tryrequest:
        try:
            hirerequest = requests.post("http://" + gameworld + '.' + mainurl, data = hireformdata, cookies = loginrequest.cookies)
            tryrequest = False
        except ConnectionError:
            pass


    hirehtml = BeautifulSoup(hirerequest.text)
    tree = hirehtml.body

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
            if content.name == 'div' and content['class'] == 'error':
                tree = content
                break

    error = tree

    if "This player can't be hired yet. After a player is fired he cannot be rehired by someone else for 12 to 36 hours." not in str(error):
        loop = False


if "You can only have 2 players. (You have 2)" in str(error):

    # fire myplayer
    fireformdata = {'player_id': myplayer, 'fire': 'Fire'}
    firerequest = requests.post("http://" + gameworld + '.' + mainurl, data = hireformdata, cookies = loginrequest.cookies)

    hireformdata = {'player_id': newplayer, 'hire': ' '}
    hirerequest = requests.post("http://" + gameworld + '.' + mainurl, data = hireformdata, cookies = loginrequest.cookies)
