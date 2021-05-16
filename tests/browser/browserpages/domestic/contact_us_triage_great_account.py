# -*- coding: utf-8 -*-
"""Domestic - Domestic Contact us - Great.gov.uk account"""
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
    choose_one_form_option_except,
    find_element,
    get_selectors,
    go_to_url,
    take_screenshot,
)
from browserpages.domestic import (
    contact_us_short_domestic,
    contact_us_triage_great_account_dedicated_support_content as SUPPORT_CONTENT,
)

NAME = "Great.gov.uk account"
SERVICE = Service.DOMESTIC
TYPE = PageType.DOMESTIC_CONTACT_US
URL = URLs.CONTACT_US_GREAT_ACCOUNT.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

SUBMIT_BUTTON = Selector(
    By.CSS_SELECTOR, "div.exred-triage-form button", type=ElementType.BUTTON
)
SELECTORS = {
    "form": {
        "itself": Selector(By.CSS_SELECTOR, "#lede form"),
        "i have not received an email confirmation": Selector(
            By.CSS_SELECTOR,
            "input[value='no-email-confirmation']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "i need to reset my password": Selector(
            By.CSS_SELECTOR,
            "input[value='password-reset']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "my companies house login is not working": Selector(
            By.CSS_SELECTOR,
            "input[value='companies-house-login']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "i do not know where to enter my verification code": Selector(
            By.CSS_SELECTOR,
            "input[value='verification-code']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "i have not received my letter containing the verification code": Selector(
            By.CSS_SELECTOR,
            "input[value='no-verification-letter']",
            type=ElementType.RADIO,
            is_visible=False,
        ),
        "i have not received a verification code": Selector(
            By.CSS_SELECTOR,
            "input[value='verification-missing']",
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
    "i have not received an email confirmation": SUPPORT_CONTENT,
    "i need to reset my password": SUPPORT_CONTENT,
    "my companies house login is not working": SUPPORT_CONTENT,
    "i do not know where to enter my verification code": SUPPORT_CONTENT,
    "i have not received my letter containing the verification code": SUPPORT_CONTENT,
    "i have not received a verification code": SUPPORT_CONTENT,
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


def pick_random_radio_option_and_submit(driver: WebDriver, ignored: List[str]):
    radio_selectors = get_selectors(SELECTORS["form"], ElementType.RADIO)
    selected = choose_one_form_option_except(driver, radio_selectors, ignored)
    take_screenshot(driver, "Before submitting the form")
    button = find_element(
        driver, SUBMIT_BUTTON, element_name="Submit button", wait_for_it=False
    )
    button.click()
    take_screenshot(driver, "After submitting the form")
    return POs[selected.lower()]
