# -*- coding: utf-8 -*-
"""Domestic - Domestic Contact us - What can we help you with?"""
import logging
from types import ModuleType
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType
from browserpages.common_actions import (
    Selector,
    check_url,
    choose_one_form_option,
    find_element,
    get_selectors,
    go_to_url,
    take_screenshot,
)
from browserpages.domestic import (
    contact_us_long_export_advice_comment,
    contact_us_office_finder,
    contact_us_short_domestic,
    contact_us_triage_great_services,
    domestic_eu_exit_contact_us,
    ukef_your_details,
)

NAME = "What can we help you with?"
SERVICE = Service.DOMESTIC
TYPE = PageType.DOMESTIC_CONTACT_US
URL = URLs.CONTACT_US_DOMESTIC.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

SUBMIT_BUTTON = Selector(
    By.CSS_SELECTOR, "div.exred-triage-form button", type=ElementType.BUTTON
)
SELECTORS = {
    "form": {
        "itself": Selector(By.CSS_SELECTOR, "#lede form"),
        "find your local trade office": Selector(
            By.CSS_SELECTOR,
            "input[value='trade-office']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "advice to export from the uk": Selector(
            By.CSS_SELECTOR,
            "input[value='export-advice']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "great.gov.uk account and services support": Selector(
            By.CSS_SELECTOR,
            "input[value='great-services']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "uk export finance (ukef)": Selector(
            By.CSS_SELECTOR,
            "input[value='finance']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "brexit enquiries": Selector(
            By.CSS_SELECTOR,
            "input[value='euexit']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "events": Selector(
            By.CSS_SELECTOR,
            "input[value='events']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "defence and security organisation (dso)": Selector(
            By.CSS_SELECTOR,
            "input[value='dso']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "other": Selector(
            By.CSS_SELECTOR,
            "input[value='other']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "submit": SUBMIT_BUTTON,
        "back": Selector(
            By.CSS_SELECTOR,
            "form button[name='wizard_goto_step']",
            type=ElementType.LINK,
        ),
    }
}
POs = {
    "find your local trade office": contact_us_office_finder,
    "advice to export from the uk": contact_us_long_export_advice_comment,
    "great.gov.uk account and services support": contact_us_triage_great_services,
    "uk export finance (ukef)": ukef_your_details,
    "brexit enquiries": domestic_eu_exit_contact_us,
    "events": contact_us_short_domestic,
    "defence and security organisation (dso)": contact_us_short_domestic,
    "other": contact_us_short_domestic,
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)


def should_see_form_choices(driver: WebDriver, names: List[str]):
    radio_selectors = get_selectors(SELECTORS["form"], ElementType.RADIO)
    for name in names:
        radio_selector = radio_selectors[name.lower()]
        find_element(driver, radio_selector, element_name=name, wait_for_it=False)
    logging.debug(
        f"All expected form choices: '{names}' are visible on " f"{driver.current_url}"
    )


def pick_radio_option_and_submit(driver: WebDriver, name: str) -> ModuleType:
    radio_selectors = get_selectors(SELECTORS["form"], ElementType.RADIO)
    choose_one_form_option(driver, radio_selectors, name)
    take_screenshot(driver, "Before submitting the form")
    button = find_element(
        driver, SUBMIT_BUTTON, element_name="Submit button", wait_for_it=False
    )
    button.click()
    take_screenshot(driver, "After submitting the form")
    return POs[name.lower()]
