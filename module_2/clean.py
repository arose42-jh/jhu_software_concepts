import json
import re
from bs4 import BeautifulSoup


#Loads the Json File from Scrape.py
def load_data(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
           data = json.load(f)
    return data

#Cleans and builds a new Json of the information within the HTML
def clean_data(soup):
    #regex Patterns for Tags, most of this regex was provided by AI.
    term_re = re.compile(r"(Fall|Spring|Summer|Winter)\s*\d{4}", re.IGNORECASE)
    nat_re = re.compile(r"International|American", re.IGNORECASE)
    gpa_re = re.compile(r"GPA.*", re.IGNORECASE)
    gre_re = re.compile(r"GRE.*", re.IGNORECASE)
    
    data = []

    for entry in soup:

        current_app={}
        main_row = BeautifulSoup(entry["main_row"], "html.parser")

        #nth-of-type(x) was an ai suggestion. Worked better than other things.
        #Sorts the main row html and grabs institution, program, date_added, decision, and the link
        institution = main_row.select_one("td div.tw-font-medium")
        if institution:
            current_app["University"] = institution.text.strip()
        #Program
        program = main_row.select_one("td:nth-of-type(2) div")
        if program:
            current_app["Program"] = re.sub(r"\n+", " | ", program.text.strip())
        #Added on       
        Date_added =  main_row.select_one("td:nth-of-type(3)")
        if Date_added:
            current_app["Date Added"] = Date_added.text.strip()
        #Choices
        Decision =  main_row.select_one("td:nth-of-type(4) div")
        if Decision:
            current_app["Decision"] = Decision.text.strip()

        result_link = main_row.select_one("a[href^='/result/']")
        if result_link and result_link.get("href"):
            current_app["URL"] = f"https://www.thegradcafe.com{result_link['href']}"

        #Goes through Details to grab, GPA, Term, GRE, Nationality
        if entry["details"]:
            deets_row = BeautifulSoup(entry["details"], "html.parser")
            gres = []
            for deet in deets_row.select("div.tw-inline-flex"):
                text = deet.get_text(strip=True)
                if term := term_re.match(text):
                    current_app["Term"] = term.group()

                elif gpa := gpa_re.match(text):
                    current_app["GPA"] = gpa.group()

                elif nat := nat_re.match(text):
                    current_app["Nationality"] = nat.group()
                #GREs needed different stuff because there was anywhere from 0-3 of them per row
                elif gre := gre_re.match(text):
                    gres.append(gre.group())
            
            if gres:
                current_app["GRE"] = ", ".join(gres)

        # Comments (if they exist)
        if entry["comments"]:
            comment_row = BeautifulSoup(entry["comments"], "html.parser")
            comment = comment_row.find("p")
            if comment:
                current_app["Comments"] = re.sub(r"\s+", " ", comment.get_text().strip())
    
        data.append(current_app)
    #Saves all the data into a final Json file.
    with open("applicant_data.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)


