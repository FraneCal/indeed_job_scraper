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

job_posting = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]')))
job_posting.click()

time.sleep(3)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, "html.parser")

# Basic information about the job posting (title, company name, location, salary)
box = soup.find('div', class_='jobsearch-HeaderContainer')
title = box.find('span').getText().split(' - ')[0]
company_name = box.find('span', class_='css-1saizt3').getText()
location = box.find('div', class_='css-waniwe').find('div').getText()
salary = box.find('span', class_='css-19j1a75').getText()

# Link to the job posting
links = soup.find('table', class_='big6_visualChanges').find('a', class_='jcs-JobTitle').get('href')
if "/rc/clk" in links:
    job_id_start = links.find("?jk=")
    job_id_end = links.find("&", job_id_start)
    job_id = links[job_id_start + 4:job_id_end]
    link = f"https://www.indeed.com/viewjob?jk={job_id}"
else:
    link = "Link not found or formatted differently"

print(title)
print(company_name)
print(location)
print(salary)
print(link)



# FINISH SALARY
