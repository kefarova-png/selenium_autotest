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


#  Создаём вебдрайвер Chrome, с автоматической проверкой/установкой драйвера и c настройками, которые в options
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
#  Открываем вебдрайвером ссылку
driver.get('https://app.imyx.ru/auth')
#  Устанавливаем размер окна
driver.set_window_size(1920,1080)

#  Находим элемент для логина, используя XPATH, и Вводим в поле логин "not_office@mail.ru"
driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[1]/input").send_keys("not_office@mail.ru")
print('Login input')

#  Находим элемент для пароля, используя XPATH, и Вводим в поле пароль "Shur_1234"
driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[2]/div/input").send_keys("Shur_1234")
print('Password input')

#  Найдём и нажмём кнопку входа
driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/button").click()
print('Login button click')

# Выведем текущий URL и сравним его с ожидаемым
time.sleep(10) #  Пауза для загрузки стриницы после нажатия кнопки входа
get_url = driver.current_url
print(get_url)
expected_url = 'https://app.imyx.ru/'
assert expected_url == get_url, "Фактический URL должен совпадать с ожидаемым."
print("The current URL is correct")

#  Найдём заголовок "Генерация" и сравним его с ожидаемым
get_generation_text = driver.find_element(By.XPATH, '//h1[@class="page-title"]')
get_generation_text_value = get_generation_text.text
print(f'"{get_generation_text_value}" is the found title')
expected_generation_text = "Генерация"
assert expected_generation_text == get_generation_text_value, "Фактический заголовок должен совпадать с ожидаемым."
print("The current page-title is correct")

# Пауза для визуальной проверки
time.sleep(10)
# Закрываем браузер
driver.close()