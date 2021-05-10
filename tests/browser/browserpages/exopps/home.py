# -*- coding: utf-8 -*-
"""Export Opportunities Home Page Object."""
import logging

from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import common_selectors
from browserpages.common_actions import check_url, go_to_url

NAME = "Home"
SERVICE = Service.EXPORT_OPPORTUNITIES
TYPE = PageType.HOME
URL = URLs.EXOPPS_LANDING.absolute
PAGE_TITLE = "Export opportunities"
SELECTORS = {}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=True)
    logging.debug("All expected elements are visible on '%s' page", NAME)
