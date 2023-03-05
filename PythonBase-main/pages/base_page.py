from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)

    def auth_form(self, userName, Password):
        import requests
        r = requests.get(self.url, auth=(userName, Password))
        print(r.request.url, r.text)

    def auth_by_url(self, userName, Password, domain):
        url = 'https://{}:{}@{}'.format(userName, Password, domain)
        self.browser.get(url)


    def open(self):
        self.browser.get(self.url)

    def wait_and_click_on_element(self, how, what, timeout=4):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what))).click()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_element_clickable(self, how, what):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable((how, what)))

    def is_url_changed(self, path_url):
        return WebDriverWait(self.browser, self.timeout).until(EC.url_changes(self.url+path_url))

    def is_displaed(self, how, what):
        return WebDriverWait(self.browser, self.timeout).until(EC.invisibility_of_element_located((how, what)))