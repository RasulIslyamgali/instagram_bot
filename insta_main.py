import keys
from pages import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем драйвер Firefox
browser = webdriver.Firefox()
'''
Неявные ожидания - Implicit Waits - конфигурируют экземпляр WebDriver делать
многократные попытки найти элемент (элементы) на странице в
течении заданного периода времени, если элемент не найден сразу.
Tолько по истечении этого времени WebDriver бросит ElementNotFoundException.

Неявные ожидания обычно настраиваются сразу после создания экземпляра WebDriver и действуют
в течении всей жизни этого экземпляра, хотя переопределить их можно в любой момент.
'''
browser.implicitly_wait(5)
# обращаемся к классу HomePage
home_page = HomePage(browser)
# Обращаемся к функции класса HomePage go_to_login_page()
login_page = home_page.go_to_login_page()
'''функция go_to_login_page возвращает класс LoginPage, и мы поэтому обращаемся
к функции класса LoginPage login и передаем в качестве аргументов наш пароль и имя пользователя импортированные из keys
'''
login_page.login(keys.my_login, keys.my_pass)



# browser.implicitly_wait(5)
# browser.get("https://www.instagram.com/")
#username_input = browser.find_element_by_css_selector("input[name='username']")
#password_input = browser.find_element_by_css_selector(("input[name='password']"))
#username_input.send_keys(keys.my_login)
#sleep(4)
#password_input.send_keys(keys.my_pass)
#sleep(6)
#login_button = browser.find_element_by_css_selector("button[type='submit']")
#login_button.click()

sleep(15)
#browser.close()