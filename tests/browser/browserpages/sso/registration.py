# -*- coding: utf-8 -*-
"""SSO Registration Page Object."""
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Actor,
    Selector,
    check_for_sections,
    check_url,
    fill_out_input_fields,
    go_to_url,
    submit_form,
    tick_checkboxes,
)

NAME = "Registration"
SERVICE = Service.SSO
TYPE = PageType.FORM
URL = URLs.SSO_SIGNUP.absolute
PAGE_TITLE = "Register - great.gov.uk"

SELECTORS = {
    "form": {
        "title": Selector(By.CSS_SELECTOR, "#profile-register-intro > h1"),
        "email": Selector(By.ID, "id_email", type=ElementType.INPUT),
        "confirm email": Selector(By.ID, "id_email2", type=ElementType.INPUT),
        "password": Selector(By.ID, "id_password1", type=ElementType.INPUT),
        "confirm password": Selector(By.ID, "id_password2", type=ElementType.INPUT),
        "t&c": Selector(
            By.ID, "id_terms_agreed", is_visible=False, type=ElementType.CHECKBOX
        ),
        "sign up button": Selector(
            By.CSS_SELECTOR, "#signup_form > button", type=ElementType.SUBMIT
        ),
    }
}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.SSO_LOGGED_OUT)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def generate_form_details(actor: Actor, *, custom_details: dict = None) -> dict:
    result = {
        "email": actor.email,
        "confirm email": actor.email,
        "password": actor.password,
        "confirm password": actor.password,
        "t&c": True,
    }
    if custom_details:
        result.update(custom_details)
    return result


def fill_out(driver: WebDriver, contact_us_details: dict):
    form_selectors = SELECTORS["form"]
    fill_out_input_fields(driver, form_selectors, contact_us_details)
    tick_checkboxes(driver, form_selectors, contact_us_details)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
