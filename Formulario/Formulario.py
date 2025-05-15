from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
import time

#driver = webdriver.Chrome()
#driver.get("https://demoqa.com/automation-practice-form")
#time.sleep(2)

#nombre_box = driver.find_element(By.ID, "firstName")
#nombre_box.send_keys("Lina")
#time.sleep(2)

#apellido_box = driver.find_element(By.ID, "lastName")
#apellido_box.send_keys("Roncancio")
#time.sleep(2)

#Email_box = driver.find_element(By.ID, "userEmail")
#Email_box.send_keys("bridgeth1991@gmail.com")
#time.sleep(2)

#celular_box = driver.find_element(By.ID, "userNumber")
#elular_box.send_keys("3207682020")
#time.sleep(2)

#tema_box = driver.find_element(By.ID, "subjectsInput")
#tema_box.send_keys("Maths")
#time.sleep(2)

#search_box = driver.find_element(By.ID, "subjectsInput")
#search_box.send_keys("Physics")
#time.sleep(2)
#direccion_box = driver.find_element(By.ID, "currentAddress")
#direccion_box.send_keys("Av. Caracas #35 – 38, Bogotá")
#time.sleep(2)

#lnk_submit  = driver.find_element(By.ID, "submit")
#lnk_submit.submit()
#time.sleep(2)


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--incognito")
    #options.add_argument("--window-size=1700,900")
    driver = webdriver.Chrome(options)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver
    
    
    
    
def datos_texto_plano(driver: WebDriver):
    datos: dict[str , str] = {
        "firstName" : "Lina",
        "lastName" : "Roncancio",
        "userEmail" : "bridgeth1991@gmail.com",
        "userNumber" : "3207682020",
        "subjectsInput" : "Maths",
        "currentAddress" : "Av. Caracas #35 – 38, Bogotá",
        #"submit" : " ***",
        
    }
    
    for id_pag in datos:
        texto = datos[id_pag]
        driver.find_element(By.ID, id_pag).send_keys(texto)
        time.sleep(3)
        
        
def main():
    driver: WebDriver = get_driver()
    datos_texto_plano(driver)
    driver.save_screenshot("antes_de_enviar.png")
    driver.find_element(By.ID, "submit").submit()
    driver.save_screenshot("despues_de_enviar.png")
    time.sleep(4)
    

    driver.quit()
    
if __name__== "__main__":
    main()