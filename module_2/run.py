from clean import clean_data, load_data
from scrape import scrape_data, save_data
import time
#Runs the program, 500 selected as at least 20 applications per page
#time.sleep was a recomendation to not overload the server.
#program takes 4+ minutes to run.
scraped = []
for j in range(500):
    pages = scrape_data(j)
    scraped.extend(pages)
    time.sleep(0.5)

save_data(scraped)

soup = load_data("scraped_data.json")
clean_data(soup)