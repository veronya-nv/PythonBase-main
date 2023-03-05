import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Для фикстур можно задавать область покрытия фикстур
# “function” - фикстура будет вызываться один раз для тестового метода
# “class”, -  фикстура будет вызываться один раз для класса,
# “module”,  фикстура будет вызываться один раз для модуля
# “session” - фикстура будет вызываться один раз для для всех тестов, запущенных в данной сессии.
# При описании фикстуры можно указать дополнительный параметр autouse=True,
# который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова:
@pytest.fixture(scope='module', autouse=True)
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=Options())
    browser.maximize_window()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()