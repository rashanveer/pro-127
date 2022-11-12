from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

Start_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(executable_path=r'chromedriver.exe') 
browser.get(Start_URL)
time.sleep(10)

def scrape(): 
    headers = ["Name","Distance","Mass","Radius"] 
    BrightestStar = [] 
    for i in range(0, 10): 
        soup = BeautifulSoup(browser.page_source, "html.parser") 
        for tr_tag in soup.find_all("tr", attrs={"class", "Brighteststar"}): 
            td_tags = tr_tag.find_all("td") 
            tempList = [] 
            for index, td_tag in enumerate(td_tags): 
                if index == 0: 
                    tempList.append(td_tag.find_all("a")[0].contents[0]) 
                else: 
                    try: 
                        tempList.append(td_tag.contents[0]) 
                    except: 
                        tempList.append("") 
            BrightestStar.append(tempList) 
scrape()