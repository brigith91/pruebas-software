from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


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

#def get_driver():
    #options = webdriver.ChromeOptions()
    #options.add_argument("start-maximized")
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")
    #options.add_argument("--incognito")
    #options.add_argument("--window-size=1700,900")
    #driver = webdriver.Chrome(options)
    #driver.get("https://demoqa.com/automation-practice-form")
    #return driver
    
    
    
    
#def datos_texto_plano(driver: WebDriver):
    #datos: dict[str , str] = {
    #    "firstName" : "Lina",
    #    "lastName" : "Roncancio",
    #    "userEmail" : "bridgeth1991@gmail.com",
    #    "userNumber" : "3207682020",
    #    "subjectsInput" : "Maths",
    #    "currentAddress" : "Av. Caracas #35 – 38, Bogotá",
    #    "submit" : " ***",
        
    #}
    
    #for id_pag in datos:
    #    texto = datos[id_pag]
    #    driver.find_element(By.ID, id_pag).send_keys(texto)
    #    time.sleep(3)
        
        
#def main():
    #driver: WebDriver = get_driver()
    #datos_texto_plano(driver)
    #driver.save_screenshot("antes_de_enviar.png")
    #driver.find_element(By.ID, "submit").submit()
    #driver.save_screenshot("despues_de_enviar.png")
    #time.sleep(4)
    

    #driver.quit()
    
#if __name__== "__main__":
#    main()


OPTIONS:list[str] =[
    "--disable-extensions",
    #"--disable-gpu",
    "start-maximized",
]

def get_driver(options:list[str] = [])-> WebDriver:
    
    opt = webdriver.ChromeOptions = webdriver.ChromeOptions()
    for option in options:
        opt.add_argument(option)

    driver = webdriver.Chrome(options=opt)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver

def scroll_to_element(driver: WebDriver, element:WebElement)-> None:
    driver.execute_script("arguments[0].scrollIntoView(true);",element)
    sleep(1)
 
def llenar_texto_by_id(driver: WebDriver, id_element: str, texto: str)->  WebElement:
    element: WebElement = driver.find_element(By.ID, id_element)
    element.send_keys(texto)
    scroll_to_element(driver=driver, element=element)
    return element

def texto_autocompletado(driver: WebDriver, id_element: str, texto: str)-> None:
    llenar_texto_by_id(driver=driver, id_element=id_element, texto=texto)
    element_autocomplete = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            ( 
                By.XPATH,
                f"//div[contains(@class, 'subjects-autocomplete__option') and text()='{texto}']"
            )
        )
    )
    element_autocomplete.click()

def seleccionar_fecha(driver: WebDriver)-> None:
    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID,"dateOfBirthInput"))
    ).click()

    year_select: WebElement = driver.find_element(
        By.CLASS_NAME, "react-datepicker__year-select"
    )
    sleep(1)
    Select(year_select).select_by_value("1991")

    month_select: WebElement = driver.find_element(
        By.CLASS_NAME, "react-datepicker__month-select"
    )
    sleep(1)
    Select(month_select).select_by_value("September")

    day_select: WebElement = driver.find_element(
        By.CLASS_NAME, "react-datepicker__day--05"
    )
    sleep(1)
    day_select.click()
    sleep(1)
    

def llenar_formulario(driver: WebDriver)-> None:
    campos_texto: dict[str,str]={
        "firstName":"Lina",
        "lastName":"Roncancio",
        "userEmail":"bridgeth1991@gmail.com",
        "userNumber":"3207682020",
        "currentAddress":"Av. Caracas #35  38, Bogotá",
        "uploadPicture":"C:/Users/User/OneDrive/Imágenes/python.jpg"

    }
    for key ,value in campos_texto.items():
        llenar_texto_by_id(driver=driver, id_element=key, texto=value)
        sleep(1)

def llenar_radio_check(driver:WebDriver, element_value:str)-> None:
    radio_button: WebElement = driver.find_element(
        By.XPATH, f"//label[contains(text(),'{element_value}')]"
    )
    scroll_to_element(driver=driver, element=radio_button)
    radio_button.click()
    sleep(1)


def llenar_cuidad(driver:WebDriver, state: str, city: str)-> None:
    estado: WebElement =driver.find_element(By.ID, "state")
    scroll_to_element(driver=driver, element=estado)
    estado.click()

    estado: WebElement =driver.find_element(
         By.XPATH,
         f"//div[contains(@id,'react-select-3-option-')and contains(text(), '{state}')]",
    )
    estado.click()

    estado: WebElement =driver.find_element(By.ID ,"city")
    scroll_to_element(driver=driver, element=estado)
    estado.click()
    ciudad: WebElement =driver.find_element(
         By.XPATH,
         f"//div[contains(@id,'react-select-4-option-')and contains(text(), '{city}')]",
    )
    ciudad.click()

def enviar_formulario(driver:WebDriver)-> None:
    submit:WebElement = driver.find_element(By.ID, "submit")
    scroll_to_element(driver=driver, element=submit)
    submit.click()

def main()-> None:
    driver: WebDriver = get_driver(options=OPTIONS)
    llenar_formulario(driver=driver)
    sleep(3)
    for subject in ["Maths", "Physics", "Chemistry"]:
        texto_autocompletado(
            driver=driver,
            id_element="subjectsInput",
            texto=subject,
        )
    seleccionar_fecha(driver=driver)
    llenar_radio_check(driver=driver, element_value="Female")
    llenar_radio_check(driver=driver, element_value="Sports")
    llenar_radio_check(driver=driver, element_value="Music")
    llenar_radio_check(driver=driver, element_value="Reading")
    llenar_cuidad(driver=driver, state="NCR", city="Delhi")
    sleep(3)
    enviar_formulario(driver=driver)
    driver.save_screenshot("screenshot.png")
    driver.quit()



if __name__== "__main__":
    main()



    
    
    
    
    
