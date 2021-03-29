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

NAME = "Travel Plan"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_TRAVEL_PLAN.absolute
PAGE_TITLE = "Travel Plan Page"

SELECTORS = {
    "travel plan": {
        "back": Selector(
            By.XPATH, "//body/div[7]/div/div/div/div[1]/a"
        ),
        "product cost educational": Selector(
            By.XPATH, "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tr[1]/td[1]/div/div/button/i"
        ),
        "travel plan": Selector(
            By.XPATH, "//input[@id='product_costs']", type=ElementType.INPUT
        ),
        "labour cost educational": Selector(
            By.XPATH, "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tr[2]/td[1]/div/div[1]/button/i"
        ),
        "labour cost": Selector(
            By.XPATH, "//input[@id='labour_costs']", type=ElementType.INPUT
        ),
        "additional margin": Selector(
            By.XPATH, "//input[@id='other_direct_costs']", type=ElementType.INPUT
        ),
        "direct costs total": Selector(
            By.XPATH, "//span[@class='body-l-b text-white']"
        ),
        "product adaptation educational": Selector(
            By.XPATH, "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[3]/table/tr[1]/td[1]/div/div/button/i",
            type=ElementType.INPUT
        ),
        "product adaptation": Selector(
            By.XPATH, "//input[@id='product_adaption']", type=ElementType.INPUT
        ),
        "freight and logistics educational": Selector(
            By.XPATH, "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[3]/table/tr[2]/td[1]/div/div/button/i"
        ),
        "freight and logistics": Selector(
            By.XPATH, "//input[@id='freight_logistics']"
        ),
        "agent and distributor fees educational": Selector(
            By.CSS_SELECTOR,
            "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[3]/table/tr[3]/td[1]/div/div[1]/button/i"
        ),
        "add route to market": Selector(
            By.CSS_SELECTOR, "#route-to-market > button"
        ),
        "marketing resources example": Selector(
            By.CSS_SELECTOR, "#resources > div > div.m-b-xs > button"
        ),
        "marketing resources text": Selector(
            By.XPATH, "//textarea[@id='resources']"
        ),
        "next": Selector(
            By.XPATH, "//p[contains(text(),'Next')]"
        ),
        "funding and credit": Selector(
            By.XPATH, "//span[contains(text(),'Funding and Credit')]"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#costs-and-pricing-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "sell direct to your customer link": Selector(
            By.CSS_SELECTOR,
            "#marketing-approach-content > section.container.m-b-l > div > div.c-1-4.m-t-s > div > a > div > p"
        ),
        "how to manage exchange rates": Selector(
            By.XPATH, "//h4[contains(text(),'How to manage exchange rates')]"
        ),
        "lesson": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > button"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav adaptation for your target market": Selector(
            By.XPATH, "//a[contains(text(),'Adaptation for your target market')]"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def enter_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    text_element.clear()
    text_element.send_keys("Automated tests")


def validate_entered_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    if "Automated tests" in text_element.text:
        return True
    return False


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
