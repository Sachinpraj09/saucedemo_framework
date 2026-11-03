from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


# TC05 - Sidebar menu links
def test_sidebar_menu(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.open_menu()

    assert inventory.is_visible(inventory.ALL_ITEMS_LINK)
    assert inventory.is_visible(inventory.ABOUT_LINK)
    assert inventory.is_visible(inventory.LOGOUT_LINK)


# TC06 - Add product to cart
def test_add_product_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_backpack()

    assert inventory.get_cart_count() == "1"


# TC07 - Sort price low to high
def test_sort_price_low_to_high(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("lohi")

    assert inventory.get_first_price() == "$7.99"


# TC08 - Logout
def test_logout(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    login = LoginPage(logged_in_page)

    inventory.logout()

    assert login.is_visible(login.LOGIN_BUTTON)
