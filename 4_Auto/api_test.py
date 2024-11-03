import pytest
import allure
from config import url_api
from api_page import API


api = API(url_api)


@allure.feature("API тесты для проверки функционала корзины.")
@allure.title("Тест на добавление товара в корзину.")
def test_add_product_to_cart():
    product_id = "6987"
    result_post_request, status_code = api.add_product_to_cart(product_id)
    with allure.step(
        "Проверяем, что статус код, ключи ответа в JSONе соответствуют успешной операции."
    ):
        assert status_code == 200
        assert result_post_request ['status'] == 'ok'
        assert result_post_request["btn_text"] == "Добавлено"


@allure.feature("API тесты для проверки функционала корзины.")
@allure.title("Тест на изменение количества товара в корзине")
def test_change_amount_product():
    item_id = "627533"
    quantity = "5"
    result_post_request, status_code = api.change_amount_product(item_id, quantity)
    with allure.step(
        "Проверяем, что статус код, ключи ответа в JSONе соответствуют успешной операции, \
            а количестово товара изменилось на 5"
    ):
        assert status_code == 200
        assert result_post_request ['status'] == 'ok'
        assert result_post_request["total_quantity_items"] == "5"


@allure.feature("API тесты для проверки функционала корзины.")
@allure.title("Тест на удаление товара из корзины.")
def test_delete_product_from_cart():
    product_id = "3590"
    result_post_request, status_code = api.add_product_to_cart(product_id)
    with allure.step(
        "Проверяем, что статус код, ключи ответа в JSONе соответствуют успешной операции."
    ):
        assert status_code == 200
        assert result_post_request ['status'] == 'ok'
        assert result_post_request["btn_text"] == "Добавлено"
    result_delete_product, status_code = api.delete_product_from_cart(product_id)
    with allure.step("Проверяем, что категория товара была удалена из корзины."):
        assert status_code == 200
        assert result_delete_product["status"] == "ok"
        assert result_delete_product["price_to_delete"] == "210"
   