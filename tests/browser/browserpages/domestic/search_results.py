# -*- coding: utf-8 -*-
"""Domestic Search Result Page object"""

import logging
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType
from browserpages.common_actions import (
    Selector,
    assertion_msg,
    check_url,
    find_element,
    find_elements,
    find_selector_by_name,
    go_to_url,
    scroll_to,
    take_screenshot,
)

NAME = "Search results"
SERVICE = Service.DOMESTIC
TYPE = PageType.SEARCH_RESULTS
URL = URLs.DOMESTIC_SEARCH.absolute

PAGES = Selector(By.CSS_SELECTOR, "ol.navigation li")
PAGINATION = Selector(By.CSS_SELECTOR, "div.pagination")
ACTIVE_PAGE = Selector(By.CSS_SELECTOR, ".pagination span.active")
NEXT = Selector(By.CSS_SELECTOR, ".pagination a.pagination-next")
PREVIOUS = Selector(By.CSS_SELECTOR, "a.pagination-previous[rel=prev]")
SUBMIT_BUTTON = Selector(
    By.CSS_SELECTOR, "#search-again-input ~ input[type=submit]", type=ElementType.BUTTON
)
SEARCH_RESULTS = Selector(By.CSS_SELECTOR, "ul.results li")
SELECTORS = {
    "form": {
        "search box": Selector(By.ID, "search-again-input", type=ElementType.INPUT),
        "search button": SUBMIT_BUTTON,
    },
    "results": {
        "itself": Selector(By.ID, "search-results-list"),
        "active_page": ACTIVE_PAGE,
        "pagination": PAGINATION,
        "browserpages": PAGES,
        "search results": SEARCH_RESULTS,
        "next": NEXT,
    },
    "consequent results": {"previous": PREVIOUS},
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
    logging.debug("All expected elements are visible on '%s' page", NAME)


def should_see_page_number(driver: WebDriver, page_num: int):
    scroll_to(driver, find_element(driver, ACTIVE_PAGE))
    take_screenshot(driver, NAME)
    selector = find_element(driver, ACTIVE_PAGE)

    with assertion_msg(f"Expected to see {page_num} but got {int(selector.text)}"):
        assert int(selector.text) == page_num


def click_on_result_of_type(driver: WebDriver, type_of: str):
    results = find_elements(driver, SEARCH_RESULTS)
    results_of_matching_type = [
        result
        for result in results
        if result.find_element_by_css_selector("span.type").text.lower()
        == type_of.lower()
    ]

    with assertion_msg(
        f"Expected to see at least 1 search result of type '{type_of}' but found none"
    ):
        assert results_of_matching_type
    logging.debug(f"Found {len(results_of_matching_type)} results of type '{type_of}'")
    result = random.choice(results_of_matching_type)
    result_link = result.find_element_by_css_selector("a")
    logging.debug(
        f"Will click on {result_link.text} -> {result_link.get_property('href')}"
    )
    result_link.click()


def has_pagination(driver: WebDriver, min_page_num: int):
    scroll_to(driver, find_element(driver, PAGINATION))
    take_screenshot(driver, NAME)
    selectors = find_elements(driver, PAGES)
    with assertion_msg(
        f"Expected to see more that {min_page_num} search results page but got just {len(selectors)}"
    ):
        assert len(selectors) > min_page_num


def search(driver: WebDriver, phrase: str):
    search_input = find_element(driver, find_selector_by_name(SELECTORS, "search box"))
    search_button = find_element(
        driver, find_selector_by_name(SELECTORS, "search button")
    )
    search_input.clear()
    search_input.send_keys(phrase)
    search_button.click()
