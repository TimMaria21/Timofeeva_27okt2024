import requests
from typing import Dict, Any, Tuple
from config import payload, body, headers


class API():
    def __init__(self, url: str) -> None:
        self.url = url


    def add_product_to_cart(self, product_id: str)-> Tuple[Dict[str, Any], int]:
        """Метод позволяет добавить товар в корзину.
        Args:
            product_id (str): id продукта.
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией и статус код.
        """
        payload_new = payload.copy()
        payload_new["product_id"] = product_id
        result_add_to_cart =requests.post(
            self.url + "add_products_to_cart_from_preview.php", 
            data=payload_new, 
            headers=headers
            )
        return result_add_to_cart.json(), result_add_to_cart.status_code
    

    def change_amount_product(self, item_id: str,  quantity: str) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет изменить количество товара.
        Args:
            item_id (str): динамическая величина, id номер товара добавленного в корзину пользователем,
            quantity (str): количество товара.
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией и статус код.
        """
        body_new = body.copy()
        body_new["itemID"] = item_id
        body_new["quantity"] = quantity
        result_change_amount_product =requests.post(
            self.url + "action_with_basket_on_cart_page.php", 
            data=body_new, 
            headers=headers
            )
        return result_change_amount_product.json(), result_change_amount_product.status_code
    

    def delete_product_from_cart(self, product_id) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет удалить категорию товара из корзины.
        Args:
            product_id (str): id продукта.
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией и статус код.
        """
        payload_new = payload.copy()
        payload_new["product_id"] = product_id
        result_delete_from_cart = requests.post(
            self.url + "delete_products_from_cart_preview.php",
            data=payload_new,
            headers=headers,
        )
        return result_delete_from_cart.json(), result_delete_from_cart.status_code