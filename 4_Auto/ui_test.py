import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from ui_page import Ui
from config import url_ui, login, password



@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.step("Добавить товар в корзину")
def test_add_to_cart(driver: WebDriver):
    driver.get(url_ui)
    ui = Ui(driver)
    with allure.step('Войти в линчый кабинет'):
        ui.authorization(login, password)
    with allure.step('Ввести в поисковик название продукта'):
        product_name = "Бальзам Иммунитет, 200 мл"
    ui.product_search(product_name)
    with allure.step('Перейти в корзину'):
        ui.adding_to_cart()
    ui.go_to_cart()
    with allure.step('Проверить совпадают ли полученные данные с веденными нами данными'):
        assert ui.product_name_to_cart() == product_name


@allure.step("Изменить количество товара в корзине")
def test_alter_quantity_to_cart(driver: WebDriver):
    driver.get(url_ui)
    ui = Ui(driver)
    with allure.step('Войти в линчый кабинет'):
        ui.authorization(login, password)
    product_name = "каркаде (гибискус)"
    ui.product_search(product_name)
    with allure.step('Перейти в корзину'):
        ui.adding_to_cart()
    ui.go_to_cart()
    with allure.step('Увеличить количество товара'):
        ui.increasing_quantity()
    with allure.step('Проверить количество товара в корзине'):
        assert ui.quantity_product_to_cart() == '2'


@allure.step("Удалить товар из корзины")
def test_delete_from_cart(driver: WebDriver):
    driver.get(url_ui)
    ui = Ui(driver)
    with allure.step('Войти в линчый кабинет'):
        ui.authorization(login, password)
    with allure.step('Ввести в поисковик название продукта'):
        product_name = "Кедровое масло 100 мл"
    ui.product_search(product_name)
    with allure.step('Перейти в корзину'):
        ui.adding_to_cart()
    ui.go_to_cart()
    with allure.step('Удалить товар из корзины'):
        result_to_delete= ui.delete_product_in_cart("Кедровое масло 100 мл")
    with allure.step("Проверяем, что товар действительно отсутствует в корзине."):
        assert result_to_delete is True