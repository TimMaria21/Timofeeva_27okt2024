url_ui =  "https://altaivita.ru/"
url_api = "https://altaivita.ru/engine/cart/"


login = 'ti44m4r@yandex.ru'
password = 'r4m44it!'

payload = {
    "product_id": "2306",
    "LANG_key": "ru",
    "S_wh": "1",
    "S_CID": "344585df62427a34aba3b58e535e003a",
    "S_cur_code": "rub",
    "S_koef": "1",
    "quantity": "1",
    "S_hint_code": "",
    "S_customerID": "341361"
    }
headers = {"Content-Type": "application/x-www-form-urlencoded"}

body = {
    "itemID": "626332",
    "action": "update_quantity",
    "quantity": "1",
    "LANG_key": "ru",
    "S_wh": "1",
    "S_CID": "344585df62427a34aba3b58e535e003a",
    "S_cur_code": "rub",
    "S_koef": "1",
    "S_hint_code": "",
    "S_customerID": "341361"
    }