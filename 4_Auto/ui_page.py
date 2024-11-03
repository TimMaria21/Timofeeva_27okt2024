import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Ui():
   
    def __init__(self, url) -> None:
        self.url = url

    @allure.step("Вход в личный кабинет")
    def authorization(self, login: str, password: str) -> None:
        self.url.find_element(By.CSS_SELECTOR, "span.header__personal-name").click()
        self.url.find_element(By.CSS_SELECTOR, "input.aj_login").send_keys(login)
        self.url.find_element(By.CSS_SELECTOR, "button.main-btn.green.sign-in").click()
        self.url.find_element(By.CSS_SELECTOR, "input.password").send_keys(password)
        self.url.find_element(By.XPATH, '//*[@id="form_login_second_step"]/div[2]/div[2]/button').click()
        WebDriverWait(self.url, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "main.main")))


   
    @allure.step("Поиск продукта с помощью поисковика")
    def product_search(self, product: str) -> None:
        WebDriverWait(self.url, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "input.searchpro__field-input.js-searchpro__field-input"))).send_keys(product)
        WebDriverWait(self.url, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.searchpro__field-button.js-searchpro__field-button"))).click()
        WebDriverWait(self.url, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.category__filter")))

        
 
    @allure.step("Добавление продукта в корзину")
    def adding_to_cart(self)-> None:
        WebDriverWait(self.url, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.product__buy"))).click()
       

    @allure.step("Перейти в корзину")
    def go_to_cart(self)-> None:
        WebDriverWait(self.url, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "a.header__basket-link.ga_link_to_cart.grid_container_mobile_menu.pdd_cart"))).click()
        WebDriverWait(self.url, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-go-over.link-gray.ga_link_to_cart"))).click()
        WebDriverWait(self.url, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.basket__result-top")))
        


    @allure.step("Получить название продукта в корзине")
    def product_name_to_cart(self)-> None:
        return self.url.find_element(By.CSS_SELECTOR, 'a.basket__name').text
    

    @allure.step("Увеличение количества товара в корзине")
    def increasing_quantity(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "button.more.js-plus").click()
        sleep(3)

    @allure.step("Получить количество продукта в корзине")
    def quantity_product_to_cart(self)-> None:
        return self.url.find_element(By.CSS_SELECTOR, 'span.num').text


    @allure.step("Удалить необходимый товар из корзины.")
    def delete_product_in_cart(self, product_name_to_delete: str) -> bool:
        WebDriverWait(self.url, 20).until
        (EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.basket__delete i")))
        delete_buttons = self.url.find_elements(By.CSS_SELECTOR, "div.basket__delete i")
        products = self.url.find_elements(By.CSS_SELECTOR, "a.basket__name")
        for i in range(len(products)):
            if products[i].text.strip() == product_name_to_delete:
                delete_buttons[i].click()
                return True
        return False