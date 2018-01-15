import requests
from bs4 import BeautifulSoup
#get ideas website
url = 'http://www.ideaswatch.com/startup-ideas/?p='
#loop through number of pages
for page in range(211):

    

    r = requests.get(url + str(page))
    #get all the content from the pages
    soup = BeautifulSoup(r.content, "html.parser")

    # select all divs
    for link in soup.find_all("div"):
        #select the divs with the class postit_text
        general_data = soup.find_all('div', {'class' : 'postit_text'})

    #loop trough all the classes
    for item in general_data:
        #print the ideas
        print(item.contents[0])
