from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        
    def should_item_in_basket(self):
        self.should_cost_equal()
        self.should_name_equal()

    def should_cost_equal(self):
        item_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert item_basket_cost.text == item_product_cost.text, "Prices in basket and in product page are not equal"

    def should_name_equal(self):
        items_strong = self.browser.find_elements(*ProductPageLocators.BASKET_STRONG_NAMES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = ''
        names_equal = False
        for item_strong in items_strong:
            if item_strong.text == product_name:
                names_equal = True
        assert names_equal, "Names of product are not equal"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is present, but should not be"
           
    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"