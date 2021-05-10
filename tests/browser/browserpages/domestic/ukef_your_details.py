# -*- coding: utf-8 -*-
"""Domestic UKEF Contact Us - Page Object."""
import logging
from types import ModuleType
from typing import List, Union
from uuid import uuid4

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType
from browserpages.common_actions import (
    Actor,
    Selector,
    check_for_sections,
    check_url,
    fill_out_input_fields,
    go_to_url,
    submit_form,
)

NAME = "Your details"
SERVICE = Service.DOMESTIC
TYPE = PageType.UKEF_CONTACT_US
URL = URLs.DOMESTIC_GET_FINANCE_YOUR_DETAILS.absolute
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
        "first name": Selector(
            By.ID, "id_your-details-firstname", type=ElementType.INPUT
        ),
        "last name": Selector(
            By.ID, "id_your-details-lastname", type=ElementType.INPUT
        ),
        "position": Selector(By.ID, "id_your-details-position", type=ElementType.INPUT),
        "email": Selector(By.ID, "id_your-details-email", type=ElementType.INPUT),
        "phone": Selector(By.ID, "id_your-details-phone", type=ElementType.INPUT),
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


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def generate_form_details(actor: Actor) -> dict:
    result = {
        "first name": actor.alias,
        "last name": str(uuid4()),
        "position": "automated tests",
        "email": actor.email,
        "phone": "automated tests",
    }
    return result


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["form"]
    fill_out_input_fields(driver, form_selectors, details)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])
