from pages.base_page import BasePage


class CartPage(BasePage):

    # ---------- Locators ----------
    CART_ITEM = ".cart_item"
    CART_ITEM_NAME = ".cart_item .inventory_item_name"
    REMOVE_BACKPACK_BUTTON = "#remove-sauce-labs-backpack"
    CHECKOUT_BUTTON = "#checkout"

    # ---------- Actions ----------
    def get_item_name(self):
        return self.get_text(self.CART_ITEM_NAME)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def is_item_visible(self):
        return self.is_visible(self.CART_ITEM)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
