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
    fill_out_email_address,
    fill_out_textarea_fields,
)

NAME = "Getting Paid"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_GETTING_PAID.absolute
PAGE_TITLE = "Getting Paid Page"

SELECTORS = {
    "getting paid": {
        "payment methods": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(1) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        ),
        "payment methods notes": Selector(
            By.CSS_SELECTOR, "#method_notes", type=ElementType.INPUT
        ),
        "payment terms": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(2) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        ),
        "payment terms notes": Selector(
            By.CSS_SELECTOR, "#payments_notes", type=ElementType.INPUT
        ),
        "incoterms": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(3) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        ),
        "incoterms notes": Selector(
            By.CSS_SELECTOR, "#incoterms_notes", type=ElementType.INPUT
        ),
        "section complete": Selector(
            By.XPATH, "//label[contains(text(),'Yes')]"
        ),
        "travel plan": Selector(
            By.XPATH, "//*[@id=\"getting-paid-content\"]/section[4]/div/div/div[2]/a/span"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#costs-and-pricing-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav travel plan": Selector(
            By.XPATH, "//*[@id=\"collapseNav\"]/div/ul/li[9]/a"
        ),
        "back": Selector(
            By.XPATH, "//body/div[10]/div/div/div/div[1]/a"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "top export plan home": Selector(
            By.XPATH, "//*[@id=\"getting-paid-content\"]/section[1]/div/div/div[2]/a/span"
        ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div > label"
        ),
        "dashboard": Selector(
            By.XPATH, "//a[contains(text(),'Dashboard')]"
        ),"choose the right payment method": Selector(
            By.XPATH,
            "//h4[contains(text(),'Choose the right payment method')]"
        ),
        "decide when to get paid": Selector(
            By.XPATH,
            "//h4[contains(text(),'Decide when to get paid')]"
        ),
        "choose which incoterms are right for you": Selector(
            By.XPATH,
            "//h4[contains(text(),'Choose which incoterms are right for you')]"
        ),
        "incoterms lesson": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(3) > div.select.m-b-l > div > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "payment terms lesson": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(2) > div.select.m-b-l > div > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "payment methods lesson": Selector(
            By.XPATH,
            "//*[@id=\"getting-paid\"]/div/div[1]/div[1]/div/div[1]/div[1]/button"
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


def enter_business_objectives_details(driver: WebDriver, startdate: str, enddate: str, objectives: str, owner: str,
                                      plannedreviews: str):
    input_field_selectors = SELECTORS["business objectives"]
    input_details_dict = {"start date": startdate, "end date": enddate, "owner": owner}
    fill_out_input_fields(driver, input_field_selectors, input_details_dict)

    text_area_details_dict = {"objective text": objectives, "planned review": plannedreviews}
    fill_out_textarea_fields(driver, input_field_selectors, text_area_details_dict)
    time.sleep(1)


def find_and_select_random_item_list(driver: WebDriver, element_selector_name: str):
    payment_methods_btn = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(1) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > div.select__placeholder--input")
    payment_methods_btn.click()
    payment_terms_btn = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(2) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > div.select__placeholder--input")
    payment_terms_btn.click()
    incoterms_btn = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(3) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > div.select__placeholder--input")
    incoterms_btn.click()
    driver.implicitly_wait(5)
    # select__list body-l bg-white radius
    payment_methods_element = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(1) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > ul")
    payment_terms_element = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(2) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > ul")
    incoterms_element = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(3) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > ul")

    li_elements = payment_methods_element.find_elements_by_tag_name("li")
    li_elements = payment_terms_element.find_elements_by_tag_name("li")
    li_elements = incoterms_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)

def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()

def fill_out_country(driver: WebDriver, country: str):
    driver.implicitly_wait(1)
    # parent div: //body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]
    # parent ul: //body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul

    # where to export : country search
    # //body/div[8]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]
    # //body/div[8]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/ul

    # country
    # country_btn = find_element(
    #     driver, find_selector_by_name(SELECTORS, "country-btn")  # dashboard add country button
    # )
    # country_btn.click()

    # try:
    #     if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
    #         driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
    # except:
    #     pass
    driver.find_element_by_xpath("//button[contains(text(),'Add a target market')]").click()
    if 0 == len(country):
        # if country name is not provided from the test case, then select one of the random 5 countries listed on the browser
        path_random_country_element = "body > div:nth-child(13) > div > div > div > div > div > div.only-desktop > div.suggested-markets > ul > button:nth-child(" + str(
            random.randint(1, 5)) + ")"
        driver.find_element_by_css_selector(path_random_country_element).click()
    else:
        # search using the provide country name from the test case
        driver.find_element_by_css_selector("#search-input").clear()
        driver.find_element_by_css_selector("#search-input").send_keys(country)

        # look out for the list displayed after entering country name and select random/provided country
        ul_list_element = driver.find_element_by_xpath(
            "/html/body/div[11]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul")
#            "//body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul")

        section_elements = ul_list_element.find_elements_by_tag_name("section")
        logging.debug("length of section elements " + str(len(section_elements)))
        # select random section element and within that select a country
        index_random_element_to_be_selected = random.randint(0, len(section_elements) - 1)
        logging.debug("Index of section elements " + str(index_random_element_to_be_selected))
        section_element_selected = section_elements[index_random_element_to_be_selected]
        logging.debug(section_element_selected)

        div_elements = section_element_selected.find_elements_by_tag_name("div")  # 2 has to be present
        logging.debug("length of div elements " + str(len(div_elements)))
        level_1_div_element = div_elements[
            1]  # section_element_selected.find_element_by_class_name("p-t-s expand-section open")
        level_2_div_element = level_1_div_element.find_element_by_tag_name("div")
        span_elements = level_2_div_element.find_elements_by_tag_name("span")
        logging.debug("length of span elements " + str(len(span_elements)))
        # select random span element and within that select a country
        index_random_element_to_be_selected = random.randint(0, len(span_elements) - 1)
        span_element_selected = span_elements[index_random_element_to_be_selected]
        li_element = span_element_selected.find_element_by_tag_name("li")
        # finally arrived at country name button(s)
        buttons_elements = li_element.find_elements_by_tag_name("button")
        logging.debug("length of country button elements " + str(len(buttons_elements)))
        country_name_found = False
        for button_element in buttons_elements:
            if str(button_element.text).lower() == country.lower():
                country_name_found = True
                button_element.click()
                break
        if country_name_found == False:
            raise Exception("Country name could not be found " + str(country))


# def fill_out_products_and_country(driver: WebDriver, products: str, country: str):
#     fill_out_product(driver, products)
#
#     fill_out_country(driver, country)
