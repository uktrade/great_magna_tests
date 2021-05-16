# -*- coding: utf-8 -*-
"""Domestic - Feedback Contact us form thank you page"""
import logging
from types import ModuleType
from typing import Union
from uuid import uuid4

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
    fill_out_textarea_fields,
    go_to_url,
    submit_form,
    tick_captcha_checkbox,
    tick_checkboxes,
)

NAME = "Thank you for your feedback"
SERVICE = Service.DOMESTIC
TYPE = PageType.CONTACT_US
URL = URLs.CONTACT_US_FEEDBACK_SUCCESS.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

SELECTORS = {
    "form": {
        "itself": Selector(By.CSS_SELECTOR, "#lede form"),
        "full name": Selector(By.ID, "id_name", type=ElementType.INPUT),
        "email": Selector(By.ID, "id_email", type=ElementType.INPUT),
        "feedback": Selector(By.ID, "id_comment", type=ElementType.TEXTAREA),
        "terms and conditions": Selector(
            By.ID, "id_terms_agreed", type=ElementType.CHECKBOX
        ),
        "submit": Selector(
            By.CSS_SELECTOR, "div.exred-triage-form button", type=ElementType.SUBMIT
        ),
    }
}
OTHER_SELECTORS = {
    "other": Selector(By.ID, "id_company_type_other", type=ElementType.SELECT)
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver, *, page_name: str = None):
    check_url(driver, URL, exact_match=True)


def generate_form_details(actor: Actor) -> dict:
    result = {
        "full name": str(uuid4()),
        "email": actor.email,
        "feedback": f"Feedback submitted by automated tests {actor.alias}",
        "terms and conditions": True,
    }
    logging.debug(f"Generated form details: {result}")
    return result


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["form"]
    fill_out_input_fields(driver, form_selectors, details)
    fill_out_textarea_fields(driver, form_selectors, details)
    tick_checkboxes(driver, form_selectors, details)
    tick_captcha_checkbox(driver)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])
