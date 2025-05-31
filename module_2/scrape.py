from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

#Download the pages (I tried doing them from the URL one at a time and it took forever)
#20 per page
#scrape > Save > Load > Clean

#Parses through X pages and grabs the HTML
def scrape_data(index):
    base = "https://www.thegradcafe.com/survey/?sort=newest"
    url = f"{base}&page={index}"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    
    #Takes the HTML and sorts it into the "main","details", and "Comments" rows
    pagedata = []
    body = soup.select_one("tbody")
    rows = body.find_all("tr")

    i = 0
    while i < len(rows):
        info = {
            "index" : index,
            "main_row" : str(rows[i]),
            "details" : None,
            "comments" : None
        }

        i += 1
        #Theres always a details row so grabs that after main.
        if i < len(rows):
            info["details"] = str(rows[i])
            i +=1
        
        #Checks for Comments row
        if i < len(rows) and rows[i].find("td", colspan = "100%"):
            info["comments"] = str(rows[i])
            i +=1
        
        pagedata.append(info)
    return pagedata

#Saves the output of Scrape_data and saves it as a Json file.
def save_data(alldata):
    filename = f"scraped_data.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(alldata, f, indent = 4)
