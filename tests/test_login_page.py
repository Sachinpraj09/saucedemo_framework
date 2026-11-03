from pages.login_page import LoginPage
from config import USERNAME, PASSWORD, WRONG_PASSWORD


# TC01 - Valid login
def test_valid_login(login_page):
    login = LoginPage(login_page)

    login.login(USERNAME, PASSWORD)

    assert login.get_url().endswith("/inventory.html")


# TC02 - Wrong password
def test_invalid_login(login_page):
    login = LoginPage(login_page)

    login.login(USERNAME, WRONG_PASSWORD)

    assert login.is_error_visible()
    assert "do not match" in login.get_error_text()


# TC03 - Empty username and password
def test_empty_login(login_page):
    login = LoginPage(login_page)

    login.click_login_only()

    assert "Username is required" in login.get_error_text()


# TC04 - Username entered, password left empty
def test_empty_password(login_page):
    login = LoginPage(login_page)

    login.login(USERNAME, "")

    assert "Password is required" in login.get_error_text()
