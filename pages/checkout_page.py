from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # ---------- Locators ----------
    FIRST_NAME_INPUT = "[placeholder='First Name']"
    LAST_NAME_INPUT = "[placeholder='Last Name']"
    POSTAL_CODE_INPUT = "[placeholder='Zip/Postal Code']"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    SUCCESS_MESSAGE = ".complete-header"

    # ---------- Actions ----------
    def fill_details(self, first, last, postal):
        self.fill(self.FIRST_NAME_INPUT, first)
        self.fill(self.LAST_NAME_INPUT, last)
        self.fill(self.POSTAL_CODE_INPUT, postal)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
