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

NAME = "Compare Countries"
SERVICE = Service.WHERE_TO_EXPORT
TYPE = PageType.WHERE_TO_EXPORT
URL = URLs.GREAT_MAGNA_WHERE_TO_EXPORT.absolute
PAGE_TITLE = "Compare Countries"

SELECTORS = {
    "compare countries": {
        "product_input": Selector(
            By.CSS_SELECTOR, "#cta-container > button"
        ),
        "search": Selector(
            By.CSS_SELECTOR, "#search-input"
        ),
        "enter": Selector(
            By.XPATH, "//body/div[6]/div/div/form/div[2]/div/div/div[2]/button/i"
        ),
        "close": Selector(
            By.CSS_SELECTOR, "#dialog-close"
        ),
        "search again": Selector(
            By.CSS_SELECTOR, "#body > div:nth-child(15) > div > div > form > div.scroll-area > div > span > button > i"
        ),
        "next": Selector(
            By.XPATH, "//button[contains(text(),'Next')]"
        ),
        "save product": Selector(
            By.XPATH, "//button[contains(text(),'Save product')]"
        ),
        "add a place": Selector(
            By.CSS_SELECTOR, "#cta-container > button"
        ),
        "search country": Selector(
            By.CSS_SELECTOR, "#search-input"
        ),
        "delete": Selector(
            By.CSS_SELECTOR, "#market-India > th > button > i"
        ),
        "add a second place": Selector(
            By.CSS_SELECTOR, "#open-product-finder > span > div.table.market-details.m-h-m.bg-white.p-v-s.p-b-s.p-h-s.radius > button"
        ),
        "cpi educational": Selector(
            By.CSS_SELECTOR, "//body/main/div[3]/span/div[2]/span/table/thead/tr/th[6]/div/div/div/button/i"
        ),
        "adjusted national income": Selector(
            By.XPATH, "//*[@id=\"open-product-finder\"]/span/div[2]/span/table/thead/tr/th[4]/div/div/div/button/i"
        ),
        "adjusted national income educational": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/thead/tr/th[4]/div/div/div/button/i"
        ),
        "ease of doing business rank": Selector(
            By.XPATH, "//*[@id=\"open-product-finder\"]/span/div[2]/span/table/thead/tr/th[5]/div/div/div/button/i"
        ),
        "ease of doing business rank educational": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/thead/tr/th[5]/div/div/div/button/i"
        ),
        "corruption perception index": Selector(
            By.XPATH, "//*[@id=\"open-product-finder\"]/span/div[2]/span/table/thead/tr/th[6]/div/div/div/button/i"
        ),
        "where to export": Selector(
            By.XPATH, "#header-link-markets"
        ),
        "country 1": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[1]/th/div"
        ),
        "country 2": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[2]/th/div"
        ),
        "country 3": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[3]/th/div"
        ),
        "religion 1": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[1]/td[1]/div[1]"
        ),
        "religion 2": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[2]/td[1]/div[1]"
        ),
        "religion 3": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[3]/td[1]/div[1]"
        ),
        "language 1": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[3]/td[1]/div[1]"
        ),
        "language 2": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/tbody/tr[3]/td[1]/div[1]"
        ),
        "rule of law making educational": Selector(
            By.XPATH, "//body/main/div[3]/span/div[2]/span/table/thead/tr/th[4]/div/div/div/button/i"
        ),
        "country 1 bottom": Selector(
            By.XPATH, "//body/main/div[4]/div/section/div[2]/ul/li[1]/button"
        ),
        "country 2 bottom": Selector(
            By.XPATH, "//body/main/div[4]/div/section/div[2]/ul/li[2]/button"
        ),
        "country 3 bottom": Selector(
            By.XPATH, "//body/main/div[4]/div/section/div[2]/ul/li[3]/button"
        ),
    },
}
def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)

def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)

def check_lesson_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()

def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()

def where_to_export(driver: WebDriver, product_name: str):
    # logging.debug(f'product_name -> {product_name}')
    product_input = find_element(
        driver, find_selector_by_name(SELECTORS, "product name")
    )
    product_input.clear()
    product_input.send_keys(product_name)
    product_input(driver)