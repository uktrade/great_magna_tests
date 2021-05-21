# -*- coding: utf-8 -*-
"""Domestic - International Contact us - What would you like to know more about?"""
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
    wait_for_page_load_after_action,
)
from browserpages.international import (
    international_contact_us,
    international_contact_us_capital_invest,
    international_transition_period_enquiries_contact_us,
    trade_contact_us,
)
#from browserpages.invest import contact_us as invest_contact_us

NAME = "What would you like to know more about?"
SERVICE = Service.DOMESTIC
TYPE = PageType.INTERNATIONAL_CONTACT_US
URL = URLs.CONTACT_US_INTERNATIONAL.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

SUBMIT_BUTTON = Selector(
    By.CSS_SELECTOR, "#content form button.button", type=ElementType.BUTTON
)
SELECTORS = {
    "form": {
        "itself": Selector(By.CSS_SELECTOR, "#lede form"),
        "expanding to the uk": Selector(
            By.ID, "id_choice_0", type=ElementType.RADIO, is_visible=False
        ),
        "investing capital in the uk": Selector(
            By.ID, "id_choice_1", type=ElementType.RADIO, is_visible=False
        ),
        "find a uk business partner": Selector(
            By.ID, "id_choice_2", type=ElementType.RADIO, is_visible=False
        ),
        "the transition period": Selector(
            By.ID, "id_choice_3", type=ElementType.RADIO, is_visible=False
        ),
        "other": Selector(
            By.ID, "id_choice_4", type=ElementType.RADIO, is_visible=False
        ),
        "submit": SUBMIT_BUTTON,
        "back": Selector(By.CSS_SELECTOR, "#content > div:nth-child(2) > form > div > div > button", type=ElementType.LINK),
    }
}
POs = {
    #"expanding to the uk": invest_contact_us,
    "investing capital in the uk": international_contact_us_capital_invest,
    "find a uk business partner": trade_contact_us,
    "the transition period": international_transition_period_enquiries_contact_us,
    "other": international_contact_us,
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
    with wait_for_page_load_after_action(driver, timeout=15):
        button.click()
    return POs[name.lower()]
