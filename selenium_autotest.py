#  Импортируем необходимые библиотеки и модули
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#  Chrome. Создаём переменную для опций браузера
options = webdriver.ChromeOptions()
#  Пишем в опции: detach, True -- чтобы Chrome не закрывал окно браузера после завершения работы кода
options.add_experimental_option("detach",True)

#  Включаем Headless-режим -- без открытия браузера
options.add_argument("--headless")

#  Создаём вебдрайвер Chrome, с автоматической проверкой/установкой драйвера и c настройками, которые в options
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
#  Открываем вебдрайвером ссылку
driver.get('https://saucedemo.com/')
# #  Устанавливаем размер окна
# driver.set_window_size(1920,1080)

#  Находим элемент для логина, используя XPATH, и Вводим в поле логин "standard_user"
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("standard_user")
print('Login input')

#  Находим элемент для пароля, используя XPATH, и Вводим в поле пароль "secret_sauce"
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys("secret_sauce")
print('Password input')

#  Найдём и нажмём кнопку входа
driver.find_element(By.ID, "login-button").click()
print('Login button click')

#  Выведем текущий URL и сравним его с ожидаемым
get_url = driver.current_url
print(get_url)
time.sleep(10)
expected_url = 'https://www.saucedemo.com/inventory.html'
assert expected_url == get_url, "Фактический URL должен совпадать с ожидаемым."
print("The current URL is correct")

#  Найдём заголовок "Products" и сравним его с ожидаемым
get_generation_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
get_generation_text_value = get_generation_text.text
print(f'"{get_generation_text_value}" is the found title')
expected_generation_text = "Products"
assert expected_generation_text == get_generation_text_value, "Фактический заголовок должен совпадать с ожидаемым."
print("The current page-title is correct")

# #  Пауза для визуальной проверки
# time.sleep(10)
#  Закрываем браузер
driver.close()