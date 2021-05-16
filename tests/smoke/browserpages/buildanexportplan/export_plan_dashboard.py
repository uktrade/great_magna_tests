import logging
import random
import time
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from great_magna_tests_shared.utils import check_url_path_matches_template
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_url,
    find_element,
    find_selector_by_name,
    find_elements,
    go_to_url,
    pick_option,
    is_element_present,
    submit_form,
    check_random_radio,
    take_screenshot,
    wait_for_page_load_after_action,
    fill_out_input_fields,
    fill_out_email_address
)

NAME = "Export Plan Dashboard"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_DASHBOARD.absolute
PAGE_TITLE = "Export Plan Dashboard"

SELECTORS = {
    "Export Plan Dashboard": {
        "about your business": Selector(
            By.XPATH, "//*[@id=\"export-plan-dashboard\"]/div[1]/div/a/div[2]/h3"
        ),
        "business objectives": Selector(
            By.CSS_SELECTOR, "#export-plan-dashboard > div:nth-child(2) > div > a > div.p-t-s.p-b-xs.p-h-xs"
        ),
        "target markets research": Selector(
            By.XPATH, "//*[@id=\"export-plan-dashboard\"]/div[3]/div/a/div[2]"
        ),
        "Adapting Your Product": Selector(
            By.XPATH, "//h3[contains(text(),'Adapting Your Product')]"
        ),
        "marketing approach": Selector(
            By.XPATH, "//h3[contains(text(),'Marketing approach')]"
        ),
        "costs and pricing": Selector(
            By.XPATH, "//h3[contains(text(),'Costs and pricing')]"
        ),
        "funding and credit": Selector(
            By.CSS_SELECTOR, "#export-plan-dashboard > div:nth-child(7) > div > a > div.p-v-s.p-h-xs > h3"
        ),
        "getting paid": Selector(
            By.XPATH, "//*[@id=\"export-plan-dashboard\"]/div[8]/div/a"
        ),
        "travel plan": Selector(
            By.CSS_SELECTOR, "#export-plan-dashboard > div:nth-child(9) > div > a > div.p-t-s.p-b-xs.p-h-xs"
        ),
        "business risk": Selector(
            By.CSS_SELECTOR,
            "#export-plan-dashboard > div:nth-child(10) > div > div > div.bg-blue-deep-20.section-list__image-container > img"
        ),
        "upload logo": Selector(
            By.XPATH, "//h3[contains(text(),'Upload your logo')]"
        ),
        "save your plan as pdf": Selector(
            By.XPATH, "//span[contains(text(),'Save your plan as a PDF')]"
        ),
        "ok button": Selector(
            By.CSS_SELECTOR,
            "body > div:nth-child(18) > div > div > div > div.modal-inner.text-blue-deep-80.bg-white.radius-bottom-s > div > button"
        ),
        "back": Selector(
            By.CSS_SELECTOR,
            "body > div:nth-child(18) > div > div > div > div.modal-header.modal-header-bg.modal-header-bg--3.radius-top-s.bg-blue-deep-80.p-s > a"
        ),

    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
