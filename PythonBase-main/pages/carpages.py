from .base_page import BasePage
from selenium.webdriver.common.by import By

class Carpages (BasePage):
    addcar = '.btn.btn-primary'
    openmodalwindow = ".modal-content"
    __selectbrand = "#addCarBrand"
    __selectmodel = "#addCarModel"
    __inputmillage = "#addCarMileage"
    __buttonok = ".modal-content .btn.btn-primary"
    __brandford = "//select[@id='addCarBrand']/option[contains(text(),'Ford')]"
    __modelfocus = "//*[@id='addCarModel']/option[2]"
    checkmillage = "ul.car-list>li:first-child input[name='miles']"

    def click_authbyaddcar(self):
        self.browser.find_element(By.CSS_SELECTOR, self.addcar).click()

    def openmodalwindow(self):
        return self.is_element_clickable(By.CSS_SELECTOR, self.openmodalwindow)

    def selectbrand(self):
        self.wait_and_click_on_element(By.CSS_SELECTOR, self.__selectbrand)

    def brandford (self):
        self.wait_and_click_on_element(By.XPATH, self.__brandford)

    def selectmodel (self):
        self.wait_and_click_on_element(By.CSS_SELECTOR, self.__selectmodel)

    def modelfocus (self):
        self.wait_and_click_on_element(By.XPATH, self.__modelfocus)

    def inputmillage (self,millage = 1234):
        self.browser.find_element(By.CSS_SELECTOR, self.__inputmillage).send_keys(millage)

    def buttonok (self):
        self.browser.find_element(By.CSS_SELECTOR, self.__buttonok).click()

    def millagecheck (self):
        return self.browser.find_element(By.CSS_SELECTOR, self.checkmillage).get_attribute('value')


