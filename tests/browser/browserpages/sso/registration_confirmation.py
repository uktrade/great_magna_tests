# -*- coding: utf-8 -*-
"""SSO Registration Page Object."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages.common_actions import Selector, check_url

NAME = "Registration Confirmation"
SERVICE = Service.SSO
TYPE = PageType.CONFIRMATION
URL = URLs.SSO_EMAIL_CONFIRM.absolute

SIGN_IN_LINK = Selector(By.ID, "header-sign-in-link")
SELECTORS = {
    "general": {
        "title": Selector(By.CSS_SELECTOR, "#content h1"),
        "description": Selector(By.CSS_SELECTOR, "#content p:nth-child(2)"),
        "contact us link": Selector(By.CSS_SELECTOR, "#content p > a"),
        "sign in link": SIGN_IN_LINK,
    }
}


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
