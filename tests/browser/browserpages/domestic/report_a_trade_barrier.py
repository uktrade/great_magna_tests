# -*- coding: utf-8 -*-
"""Domestic - Report a trade barrier page"""
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from browserpages.common_actions import Selector, check_for_sections, check_url, go_to_url
from browserpages.domestic import actions as domestic_actions

NAME = "Report a trade barrier"
SERVICE = Service.DOMESTIC
TYPE = PageType.ARTICLE
URL = URLs.TRADE_BARRIERS_LANDING.absolute

SELECTORS = {
    "description": {
        "intro sections": Selector(By.CSS_SELECTOR, "p.lede"),
        "report a barrier": Selector(
            By.CSS_SELECTOR, "a.button", type=ElementType.LINK
        ),
        "contact the relevant british embassy": Selector(
            By.CSS_SELECTOR, "section div.grid-row p > a", type=ElementType.LINK
        ),
        "report steps": Selector(By.CSS_SELECTOR, "ol.list.big-number-list"),
    }
}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def search(driver: WebDriver, phrase: str):
    domestic_actions.search(driver, phrase)
