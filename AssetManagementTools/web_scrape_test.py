from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://survey123.arcgis.com/surveys/3b76b4e81f6a4bb48e5cc981b35a1e35/data")
content = driver.page_source
soup = BeautifulSoup(content)
pd
