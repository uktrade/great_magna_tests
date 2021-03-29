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

NAME = "Identify Opportunities"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_IDENTIFY_OPPORTUNITIES_AND_RESEARCH_THE_MARKET.absolute
PAGE_TITLE = "Identify Opportunities Page "

SELECTORS = {
    "identify opportunities": {
        "identify opportunities": Selector(
            By.XPATH, "//body/main[@id='content']/section[@id='learn-root']/section[1]/a[2]/article[1]"
        ),
        "is this opportunity right for you": Selector(
            By.XPATH, "//span[contains(text(),'Is this opportunity right for you?')]"
        ),
        "move from accidental exporting to strategic exporting": Selector(
            By.XPATH, "//span[contains(text(),'Move from accidental exporting to strategic export')]"
        ),
        "in market research": Selector(
            By.XPATH, "//span[contains(text(),'In-market research')]"
        ),
        "quantify customer demand": Selector(
            By.XPATH, "//span[contains(text(),'Quantify customer demand – how much might you sell')]"
        ),
        "module_progress": Selector(
            By.XPATH,
            "#learn-root > section.learn__single-category-header > div > div > div:nth-child(1) > div.learn__single-category-header-content > div.learn__category-progress-container"
        ),
        "lessons_progress_bar": Selector(
            By.XPATH, "//*[@id=\"55\"]/div/p"
        ),
        "lesson_categories_progress": Selector(
            By.CSS_SELECTOR,
            "4. #learn-root > section > a:nth-child(3) > article > div > div.learn__category-content.learn__category-content--progress-bar > div.learn__category-progress-container > div"
        ),
        "bottom back": Selector(
            By.CSS_SELECTOR, "#content > div > div.bg-blue-deep-80 > a > i"
        ),
        "top back": Selector(
            By.XPATH, "//*[@id=\"content\"]/div/a/i"
        ),
        "understand market barriers": Selector(
            By.XPATH, "//span[contains(text(),'Understand market barriers')]"
        ),
        "how to assess ease of entry into a new market": Selector(
            By.XPATH, "//span[contains(text(),'How to assess ease of entry into a new market')]"
        ),
        "local infrastructure": Selector(
            By.XPATH, "//span[contains(text(),'Local infrastructure')]"
        ),
        "understand how you may need to adapt your product": Selector(
            By.XPATH, "//span[contains(text(),'Understand how you may need to adapt your product ')]"
        ),
        "information you need to choose a target country": Selector(
            By.XPATH, "//span[contains(text(),'Information you need to choose a target country')]"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_progress_bar(driver: WebDriver, element_name: str):
    # search for parent progress bar div class
    parent_div_element = driver.find_element_by_class_name("learn__category-progress-container")
    # child_radio_div_elements = parent_div_radio_element.find_elements_by_tag_name("div")
    p_tag = parent_div_element.find_element_by_tag_name("p")
    logging.debug(p_tag.text)
    # get the child elements if any
    # check if progress bar exists
    # read the text from the progress bar

    #
    # find_and_click = find_element(
    #     driver, find_selector_by_name(SELECTORS, element_name)
    # )
    # find_and_click.click()
