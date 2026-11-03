import os
import base64
import pytest
import pytest_html

from config import BASE_URL, INVENTORY_URL, USERNAME, PASSWORD


# ---------------- Authentication (login once, reuse the session) ----------------
@pytest.fixture(scope="session")
def auth_state(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto(BASE_URL)
    page.locator("[placeholder='Username']").fill(USERNAME)
    page.locator("[placeholder='Password']").fill(PASSWORD)
    page.locator("#login-button").click()

    # Save cookies + localStorage so other tests can reuse the login
    state = context.storage_state()
    context.close()
    return state


# ---------------- Fixture: fresh, NOT logged in (for login tests) ----------------
@pytest.fixture
def login_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


# ---------------- Fixture: already logged in (for all other tests) ----------------
@pytest.fixture
def logged_in_page(browser, auth_state):
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    page.goto(INVENTORY_URL)
    yield page
    context.close()


# ---------------- Report: screenshot ONLY for failed tests ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("logged_in_page")
        if page is None:
            page = item.funcargs.get("login_page")

        if page:
            os.makedirs("screenshots", exist_ok=True)
            path = f"screenshots/{item.name}.png"

            # Take screenshot and save it
            image = page.screenshot(path=path)

            # Attach screenshot to the HTML report
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(base64.b64encode(image).decode()))
            report.extras = extras
