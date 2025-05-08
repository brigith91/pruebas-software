from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# 3pip install selenium
# 1 python -m venv .venv = correr el entorno
# 4 python .\main.py = correr codigo
# 2./.venv/Scripts/activate 


#driver = webdriver.Chrome()
#driver.get("https://www.google.com")
#time.sleep(5)
#search_box = driver.find_element(By.NAME, "q")
#search_box = driver.find_element(By.ID, "input")
#search_box.send_keys("Inter")
#time.sleep(5)
#search_box.submit()
#btn_search = driver.find_element(By.NAME, "btnK")
#btn_search.click()
#time.sleep(10)

#driver.quit()


driver = webdriver.Chrome()
driver.get("https://juans3.github.io")

print(driver.title)
print(driver.current_url)

time.sleep(2)
lnk_about  = driver.find_element(By.LINK_TEXT, "About")
lnk_projects  = driver.find_element(By.LINK_TEXT, "Projects")
lnk_services  = driver.find_element(By.LINK_TEXT, "Services")
lnk_experience  = driver.find_element(By.LINK_TEXT, "Experience")
lnk_education  = driver.find_element(By.LINK_TEXT, "Education")

lnk_about.click()
print(lnk_about.text)
print(lnk_about.get_attribute("href"))
print(driver.current_url)
time.sleep(2)
lnk_projects.click()
time.sleep(2)
lnk_services.click()
time.sleep(2)
lnk_experience.click()
time.sleep(2)
lnk_education.click()
time.sleep(2)


driver.quit()