from playwright.sync_api import sync_playwright, Browser
import pytest
from pytest import FixtureRequest

BROWSERS = ["chromium"]


@pytest.fixture(scope="session", params=BROWSERS)
def browser(request: FixtureRequest):
    """Фикстура для запуска браузера перед тестом."""
    with sync_playwright() as p:
        browser_name = request.param
        browser = p[browser_name].launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser):
    """Фикстура для открытия новой страницы перед каждым тестом."""
    page = browser.new_page()
    yield page
    page.close()
