import requests
import json
from bs4 import BeautifulSoup

topic = "catrt5"
to_send = "https://en.wikipedia.org/w/api.php?titles={}&action=query&prop=extracts&redirects=1&format=json&exintro=".format(topic)
r = requests.get(to_send)
data = r.json()
print(data)
entry = data['query']['pages']
the_key = list(entry.keys())[0]
pretext = entry[the_key]['extract']
print(pretext)
soup = BeautifulSoup(pretext)
text = soup.get_text()
print(text)



import requests
import json
from bs4 import BeautifulSoup
import espeak
