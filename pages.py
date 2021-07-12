from time import sleep
import keyboard
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, browser):
        self.browser = browser
    def login(self, username, password):
        # Находим поля для ввода имени пользователя и пароля, используя CSS селектор
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector(("input[name='password']"))

        # используя функцию send_keys вводим наш пароль и имя пользователя в найденные поля
        username_input.send_keys(username)
        # sleep, для имитации поведения человека, дальше везде sleep
        # для имитации поведения человека, для избегания блокировки инстаграммом
        sleep(5)
        password_input.send_keys(password)
        sleep(7)

        # после ввода данных, используя css селектор, находим кнопку для входа 'войти'
        login_button = self.browser.find_element_by_css_selector("button[type='submit']")
        # кликаем по этой кнопке
        login_button.click()
        sleep(9)

        # всплывает окошка с предложением сохранить пароль и данные для входа
        # находим кнопку 'не сейчас' с помощью CLASS_NAME
        not_now_to_save_button = self.browser.find_element(By.CLASS_NAME, "_8-yf5 ")
        # кликаем по этой кнопке
        not_now_to_save_button.click()
        sleep(5)

        # Всплывает предложение 'включить уведомления', находим кнопку 'не сейчас'
        not_now_to_notice = self.browser.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
        # кликаем по этой кнопке
        not_now_to_notice.click()
        sleep(5)

        # теги, для поиска постов
        text_tag = ['#python', '#программирование', '#питон', 'пайтон']
        # а это счетчик, для перебора тегов в списке text_tag
        count_for_tags = 0

        def foo_find_with_tag(tag_text, n):
            # Нахожу поле для поиска с помощью css селектора
            find_with_tag = self.browser.find_element(By.CSS_SELECTOR, '.XTCLo')
            # передаем текст запроса
            find_with_tag.send_keys(tag_text)
            sleep(4)
            # нажимаем клавишу enter 2 раза с небольшой паузой, т.к. инстаграм на одно нажатие не реагирует
            keyboard.send('enter')
            sleep(1)
            keyboard.send('enter')
            sleep(10)

            # находим третий пост, среди найденных постов по заданному хэштегу
            # пока что ПЫТАЕМСЯ НАЙТИ , Думаю основная трудность будет в том, чтобы
            # он находил третий пост всегда, даже когда поисковые запросы поменятся
            # пока что мы находим лишь первый пост по результатам запроса
            find_third_post = self.browser.find_element(By.CSS_SELECTOR,
                '''html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T 
                main.SCxLW.o64aR article.KC1QD div.EZdmt div div div.Nnq7C.weEfm div.v1Nh3.kIKUG._bz0w''')
            # кликаем на этот пост
            find_third_post.click()
            sleep(5)
            # ЗДЕСЬ ТОЖЕ ЕСТЬ НЮАНСЫ, ЕСЛИ ЭТОТ ПОСТ ВИДЕО, ТО ТАМ НЕТУ КНОПКИ НРАВИТСЯ, ТАМ УЖЕ ПРОСМОТРЫ, ПОЭТОМУ ТУТ ТОЖЕ НАДО try except
            # находим кнопку нравится
            list_people_who_liked = self.browser.find_element(By.CSS_SELECTOR, '.zV_Nj')
            # кликаем по нему
            list_people_who_liked.click()
            sleep(5)

            # перед тем, как нажимать кнопку вниз, надо сделать так, чтобы бот начал взаимодействовать с открывшемся окном
            # списка лайкавших. для этого надо кликнуть по нему
            empty_place_in_liked_list = self.browser.find_element(By.CSS_SELECTOR, 'div.rBNOH:nth-child(2)')
            # и собственно кликаем по нему
            empty_place_in_liked_list.click()
            sleep(2)

            # ЗДЕСЬ НАДО ОСУЩЕСТВИТЬ НАЖАТИЕ КЛАВИШИ ВНИЗ. ЧТОБЫ ПРИ КАЖДОЙ СЛЕДУЮЩЕЙ ИТЕРАЦИИ БОТ ОПУСКАЛСЯ ВНИЗ ПО СПИСКУ ЛЮДЕЙ
            # с помощью цикла при повторных обращениях бот будет опускаться вниз по списку, чтобы не выбирать одного юзера дважды
            for i in range(5):
                keyboard.send('down')
                sleep(1)
            # НЕТ ИМИТАЦИЯ НАЖАТИЯ ВНИЗ ВООБЩЕ НЕ ПОМОГАЕТ ПРОДВИГАТЬСЯ ВНИЗ ПО СПИСКУ ЮЗЕРОВ
            # ЩЯ КОНЕЧНО поищу норм варианты, но чтобы не забыть: можно к примеру взять код этой открывшеся страницы, там же есть ссылки на всех этих чуваков
            # вот его импортировать, прочесть и уже те данные вводить в поисковик гугл один за другим и подписываться и отправлять сообщ

            # enter не нажимается, т.е. конкретный человек из за нажатия кнопки вниз не будет выбираться
            # находим последнего залайкавшего
            man_who_liked = self.browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/span/a')
            # кликаем по нему
            man_who_liked.click()
            sleep(5)
            # зашли на страницу последнего лайкавшего, вот здесь эта функция пока заканчивается
            try_to_follow(text_tag, count_for_tags, n)
            # увеличиваем n для следующей итерации
            n += 1
        def try_to_follow(x, y, z):
            # ПРИДУМАЛ, МОЖНО СДЕЛАТЬ ТАК: ЕСЛИ ЮЗЕР ЗАКРЫТЫЙ, ТО ОПЯТЬ ИЩЕМ ЭТОТ ХЕШТЕГ И УЖЕ ПРИ ОТКРЫВАНИИ
            # ВКЛАДКИ НРАВЯТСЯ, НАДО ИМИТИРОВАТЬ НАЖАТИЕ КЛАВИШИ ВНИЗ, И КАЖДЫЙ РАЗ НА ОДНОГО БОЛЬШЕ БУДЕМ НАЖИМАТЬ
            # цикл while, чтобы бот продолжал поиск, пока не найдет юзера с открытым акк
            flag = True
            while flag:
                try:
                    button_for_follow = self.browser.find_element(By.CSS_SELECTOR, '._6VtSN')
                    # кликаем по этой кнопке
                    button_for_follow.click()
                    sleep(4)
                    flag = False
                except:
                    flag = True
                    # если акк оказался закрытым, то счетчик увеличивается
                    # и вызывается опять функция foo_find_with_tag(), уже со следующим тэгом внутри списка text_tag
                    # z = users_number
                    foo_find_with_tag(x[y], z)
                    # думаю, чтобы бот бесконечно пытался найти открытого акк, надо ввести цикл while
        # ВЫЗОВ ФУНКЦИИ ДЛЯ ВХОДА В СТРАНИЦУ ЦЕЛЕВОГО ЮЗЕРА ИНСТАГРАМ
        users_number = 1
        foo_find_with_tag(text_tag[count_for_tags], users_number)

        # когда заходим на его страницу, подписываемся
        # ПО СУТИ ТУТ НАДО ПРОВЕРКУ СНАЧАЛА СДЕЛАТЬ, ОТКРЫТЫЙ АКК ИЛИ ЗАКРЫТЫЙ
        # находим кнопку для подписки
        # ЕСЛИ АКК ЗАКРЫТЫЙ, ТО ЕГО CSS селектор будет другим и кнопка не находится
        # ВЕРХНИЙ СЛОЙ НАДО СДЕЛАТЬ ФУНКЦИЕЙ, потом тут сделать иф елс, если открытый акк идем вперед,
        # если закрытый, обратно ищем, но уже по другому хэштегу

        # потом если акк открытый, появляется кнопка для отправки сообщения
        # находим эту кнопку для отправки сообщения
        button_for_send_message = self.browser.find_element(By.CSS_SELECTOR, 'button.sqdOP:nth-child(1)')
        # кликаем по нему
        button_for_send_message.click()
        sleep(5)
        # после открывается диалоговое окно
        # находим поле для ввода сообщения
        find_place_for_write_message = self.browser.find_element(By.CSS_SELECTOR, '.ItkAi > textarea:nth-child(1)')
        text_message = "Hello friend) I'm so sorry. I just testing my instagram bot."
        # передаем туда текст сообщения
        find_place_for_write_message.send_keys(text_message)
        sleep(4)
        # находим кнопку отправить, чтобы отправить сообщение
        button_for_send = self.browser.find_element(By.CSS_SELECTOR, '.JI_ht > button:nth-child(1)')
        # кликаем по этой кнопке
        button_for_send.click()
        sleep(5)



        # # перехожу на директ, нажимаю на кнопку директа
        # # поменял тут путь до кнопки, попробую запускать снова, в этом месте бот останавливался
        # not_now_button3 = self.browser.find_element(By.CSS_SELECTOR, ".xWeGp > svg:nth-child(1)")
        # not_now_button3.click()
        # sleep(5)
        #
        # # я выбираю себя для отправки сообщения и нажимаю на себя, чтобы открыть диалоговое окно
        #
        # not_now_button2 = self.browser.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[1]/div/div/div/div")
        # not_now_button2.click()
        # sleep(5)
        #
        # # ПЫТАЮСЬ ПРОЧЕСТЬ ПОСЛЕДНЮЮ ОТПРАВЛЕННУЮ МНЕ СООБЩЕНИЮ
        # read_last_message = self.browser.find_element(By.XPATH,
        #                                               "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[12]/div[2]/div/div/div/div/div")
        # print(read_last_message.text)
        # sleep(15)
        #
        # # ввод и отправка сообщения
        # # ввод
        # message_input = self.browser.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        # message_input.send_keys('This message i write special stories for my followers in 1mlnlittleactions!!!')
        # sleep(5)
        # # отправка, нажатие на отправить
        #
        # button_send_message = self.browser.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        # button_send_message.click()
        #
        # not_now_button2 = self.browser.find_element(By.XPATH, "/ html / body / div[1] / section / div / div[2] / div / div / div[1] / div[2] / div / div / div / div / div[2] / a / div / div[2] / div[1] / div / div / div / div")
        # not_now_button2.click()
        # sleep(5)
        #
        # not_now_button2 = self.browser.find_element(By.XPATH, "/ html / body / div[1] / section / div / div[2] / div / div / div[2] / div[1] / div / div / div[2] / div / div[2] / button / div / div / div")
        # not_now_button2.click()
        # sleep(5)
        #
        # not_now_button2 = self.browser.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[2]/article/div/div/div/div[1]")
        # not_now_button2.click()
        # sleep(5)
        #
        # not_now_button2 = self.browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span")
        # not_now_button2.click()
        #
        #
        # not_now_button2 = self.browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button/div")
        # not_now_button2.click()
        # sleep(5)
        # comment_input = self.browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
        # comment_input.send_keys('Очень крутой пост. А это комментарий, написанный Ботом).')
        # sleep(5)
        #
        # not_now_button2 = self.browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]")
        # not_now_button2.click()
        #
        # # ПЫТАЮСЬ ПРОЧЕСТЬ ПОСЛЕДНЮЮ ОТПРАВЛЕННУЮ МНЕ СООБЩЕНИЮ
        # read_last_message = self.browser.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[12]/div[2]/div/div/div/div/div")
        # print(read_last_message.text)
        # sleep(60)







class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.instagram.com/")
    def go_to_login_page(self):
        return LoginPage(self.browser)