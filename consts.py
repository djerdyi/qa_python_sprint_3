BASE_URL = "https://stellarburgers.nomoreparties.site/"

# Authorization
LOGIN = 'gusev_07@gmail.com'
PASSWORD = '123123'
VALID_PASSWORD_LENGTH = 6
INVALID_PASSWORD_LENGTH = 4

# Locators
LOC_HEADER_BUTTON_CONSTRUCTOR = '(.//a[@class="AppHeader_header__link__3D_hX" and @href="/"])' # Кнопка "Конструктор" в шапке
LOC_HEADER_BUTTON_ORDERS = '(.//a[@class="AppHeader_header__link__3D_hX" and @href="/feed"])' # Кнопка "Лента Заказов" в шапке
LOC_HEADER_BUTTON_LOGO = '(.//div[@class="AppHeader_header__logo__2D0X2"]/a)' # Логотип в шапке
LOC_HEADER_BUTTON_PERSONAL_CABINET = '(.//a[@class="AppHeader_header__link__3D_hX" and @href="/account"])' # Кнопка "Личный Кабинет" в шапке
LOC_MAIN_BUTTON_LOGIN = '(.//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"])' # Кнопка "Войти в аккаунт" на главной
LOC_MAIN_BUTTON_MAKE_ORDER = '(.//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"])' # Кнопка "Оформить заказ" на главной
LOC_CONSTRUCTOR_DIV_BUNS = '(.//span[text()="Булки"]/parent::div)' # Вкладка "Булки" на главной
LOC_CONSTRUCTOR_DIV_SAUSES = '(.//span[text()="Соусы"]/parent::div)' # Вкладка "Соусы" на главной
LOC_CONSTRUCTOR_DIV_STUFFINGS = '(.//span[text()="Начинки"]/parent::div)' # Вкладка "Начинки" на главной
LOC_CONSTRUCTOR_LI_LAST = '(.//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][last()]/a[last()])' # Последний элемент спсика ингридиентов
CONSTRUCTOR_TAB_CLASS_SELECTED = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'  # Класс активной на данный моммент вкладки
LOC_FEED_HEADER_ORDERS_LIST = '(.//h1[text()="Лента заказов"])' # Заголовок на странице заказов
LOC_LOGIN_INTPUT_EMAIL = '(.//input[@class="text input__textfield text_type_main-default" and @type="text"])' # Поле "email" на странице логина
LOC_LOGIN_INTPUT_PASSWORD = '(.//input[@class="text input__textfield text_type_main-default" and @type="password"])' # Поле "Пароль" на странице логина
LOC_LOGIN_BUTTON_LOGIN = '(.//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"])' # Кнопка "Войти" на странице логина
LOC_LOGIN_LINK_REGISTER = '(.//a[@class="Auth_link__1fOlj" and @href="/register"])' # Ссылка "Зарегистрироваться" на странице логина
LOC_LOGIN_LINK_FORGOT_PASSWORD = '(.//a[@class="Auth_link__1fOlj" and @href="/forgot-password"])' # Кнопка "Восстановить пароль" на странице логина
LOC_REGISTER_INPUT_NAME = '((.//input[@class="text input__textfield text_type_main-default"])[1])' # Поле "Имя" на странице регистрации
LOC_REGISTER_INPUT_EMAIL = '((.//input[@class="text input__textfield text_type_main-default"])[2])' # Поле "Email" на странице регистрации
LOC_REGISTER_INPUT_PASSWORD = '((.//input[@class="text input__textfield text_type_main-default"])[3])' # Поле "Пароль" на странице регистрации
LOC_REGISTER_BUTTON_REGISTER = '(.//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"])' # Кнопка "Зарегистрироваться" на странице регистрации
LOC_REGISTER_PARAGRAPH_USER_EXIST = '(.//p[@class="input__error text_type_main-default" and text()="Такой пользователь уже существует"])' # Текст ошибки при некорректном вводе пароля на странице регистрации
LOC_REGISTER_PARAGRAPH_INCORRECT_PASSWORD = '(.//p[@class="input__error text_type_main-default" and text()="Некорректный пароль"])' # Текст ошибки при попытке зарегистрировать пользователя повторно на странице регистрации
LOC_REGISTER_LINK_LOGIN = '(.//a[@class="Auth_link__1fOlj"])' # Ссылка "Войти" на странице регистрации
LOC_FORGOTPASSWORD_LINK_LOGIN = '(.//a[@class="Auth_link__1fOlj"])' # Ссылка "Войти" на странице восстановления пароля
LOC_ACCOUNT_BUTTON_LOGOUT = '(.//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"])' # Кнопка "Выход" на странице аккаунта
