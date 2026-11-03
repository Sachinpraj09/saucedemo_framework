from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config import FIRST_NAME, LAST_NAME, POSTAL_CODE


# TC10 - Full checkout flow
def test_checkout_flow(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.click_checkout()

    checkout.fill_details(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout.finish_order()

    assert checkout.get_success_message() == "Thank you for your order!"
