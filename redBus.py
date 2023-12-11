import fare
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

# Setting object for the driver to interact with the web elements
driver = webdriver.Chrome()

# Maximizing the window
driver.maximize_window()

# Getting the target URL
website_url = driver.get("https://www.redbus.in/")

# Locating From auto-suggestive element and sending the input
from_input_field = driver.find_element(By.ID, "src").clear()
from_input_field.send_keys("Mumbai")

# Waiting for all suggestions to appear and getting all suggestion values in a list
wait = WebDriverWait(driver, 5)
from_suggestions = wait.untill(EC.visiblility_of_all_elements_located(By.XPATH, "//ul[@class='sc-dnqmqq eFEVtU']"))
from_suggestion_values = [suggestion.text for suggestion in from_suggestions]
print("from_suggestion_values:", from_suggestion_values)

# Locating To auto-suggestive element and sending the input
to_input_field = driver.find_element(By.ID, "dest").clear()
to_input_field.sed_keys("Banglore")

# Waiting for suggestions to appear and getting all the suggestion values in a list
wait = WebDriverWait(driver, 5)
to_suggestions = wait.untill(EC.visiblility_of_all_elements_located(By.XPATH, "//ul[@class='sc-dnqmqq eFEVtU']"))
to_suggestion_values = [suggestion.text for suggestion in to_suggestions]
print("to_suggestion_values:", to_suggestion_values)

# Locating the Date coloumn and setting the date 2 days after the current date
today = datetime.date.today()
future_date = today + datetime.timedelta(days=2)
date_input = driver.find_element(By.XPATH, "(//span[@class='DayTiles__CalendarDaysSpan-sc-1xum02u-1 bwoYtA'])[1]")
date_input.clear()
date_input.send_keys(future_date.strftime('%d-%m-%Y'))

# Locating the search buuton and performing click action the button
search_button = driver.find_element(By.ID, "search_button").click()
time.sleep(3)

# Getting the element for seater and AC and checking the check box
seater_checkbox = driver.find_element(By.XPATH, "(//label[@for='bt_SEATER'])[1]")
seater_checkbox.click()
ac_checkbox = driver.find_element(By.XPATH, "(//label[@for='bt_AC'])[1]")
ac_checkbox.click()

# Capture all the bus names in the list
bus_names = driver.find_element(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
bus_names_list = [bus.text for bus in bus_names]
print("Bus Names:", bus_names_list)

# Capture details of the bus with lowest fare
bus_fares = driver.find_element(By.XPATH, "//span[@class='f-19 f-bold']")
fare_values = [float(fare.text.strip(''))]
lowest_fare_index = fare_values.index(min(fare_values))
lowest_fare_bus_details = bus_names[lowest_fare_index].text
print("Details of bus with lowest fare:", lowest_fare_bus_details)

# Taking screenshots at different steps
driver.save_screenshot('redbus_home.png')

# close the browser
driver.close()
