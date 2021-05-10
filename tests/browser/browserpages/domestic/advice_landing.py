# -*- coding: utf-8 -*-
"""Domestic Common Advice Page Object."""
import random
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import extract_attributes_by_css
from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    go_to_url,
    wait_for_page_load_after_action,
)
from browserpages.domestic import actions as domestic_actions

NAME = "Advice landing"
TYPE = PageType.LANDING
SERVICE = Service.DOMESTIC
URL = URLs.DOMESTIC_ADVICE.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

ARTICLE_LINKS = Selector(
    By.CSS_SELECTOR, "#-list-section a", type=ElementType.LINK
)
SELECTORS = {
    "advice & guidance tiles": {
        "itself": Selector(By.CSS_SELECTOR, "#-list-section"),
        "cards": Selector(By.CSS_SELECTOR, "#-list-section div.card"),
        "articles": ARTICLE_LINKS,
        "article images": Selector(By.CSS_SELECTOR, "#-list-section .card-image"),
    }
}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.DOMESTIC_HERO_WO_LINK)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def open_any_article(driver: WebDriver) -> str:
    links = extract_attributes_by_css(
        driver.page_source, ARTICLE_LINKS.value, attrs=["href"]
    )
    selected_link = random.choice(links)

    link = driver.find_element_by_css_selector(f"a[href='{selected_link['href']}']")
    with wait_for_page_load_after_action(driver):
        link.click()
    return selected_link["text"]


def search(driver: WebDriver, phrase: str):
    domestic_actions.search(driver, phrase)
