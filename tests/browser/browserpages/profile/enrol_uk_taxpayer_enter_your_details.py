# -*- coding: utf-8 -*-
"""Profile - Enrol - UK taxpayer - Enter your details"""
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
from browserpages.profile import enrol_account_created

NAME = "Enter your details (UK taxpayer)"
SERVICE = Service.PROFILE
TYPE = PageType.FORM
URL = URLs.PROFILE_ENROL_INDIVIDUAL_ENTER_YOUR_PERSONAL_DETAILS.absolute
PAGE_TITLE = ""

SELECTORS = {
    "enrolment progress bar": {"itself": Selector(By.ID, "progress-column")},
    "your business type": {
        "information box": Selector(By.ID, "business-type-information-box"),
        "change business type": Selector(By.ID, "change-business-type"),
    },
    "enter your details": {
        "itself": Selector(By.CSS_SELECTOR, "section form"),
        "heading": Selector(By.CSS_SELECTOR, "h1"),
        "first name": Selector(
            By.ID, "id_personal-details-given_name", type=ElementType.INPUT
        ),
        "last name": Selector(
            By.ID, "id_personal-details-family_name", type=ElementType.INPUT
        ),
        "job title": Selector(
            By.ID, "id_personal-details-job_title", type=ElementType.INPUT
        ),
        "phone number": Selector(
            By.ID, "id_personal-details-phone_number", type=ElementType.INPUT
        ),
        "submit": Selector(
            By.CSS_SELECTOR,
            "form button.button",
            type=ElementType.SUBMIT,
            next_page=enrol_account_created,
        ),
    },
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
    msg = f"Got 404 on {driver.current_url}"
    assert "This page cannot be found" not in driver.page_source, msg


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def generate_form_details(actor: Actor) -> dict:
    result = {
        "first name": actor.alias,
        "last name": str(uuid4()),
        "job title": "DIT AUTOMATED TESTS",
        "phone number": "07123456789",
    }
    logging.debug(f"Generated form details: {result}")
    return result


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["enter your details"]
    fill_out_input_fields(driver, form_selectors, details)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["enter your details"])
