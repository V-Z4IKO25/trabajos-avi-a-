from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.mercadolibre.com.mx/ofertas#c_container_id=MLM779363-1&c_id=%2Fsplinter%2Fbutton&c_element_order=1&c_campaign=tracking&c_label=%2Fsplinter%2Fbutton&c_uid=63c6fcc2-1c2c-11f1-9576-6178a5284fba&c_element_id=63c6fcc2-1c2c-11f1-9576-6178a5284fba&c_content_origin=splinter-default&c_content_type=default&c_global_position=8&DEAL_ID=MLM9607&S=landingHubnovedades-de-temporada&V=6&T=Button-normal&L=TRACKING&deal_print_id=638a9000-1c2c-11f1-bedc-3bbd9da68e48&c_tracking_id=638a9000-1c2c-11f1-bedc-3bbd9da68e48")
    time.sleep(5)

    productos = driver.find_elements(By.CSS_SELECTOR, ".andes-card.poly-card.poly-card--grid-card")
    product_data = []
    for producto in productos:
        try:
            nombredelproducto = producto.find_element(By.CLASS_NAME, "poly-component__title-wrapper").text
            preciodelproducto = producto.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
            product_data.append([nombredelproducto, preciodelproducto])
        except Exception:
            continue


#crear dataframe
    import pandas as pd
    from rich.console import Console
    from rich.table import Table

    df = pd.DataFrame(product_data, columns=["Nombre", "Precio"])

    console = Console()

    table = Table(title="Lista de Productos", show_lines=True)

    table.add_column("Nombre", justify="center")
    table.add_column("Precio", justify="center")

    for i, row in df.iterrows():
        table.add_row(str(row["Nombre"]), str(row["Precio"]))

    console.print(table)

    #guardar dataframe en excel
    df.to_excel("productos.xlsx", index=False)

if __name__ == "__main__":
    main()