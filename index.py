# from lxml import html
# import requests
# page = requests.get('http://www.ideaswatch.com/browse?p=3')
# tree = html.fromstring(page.content)
#
# ideas = tree.xpath('//div[@class="postit_text"]/text()')
# print ('ideas: ', ideas)

import requests
from bs4 import BeautifulSoup

url = 'http://www.ideaswatch.com/startup-ideas/?p='

for page in range(211):

    

    r = requests.get(url + str(page))

    soup = BeautifulSoup(r.content, "html.parser")

    # String substitution for HTML
    for link in soup.find_all("div"):
        general_data = soup.find_all('div', {'class' : 'postit_text'})

    # Fetch and print general data from title class


    for item in general_data:

        print(item.contents[0])
