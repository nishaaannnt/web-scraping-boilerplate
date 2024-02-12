# Libraries used -
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import pandas as pd


# change the URL to the website page you wanna scrap
url="https://yourURL.com"


# 1st Function to get and save your fetched HTML
def fetchAndSave(url,path):
    payload ={'api_key':'YOUR_API_KEY',"url":url, 'render': 'true'}
    r=requests.get('http://api.scraperapi.com/', params=urlencode(payload))
    print(r.text)
    with open(path, "w", encoding="utf-8") as f:
         f.write(r.text);


# Remove any Unicode if present in text
def remove_unicode(text):
    return text.encode('ascii', 'ignore').decode("utf-8")

# Scrape the HTML and Store it in JSON
def scrapeAndStore(path,jsonPath):
    with open(path,"r", encoding="utf-8") as f:
        html_doc=f.read()
    soup=BeautifulSoup(html_doc,"html.parser");
    soup.prettify();
    products_div=soup.find_all("div",class_="");
    data=[];

    # Adjest the className and fields
    for products in products_div:

        # title
        title=products.find("h2",class_="")
        title_elem = title.text.strip() if title else None
        title_elem=remove_unicode(title_elem)

        # price
        price=products.find("div",class_="mpof_92 myre_zn")
        price_elem = price.text.strip() if price else None
        price_elem=remove_unicode(price_elem)

        # image
        img=products.find("a",class_="").find("img");
        if(img):
            img=img["src"]

        # state
        state_dt = products.find("dt", string="State")
        state_dd = state_dt.find_next_sibling("dd")
        state = state_dd.text.strip() if state_dd else None
        state=remove_unicode(state)

        # manufacturer
        manufacturer_dt = products.find("dt", string="Parts Manufacturer")
        if manufacturer_dt:
            manufacturer_dd = manufacturer_dt.find_next_sibling("dd")
        if manufacturer_dd:
            manufacturer = manufacturer_dd.text.strip()
            manufacturer = remove_unicode(manufacturer)

        # catalog number
        parts_catalog_number_dt = products.find("dt", string="Parts catalog number")
        parts_catalog_number_dd = parts_catalog_number_dt.find_next_sibling("dd")
        parts_catalog_number = parts_catalog_number_dd.text.strip() if parts_catalog_number_dd else None
        parts_catalog_number = remove_unicode(parts_catalog_number)

        data.append({
            "Title":title_elem,
            "Price":price_elem,
            "State":state,
            "Parts manufacturer":manufacturer,
            "Parts catalog number":parts_catalog_number,
            "Img URl":img
        })
    with open(jsonPath, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    saveInExcel("data/products.json", "data/products.xlsx")
    

# Function to save the saved data in Excel
def saveInExcel(jsonPath,excelPath):
    with open(jsonPath, "r") as json_file:
        data = json.load(json_file)

    df = pd.DataFrame(data)
    
    with pd.ExcelWriter(excelPath, engine="openpyxl",mode='a', if_sheet_exists='overlay' ) as writer:
        df.to_excel(writer,header=False,startrow=281)

# Change name or location as per your convenience

fetchAndSave(url,"data/scrap.html");
scrapeAndStore("data/scrap.html","data/products.json");
        
    
