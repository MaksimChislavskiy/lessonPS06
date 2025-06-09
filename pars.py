import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# Инициализация драйвера
driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

# Собираем данные
lighting_items = []

# Находим все элементы с освещением
products = driver.find_elements(By.CSS_SELECTOR, 'div.lsooF')
for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').text
        price = product.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        link = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        # lighting_items.append([name, price, link])
    except:
        print('Произошла ошибка при парсинге')
        continue

    lighting_items.append([name, price, link])

driver.quit()

with open('divan_lighting.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(lighting_items)