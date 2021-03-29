# -*- coding: utf-8 -*-
"""Common Language Selector on Import tariff pages"""
import logging
from types import ModuleType

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from browserpages.common_actions import (
    Selector,
    assertion_msg,
    find_element,
    find_selector_by_name,
    take_screenshot,
)

NAME = "Language selector"

LANGUAGE_SELECTOR = Selector(By.ID, "great-header-language-select")
ELEMENTS_ON = {
    "domestic - home": {
        "English": "en-gb",
        "简体中文": "zh-hans",
        "Deutsch": "de",
        "日本語": "ja",
        "español": "es",
        "Português": "pt",
        "العربيّة": "ar",
        "Français": "fr",
    },
    "find a supplier - landing": {
        "English": "en-gb",
        "简体中文": "zh-hans",
        "Deutsch": "de",
        "日本語": "ja",
        "español": "es",
        "Português": "pt",
        "العربيّة": "ar",
        "Français": "fr",
    },
    "international - landing": {
        "English": "en-gb",
        "简体中文": "zh-hans",
        "Deutsch": "de",
        "日本語": "ja",
        "español": "es",
        "Português": "pt",
        "العربيّة": "ar",
        "Français": "fr",
    },
    "invest - landing": {
        "English": "en-gb",
        "简体中文": "zh-hans",
        "Deutsch": "de",
        "日本語": "ja",
        "español": "es",
        "Português": "pt",
        "Français": "fr",
    },
}
LANGUAGE_INDICATOR_VALUES = {
    "English": "en-gb",
    "简体中文": "zh-hans",
    "Deutsch": "de",
    "日本語": "ja",
    "español": "es",
    "Português": "pt",
    "العربيّة": "ar",
    "Français": "fr",
}


def close(driver: WebDriver, page: ModuleType):
    selector = find_selector_by_name(page.SELECTORS, "language selector")
    language_selector = find_element(driver, selector, element_name="language selector")
    language_selector.send_keys(Keys.ESCAPE)


def open(driver: WebDriver, page: ModuleType, *, with_keyboard: bool = False):
    selector = find_selector_by_name(page.SELECTORS, "language selector")
    language_selector = find_element(driver, selector, element_name="language selector")
    if with_keyboard:
        language_selector.send_keys(Keys.ENTER)
    else:
        language_selector.click()


def should_see_it_on(driver: WebDriver, page: ModuleType):
    take_screenshot(driver, NAME + page.NAME)
    selector = find_selector_by_name(page.SELECTORS, "language selector")
    language_selector = find_element(driver, selector, element_name="language selector")
    with assertion_msg(f"Language selector is not visible on {driver.current_url}"):
        assert language_selector.is_displayed()
        logging.debug(f"Language selector is visible on {driver.current_url}")


def navigate_through_links_with_keyboard(driver: WebDriver, page: ModuleType):
    selector = find_selector_by_name(page.SELECTORS, "language selector")
    language_selector = find_element(driver, selector, element_name="language selector")
    options = language_selector.find_elements_by_tag_name("option")
    for _ in options:
        language_selector.send_keys(Keys.DOWN)
    for _ in options:
        language_selector.send_keys(Keys.UP)
    with assertion_msg(f"Language selector is not visible on {driver.current_url}"):
        assert language_selector.is_displayed()


def change_to(
    driver: WebDriver, page: ModuleType, language: str, *, with_keyboard: bool = False
):
    page_name = f"{page.SERVICE} - {page.NAME}".lower()

    select = find_element(
        driver, LANGUAGE_SELECTOR, element_name="Language selector", wait_for_it=False
    )
    option = ELEMENTS_ON[page_name][language]
    logging.debug(f"Picking option {option} from dropdown list")
    logging.debug("Will select option: {}".format(option))
    option_value_selector = "option[value='{}']".format(option)
    option_element = select.find_element_by_css_selector(option_value_selector)
    if with_keyboard:
        option_element.send_keys(Keys.ENTER)
    else:
        option_element.click()


def check_page_language_is(driver: WebDriver, expected_language: str):
    expected_language_code = LANGUAGE_INDICATOR_VALUES[expected_language]
    language_selector = find_element(driver, LANGUAGE_SELECTOR)
    options = language_selector.find_elements_by_tag_name("option")
    selected = [option for option in options if option.is_selected()][0]
    with assertion_msg(
        "Expected to see page in '%s' but got '%s'",
        expected_language_code,
        selected.get_attribute("value"),
    ):
        assert selected.get_attribute("value") == expected_language_code
