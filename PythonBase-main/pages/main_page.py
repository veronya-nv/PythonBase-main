from .base_page import BasePage
from selenium.webdriver.common.by import By



class MainPage(BasePage):
    modalWindow = ".modal-header"
    SignInButton = ".btn.btn-outline-white.header_signin"
    inputLogin = "#signinEmail"
    inputPassword = "#signinPassword"
    checkboxRememberMe = "#remember"
    buttonForgotPassword = "//button[@_ngcontent-miv-c51]"
    loginButton = ".modal-footer.d-flex.justify-content-between > .btn.btn-primary"
    Authbyguest = "button.header-link.-guest"


    def click_sign_in(self):
        self.wait_and_click_on_element(By.CSS_SELECTOR, self.SignInButton)

    def is_open_modal_window(self):
        return self.is_element_clickable(By.CSS_SELECTOR, self.modalWindow)

    def enter_login(self, login):
        self.browser.find_element(By.CSS_SELECTOR, self.inputLogin).send_keys(login)

    def enter_password(self, password):
        self.browser.find_element(By.CSS_SELECTOR, self.inputPassword).send_keys(password)

    def click_login_button(self):
        self.browser.find_element(By.CSS_SELECTOR, self.loginButton).click()

    def click_authbygest(self):
        self.browser.find_element(By.CSS_SELECTOR, self.Authbyguest).click()