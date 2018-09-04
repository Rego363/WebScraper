import urllib
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import re

"""
theurl = "https://twitter.com/realDonaldTrump"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")
"""
## Tutorial 1
"""
print(soup.title.text)
for link in soup.findAll('a'):
    print(link.get('href'))
    print(link.text)

print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)

i = 1

for tweets in soup.findAll('div', {"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i = i + 1
"""

def make_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    thepage = urlopen(req).read()
    #thepage = urllib.request.urlopen(url)

    #webpage = thepage.decode('utf-8')
    soupdata = BeautifulSoup(thepage, "html.parser")


    return soupdata

### Tutorial 2
"""
playerdata = ""
playerdatasaved = ""
soup = make_soup("http://www.basketball-reference.com/players/a/")
for record in soup.findAll('tr'):
    playerdata = ""
    for data in record.findAll("th"):
        playerdata = playerdata + "," + data.text

    for data in record.findAll("td"):
            playerdata = playerdata + "," + data.text

    if len(playerdata) != 0:
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "Player, From, To, Pos, Ht, Wt, Birth Date, Birth Year, College" + "\n"
file = open(os.path.expanduser("Basketball.csv"), "wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii", errors='ignore'))
print(playerdatasaved)
"""

### Tutorial 3
link1 = "https://www.hse.ie/eng/services/list/1/lho/carlowkilkenny/health-centres/#Co%20Kilkenny%20Health%20Centres"
soup = make_soup(link1)
#link = soup.find(attrs={"class":"dbg0pd"})


i = 1

phone = "Tel:"
centreData = ""
centreDataSaved = ""
found = False

for centres in soup.findAll('div', {"class":"content"}):

    for data in centres.findAll("p"):
        if data.text[0:9] == "Ballyhale":
            found = True
            print("Found")
            numberStart = data.text.find(phone)  # Pos of where the phone number starts

        numberStart = data.text.find(phone)  # Pos of where the phone nuber starts
        if found == True:
            if data.text[0:7] != 'Opening' and data.text[0:7] != 'back to':

                print(i)
                centreData = str(i)
                i = i + 1
                address = data.text[0:numberStart]
                nameEnd = data.text.find(',')
                print(address[0:nameEnd])
                centreData = centreData + "," + address[0:nameEnd]
                print(address)

            for info in data.findAll("a"):
                if data.text[0:7] != 'back to':
                    print(info.text)
                    centreData = centreData + "," + info.text
                    centreDataSaved = centreDataSaved + "\n" + centreData


    #print([int(s) for s in centres.text.split() if s.isdigit()])
    #for data in centres.findAll("/br"):
"""
    text = centres.text
    text = text.replace(" ", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("\n", "")
    name = ""
    number = ""
    while len(text) > 0:

        centreData = "" #Clear temp data
        centreData = str(i) # Add index
        #print(i)

        numberStart = text.find(phone)  # Pos of where the phone number starts
        name = text[0:numberStart] #Get Name of centre
        #print(name + "lol")
        centreData = centreData + "." + name
        #address = data.text[0:pos]
        #name = address[0:text.find(",")]
        numEnd = 0
        pn = ""
        #print(text)
        #print(text[numEnd].isalpha())
        while len(text) > numEnd and text[numEnd].isalpha() == False:
            if i == 1:
                print("1 " + str(text[numEnd].isalpha()))
            pn = pn + text[numEnd]
            numEnd = numEnd + 1

        number = pn
        centreData = centreData + "." + number
        #centreData = centreData + "." + address
        #print(number)
        lengthOfData = len(name) + len(number)
        #print(number + "Lawls")
        #print(lengthOfData)
        text = text[lengthOfData:]

        centreDataSaved = centreDataSaved + "\n" + centreData
        i = i + 1

"""


header = "Index,Name,Phone " + "\n"
file = open(os.path.expanduser("KK.csv"), "wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(centreDataSaved, encoding="ascii", errors='ignore'))
print(centreDataSaved)

"""

text_file = open("Output.html", "w")
text_file.write(soup.prettify())
text_file.close()

"""
