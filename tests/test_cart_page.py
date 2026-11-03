from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


# TC09 - Cart shows the added product, and it can be removed
def test_cart_add_and_remove_product(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()

    assert cart.get_item_name() == "Sauce Labs Backpack"

    cart.remove_backpack()

    assert not cart.is_item_visible()
