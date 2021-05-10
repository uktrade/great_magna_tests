# -*- coding: utf-8 -*-
"""International - Industries page"""
import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    find_element,
    go_to_url,
    take_screenshot,
)

NAME = "Industries"
SERVICE = Service.INTERNATIONAL
TYPE = PageType.LANDING
URL = URLs.INTERNATIONAL_INDUSTRIES.absolute
PAGE_TITLE = "Welcome to great.gov.uk - buy from or invest in the UK"

BREADCRUMB_LINKS = Selector(By.CSS_SELECTOR, ".breadcrumbs a")
SELECTORS = {
    "industry breadcrumbs": {
        "great.gov.uk international": Selector(
            By.CSS_SELECTOR, "nav.breadcrumbs ol > li:nth-child(1) > a"
        )
    },
    "industries": {
        "itself": Selector(By.CSS_SELECTOR, "section.topic-list-section"),
        "industry cards": Selector(By.CSS_SELECTOR, "section.topic-list-section a"),
    },
}
SELECTORS.update(common_selectors.INTERNATIONAL_HEADER)
SELECTORS.update(common_selectors.INTERNATIONAL_HERO)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INTERNATIONAL_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def open_industry(driver: WebDriver, industry_name: str):
    industry_name = industry_name.split(" - ")[1].strip()
    selector = Selector(By.PARTIAL_LINK_TEXT, industry_name)
    logging.debug("Looking for: {}".format(industry_name))
    industry_link = find_element(
        driver, selector, element_name="Industry card", wait_for_it=False
    )
    industry_link.click()
    take_screenshot(driver, NAME + " after opening " + industry_name + " page")
