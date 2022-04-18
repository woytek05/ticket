from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time


from_city = "Kraków"
to_city = "Połaniec"
day_number = 22
month_number = 4
departure_time = "15:45"

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
url = "https://transhans.pl/"
driver.get(url)
time.sleep(2)

starting_point = driver.find_element(By.CSS_SELECTOR, "form > fieldset > div > div.fromToHolder > label.lblFrom > span > input")
destination = driver.find_element(By.CSS_SELECTOR, "form > fieldset > div > div.fromToHolder > label.lblTo > span > input")
date = driver.find_element(By.CSS_SELECTOR, "form > fieldset > div > div.departureDateTime > div.dateSelect > label.lblDate")
submit = driver.find_element(By.CSS_SELECTOR, 'form > fieldset > div > div.buttonHolder > button[type="submit"]')

starting_point.send_keys(from_city)
time.sleep(1)
destination.click()

destination.send_keys(to_city)
time.sleep(1)

date.click()
time.sleep(1)
calendar = driver.find_elements(By.CSS_SELECTOR, "table.jCalendar > tbody > tr > td")
for day in calendar:
    if day.text == str(day_number):
        day.click()
        break

submit.click()

hours = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.searching-result > div.brief-info > div.edges-info > div.departure-time > span.time"))
)

for hour in hours:
    if hour.text == departure_time:
        hour.click()
        break
