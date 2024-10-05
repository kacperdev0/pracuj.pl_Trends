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


print(getOfferLinksForKeyword("cybersecurity"))