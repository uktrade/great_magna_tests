# -*- coding: utf-8 -*-
"""Profile - About"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import common_selectors
from browserpages.common_actions import Selector, check_url, go_to_url

NAME = "About"
SERVICE = Service.PROFILE
TYPE = PageType.FORM
URL = URLs.PROFILE_ABOUT.absolute
PAGE_TITLE = ""

SELECTORS = {
    "tab bar": {
        "itself": Selector(By.CSS_SELECTOR, ".sso-profile-tab-container"),
        "export opportunities": Selector(By.LINK_TEXT, "Export opportunities"),
        "Business profile": Selector(By.LINK_TEXT, "Business profile"),
        "Selling online overseas": Selector(By.LINK_TEXT, "Selling online overseas"),
        "about": Selector(By.LINK_TEXT, "About"),
    },
    "welcome": {"welcome message": Selector(By.ID, "welcome-message")},
}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)
