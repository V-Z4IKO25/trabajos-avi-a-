from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
User = "standard_user"
Password = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")
    user_input = driver.find_element(By.ID, "user-name")
    user_input.send_keys(User)
    pass_input = driver.find_element(By.ID, "password")
    pass_input.send_keys(Password)
    button = driver.find_element(By.ID, "login-button")
    button.click()
    nombres = [el.text for el in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    precios = [el.text for el in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    
    for n, p in zip(nombres, precios):
        print(f"Nombre: {n}, Precio: {p}")

    import pandas as pd
    from tabulate import tabulate
    diccionario_datos = {"Nombre": nombres, "Precio": precios}
    df = pd.DataFrame(diccionario_datos)
    
    # Imprimir la tabla con contorno (grid) y sin los números de la izquierda (index)
    print("\nTABLA DE PRODUCTOS:")
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
if __name__ == '__main__':
    main()