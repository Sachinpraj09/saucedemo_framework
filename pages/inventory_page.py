from pages.base_page import BasePage


class InventoryPage(BasePage):

    # ---------- Locators ----------
    PAGE_TITLE = ".title"
    MENU_BUTTON = "#react-burger-menu-btn"
    ALL_ITEMS_LINK = "#inventory_sidebar_link"
    ABOUT_LINK = "#about_sidebar_link"
    LOGOUT_LINK = "#logout_sidebar_link"
    SORT_DROPDOWN = ".product_sort_container"
    PRICE = ".inventory_item_price"          # many prices on page, first one is used below
    ADD_BACKPACK_BUTTON = "#add-to-cart-sauce-labs-backpack"
    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"

    # ---------- Actions ----------
    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def open_menu(self):
        self.click(self.MENU_BUTTON)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)

    def sort_by(self, value):
        # value examples: "az", "za", "lohi", "hilo"
        self.select_option(self.SORT_DROPDOWN, value)

    def get_first_price(self):
        return self.page.locator(self.PRICE).first.inner_text()

    def add_backpack(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def is_cart_badge_visible(self):
        return self.is_visible(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_ICON)
