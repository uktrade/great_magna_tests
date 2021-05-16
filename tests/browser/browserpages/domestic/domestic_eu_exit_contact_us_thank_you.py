# -*- coding: utf-8 -*-
"""Domestic - Domestic EU Exit Contact us - Thank you for your enquiry."""
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages.common_actions import Selector, check_url

NAME = "Brexit help"
SERVICE = Service.DOMESTIC
TYPE = PageType.THANK_YOU
URL = URLs.CONTACT_US_DOMESTIC_BREXIT_CONTACT_SUCCESS.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

PDF_LINKS = Selector(By.CSS_SELECTOR, "#documents-section a.link")
SELECTORS = {
    "beta bar": {
        "self": Selector(By.ID, "header-beta-bar"),
        "beta bar": Selector(By.CSS_SELECTOR, "#header-beta-bar strong"),
        "feedback": Selector(By.CSS_SELECTOR, "#header-beta-bar a"),
    },
    "confirmation": {
        "itself": Selector(By.ID, "confirmation-section"),
        "heading": Selector(
            By.CSS_SELECTOR, "#confirmation-section div.heading-container"
        ),
    },
    "report this page": {
        "self": Selector(By.CSS_SELECTOR, "section.error-reporting"),
        "report link": Selector(By.CSS_SELECTOR, "section.error-reporting a"),
    },
}


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=True)
    logging.debug(f"All expected elements are visible on '{URL}'")
