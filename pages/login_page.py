from pages.base_page import BasePage


class LoginPage(BasePage):

    # ---------- Locators (change here if the site changes) ----------
    USERNAME_INPUT = "[placeholder='Username']"
    PASSWORD_INPUT = "[placeholder='Password']"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message-container"

    # ---------- Actions ----------
    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def click_login_only(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_visible(self):
        return self.is_visible(self.ERROR_MESSAGE)
