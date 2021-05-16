# -*- coding: utf-8 -*-
"""Domestic UKEF Contact Us - Page Object."""
import logging
from types import ModuleType
from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType
from browserpages.common_actions import (
    Actor,
    Selector,
    check_url,
    fill_out_input_fields,
    go_to_url,
    pick_option,
    submit_form,
    tick_checkboxes,
)

NAME = "Company details"
SERVICE = Service.DOMESTIC
TYPE = PageType.UKEF_CONTACT_US
URL = URLs.CONTACT_US_FORM_GET_FINANCE_COMPANY_DETAILS.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

SELECTORS = {
    "breadcrumbs": {
        "itself": Selector(By.CSS_SELECTOR, "nav.breadcrumbs"),
        "current page": Selector(
            By.CSS_SELECTOR, "nav.breadcrumbs li[aria-current='page']"
        ),
        "links": Selector(By.CSS_SELECTOR, "nav.breadcrumbs a"),
    },
    "form": {
        "itself": Selector(By.CSS_SELECTOR, "#content form"),
        "heading": Selector(By.CSS_SELECTOR, "#heading-container h1"),
        "registered name": Selector(
            By.ID, "id_company-details-trading_name", type=ElementType.INPUT
        ),
        "building and street first line": Selector(
            By.ID, "id_company-details-address_line_one", type=ElementType.INPUT
        ),
        "building and street second line": Selector(
            By.ID, "id_company-details-address_line_two", type=ElementType.INPUT
        ),
        "town or city": Selector(
            By.ID, "id_company-details-address_town_city", type=ElementType.INPUT
        ),
        "county": Selector(
            By.ID, "id_company-details-address_county", type=ElementType.INPUT
        ),
        "postcode": Selector(
            By.ID, "id_company-details-address_post_code", type=ElementType.INPUT
        ),
        "industry": Selector(
            By.ID, "id_company-details-industry", type=ElementType.SELECT
        ),
        "i have three years of registered accounts": Selector(
            By.ID,
            "checkbox-multiple-i-have-three-years-of-registered-accounts",
            type=ElementType.CHECKBOX,
            is_visible=False,
        ),
        "i have customers outside the uk": Selector(
            By.ID,
            "checkbox-multiple-i-have-customers-outside-uk",
            type=ElementType.CHECKBOX,
            is_visible=False,
        ),
        "i supply uk companies that sell overseas": Selector(
            By.ID,
            "checkbox-multiple-i-supply-companies-that-sell-overseas",
            type=ElementType.CHECKBOX,
            is_visible=False,
        ),
        "continue": Selector(
            By.CSS_SELECTOR, "#content form button", type=ElementType.SUBMIT
        ),
    },
    "error reporting": {
        "itself": Selector(By.CSS_SELECTOR, "section.error-reporting"),
        "link": Selector(By.ID, "error-reporting-section-contact-us"),
    },
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=True)
    logging.debug("All expected elements are visible on '%s' page", NAME)


def generate_form_details(actor: Actor, *, custom_details: dict = None) -> dict:
    result = {
        "registered name": "automated tests",
        "building and street first line": "automated tests",
        "building and street second line": "automated tests",
        "town or city": "automated tests",
        "county": "automated tests",
        "postcode": "automated tests",
        "industry": None,
        "i have three years of registered accounts": True,
        "i have customers outside the uk": True,
        "i supply uk companies that sell overseas": True,
    }
    if custom_details:
        result.update(custom_details)
    return result


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["form"]
    fill_out_input_fields(driver, form_selectors, details)
    tick_checkboxes(driver, form_selectors, details)
    pick_option(driver, form_selectors, details)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])
