from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "https://www.indeed.com/"

driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

# Enter the job title
job_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text-input-what"]')))
job_title.send_keys("Mechanical Engineer")

# Enter the location
location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text-input-where"]')))
location.send_keys("Colorado")
location.send_keys(Keys.ENTER)

time.sleep(5)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, "html.parser")
