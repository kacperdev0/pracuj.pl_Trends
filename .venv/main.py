import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = 'https://www.pracuj.pl/'

def getOfferLinksForKeyword(keyword):
    searchUrl = url + "praca/" + keyword
    driver.get(searchUrl)

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "listing_ohw4t83"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    linkComponents = soup.find_all(attrs={"data-test":"link-offer"})
    links = [component.get("href") for component in linkComponents]
    return links

def getOfferRequirements(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    print(soup)
    soup.find_all(attrs={"data-test":"section-responsibilities"})
    print(soup)
print(getOfferRequirements("https://www.pracuj.pl/praca/senior-ot-soc-analyst-wroclaw,oferta,1003584871?s=ff047766&searchId=MTcyODMxODE5NDI2NS43NDcz&ref=top_booster_1_1_1"))
