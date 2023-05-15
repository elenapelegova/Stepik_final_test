from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def there_is_text_basket_is_empty(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, "There is no text Basket is empty"

    def there_are_no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in the basket, but they shouldn't be"