# -*- coding: utf-8 -*-
"""SSO Sign Out Page Object."""
from types import ModuleType
from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType
from browserpages.common_actions import Selector, check_url, go_to_url, submit_form

NAME = "Sign out"
SERVICE = Service.SSO
TYPE = PageType.FORM
URL = URLs.SSO_LOGOUT.absolute
PAGE_TITLE = "Sign out - great.gov.uk"

SELECTORS = {
    "form": {
        "title": Selector(By.CSS_SELECTOR, "#content h1.heading-xlarge"),
        "sign in button": (
            Selector(By.CSS_SELECTOR, "form button", type=ElementType.SUBMIT)
        ),
    }
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])
