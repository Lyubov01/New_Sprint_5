from selenium.webdriver.common.by import By


class Header:
    login_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # Кнопка "Войти в аккаунт" на главной странице

    My_account  = (By.XPATH, "//p[normalize-space()='Личный Кабинет']")
    # Кнопка "Личный кабинет" в шапке

    constructor_link  = (By.XPATH, "//p[normalize-space()='Конструктор']")  
    # Ссылка "Конструктор" в шапке

    logo_Stellar_Burgers = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")  
    # Логотип Stellar Burgers


# Форма входа

    title_form = (By.XPATH, "//h2[normalize-space()='Вход']")  
    # Заголовок формы входа

    email= (By.XPATH, "//label[normalize-space()='Email']/following::input[1]")  
    # Поле ввода Email

    password= (By.XPATH, "//label[normalize-space()='Пароль']/following::input[@type='password'][1]")  
    # Поле ввода пароля

    butoon_log_in= (By.XPATH, "//button[normalize-space()='Войти']")  
    # Кнопка "Войти"

    link_register= (By.XPATH, "//a[@href='/register' and normalize-space()='Зарегистрироваться']")  
    # Ссылка "Зарегистрироваться" под формой

    link_fogot_pasword= (By.XPATH, "//a[@href='/forgot-password']")  
    # Ссылка "Восстановить пароль"


# Форма регистрации

class RegisterForm:
    register_form_title = (By.XPATH, "//h2[normalize-space()='Регистрация']")  
    # Заголовок формы регистрации

    name= (By.XPATH, "//label[.='Имя']/following::input[1]")  
    # Поле "Имя"

    email_in_register_form= (By.XPATH, "//label[.='Email']/following::input[1]")  
    # Поле "Email"

    password_in_register_form= (By.XPATH, "//label[.='Пароль']/following::input[1]")  
    # Поле "Пароль"

    button_to_register= (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")  
    # Кнопка "Зарегистрироваться"

    error_mes= (By.XPATH, "//*[contains(@class,'input__error') or contains(.,'Минимальный размер пароля') or contains(.,'Некорректный пароль')]")  
    # Сообщение об ошибке при некорректном пароле

    to_log_in_link= (By.XPATH, "//a[normalize-space()='Войти']")  
    # Ссылка "Войти"


# Форма восстановления пароля

class ForgotForm:
    title_fogot_form= (By.XPATH, "//*[contains(.,'Восстановление пароля')][self::h2 or self::p]")  
    # Заголовок "Восстановление пароля"

    to_log_in_link= (By.XPATH, "//a[normalize-space()='Войти']")  
    # Ссылка "Войти"


# Личный кабинет

class AccountPage:
    button_log_out= (By.XPATH, "//button[normalize-space()='Выход']")
    # Кнопка "Выйти" в личном кабинете


# Раздел "Конструктор"

class Constructor:
    Burger_name= (By.XPATH, "//span[normalize-space()='Булки']")
    # Вкладка "Булки"

    Souse_name= (By.XPATH, "//span[normalize-space()='Соусы']")
    # Вкладка "Соусы"

    filling= (By.XPATH, "//span[normalize-space()='Начинки']")  
    # Вкладка "Начинки"
