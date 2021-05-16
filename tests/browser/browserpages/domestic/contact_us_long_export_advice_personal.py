# -*- coding: utf-8 -*-
"""Domestic - First page of Long Contact us form"""
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
    go_to_url,
    submit_form,
)
from browserpages.domestic import contact_us_long_export_advice_business

NAME = "Long (Personal details)"
SERVICE = Service.DOMESTIC
TYPE = PageType.CONTACT_US
URL = URLs.CONTACT_US_EXPORT_ADVICE_PERSONAL.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

SELECTORS = {
    "form": {
        "itself": Selector(By.CSS_SELECTOR, "#lede form"),
        "first name": Selector(By.ID, "id_personal-first_name", type=ElementType.INPUT),
        "last name": Selector(By.ID, "id_personal-last_name", type=ElementType.INPUT),
        "position": Selector(By.ID, "id_personal-position", type=ElementType.INPUT),
        "email": Selector(By.ID, "id_personal-email", type=ElementType.INPUT),
        "phone": Selector(By.ID, "id_personal-phone", type=ElementType.INPUT),
        "submit": Selector(
            By.CSS_SELECTOR,
            "div.exred-triage-form button",
            type=ElementType.SUBMIT,
            next_page=contact_us_long_export_advice_business,
        ),
    }
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)


def generate_form_details(actor: Actor) -> dict:
    result = {
        "first name": f"send by {actor.alias} - automated tests",
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
