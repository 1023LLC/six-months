# Introduction to Selenium

# from selenium import webdriver

# driver = webdriver.Chrome()

# driver.get("https://techwithtim.net")

# print(driver.title)



# Locating Elements From Html

# from selenium import webdriver

# from selenium.webdriver.common.keys import Keys

# import time

# driver = webdriver.Chrome()

# driver.get("https://techwithtim.net")

# print(driver.title)





# search = driver.find_element("s")

# search.send_keys("test")

# search.send_keys(Keys.RETURN)

# time.sleep(5) 


# driver = webdriver.Firefox()

# driver.set_page_load_timeout(10)
# driver.get("https://google.com")
# search = driver.find_element_by_name('q')
# search.send_keys("argentina vnl 2019")
# search.send_keys(Keys.RETURN)



# time.sleep(4)
# driver.quit()

# from selenium.webdriver.support.ui import By

# from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.support.ui import expected_conditions as EC

# from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.maximize_window()

# url = "https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder#maps_places_placeid_finder-typescript"
# driver.get(url)

# keyword = "Dunham Park"
# wait = WebDriverWait(driver, 10)
# wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='geo-devrel-javascript-samples.web.app']")))
# wait.until(EC.visibility_of_element_located((By.ID, "pac-input"))).send_keys(keyword)

# driver.quit()


# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service as ChromeService

# from webdriver_manager.chrome import ChromeDriverManager

# import time

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://google.com")

# time.sleep(7)

# driver.close()
# driver.quit()

# print("Done!")



from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

import time

from selenium.webdriver.common.by import By

from selenium.webdriver import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://google.com")

# googleSearchBox = driver.find_element(By.ID, 'APjFqb')

# googleSearchBox.send_keys("Sam Altman ousted")

# googleSearchBox.send_keys(Keys.RETURN)

# time.sleep(7)


driver.get("https://trytestingthis.netlify.app/index.html")

driver.find_element(By.ID, "fname").send_keys("Mwalimu")

driver.find_element(By.ID, "lname").send_keys("Nyerere")

time.sleep(7)
 
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

time.sleep(7)



