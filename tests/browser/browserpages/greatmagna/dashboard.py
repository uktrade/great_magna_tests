import logging
import random
import time
from types import ModuleType
from typing import List, Union
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.actions import action_builder

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

NAME = "Dashboard"
SERVICE = Service.GREATMAGNA
TYPE = PageType.DASHBOARD
URL = URLs.GREAT_MAGNA_DASHBOARD.absolute
PAGE_TITLE = "Dashboard Page "

SELECTORS = {
    "dashboard": {
        "learn to export": Selector(
            By.XPATH, "//a[@id='header-link-learning']"  # "//a[@id='header-link-learning']"
        ),
        "where to export": Selector(
            By.CSS_SELECTOR, "#header-link-markets"  # //a[@id='header-link-markets']"
        ),
        "build an export plan": Selector(
            By.XPATH, "//a[@id='header-link-exporting-plan']"  # "//a[@id='header-link-exporting-plan']"
        ),
        "sign out": Selector(
            By.XPATH, "//body/div[2]/div[1]/div[1]/ul[1]/li[6]/button[1]"  # //span[contains(text(),'Sign out')]
        ),
        "skipwalkthrough": Selector(
            By.XPATH, "//*[@id=\"page-tour-skip\"]"
        ),
        "avatar": Selector(
            By.CSS_SELECTOR, "#header-link-user-profile > div > button > img"
        ),
        "product-btn": Selector(
            By.CSS_SELECTOR, "#set-product-button > span > button"
        ),
        "country-btn": Selector(
            By.CSS_SELECTOR, "#set-country-button > span > button"
        ),
        "contact us": Selector(
            By.XPATH, "//a[contains(text(),'Contact us')]"
        ),

    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_and_click_change_link(driver: WebDriver, element_selector_name: str):
    change_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    change_link.click()


def should_see_following_sections(driver: WebDriver, names: List[str]):
    # desc = ["dashboard"]
    # check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
    #
    section = SELECTORS["dashboard"]
    names = [each_string.lower() for each_string in names]
    for key, selector in section.items():
        logging.debug(key)
        if key in names:
            element = find_element(
                driver,
                selector,
                element_name=key,
            )
            check_if_element_is_visible(element, element_name=key)


def click_skip_walk_through(driver: WebDriver):
    skip_link = find_element(
        driver, find_selector_by_name(SELECTORS, "skipwalkthrough")
    )
    skip_link.click()


def click_signout(driver: WebDriver):
    signout_link = find_element(
        driver, find_selector_by_name(SELECTORS, "sign out")
    )
    signout_link.click()


def click_avatar(driver: WebDriver):
    avatar_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "avatar")
    )
    avatar_btn.click()


def find_and_select_random_radio_and_click_next(driver: WebDriver):
    parent_div_radio_element = driver.find_element_by_class_name("m-b-xs")
    time.sleep(2)
    child_radio_div_elements = parent_div_radio_element.find_elements_by_xpath("//input[@type='radio']");
    RADIO_SELECTORS_DICT = {}
    for index in range(len(child_radio_div_elements)):
        child_radio_element = child_radio_div_elements[index]
        key_name = "radio" + str(index)
        radio_element_xpath = f"//input[@id='" + str(child_radio_element.get_attribute("id")) + "']"
        key_value = Selector(By.XPATH, radio_element_xpath, type=ElementType.RADIO)

        if index == 0:
            rsdict = {}
            rsdict[key_name] = key_value
            RADIO_SELECTORS_DICT["product radio info"] = rsdict
        else:
            rsdict = RADIO_SELECTORS_DICT["product radio info"]
            rsdict[key_name] = key_value
            RADIO_SELECTORS_DICT.clear()
            RADIO_SELECTORS_DICT["product radio info"] = rsdict

    radio_selectors = RADIO_SELECTORS_DICT["product radio info"]
    check_random_radio(driver, radio_selectors)

    nextbtnclick(driver)


def nextbtnclick(driver: WebDriver):
    driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()


def fill_out_product(driver: WebDriver, products: str):
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "product-btn")
    )
    product_btn.click()

    try:
        if driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").is_displayed():
            driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").click()
    except:
        pass

    try:
        # time.sleep(2)
        # driver.find_element_by_xpath("/html/body/div[3]/div/div/form/div[2]/div/div/section/div/div[2]/label/div[2]/div/i").click()
        # driver.find_element_by_xpath(
        #     "/html/body/div[3]/div/div/form/div[2]/div/div/section/div/div[2]/label/div[2]/div/i").click()

        # driver.find_element_by_xpath(
        #     "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").sendKeys(Keys.CONTROL + "a");
        # driver.find_element_by_xpath(
        #     "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys(u'\ue009' + u'\ue003')
        # driver.find_element_by_xpath(
        #     "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").sendKeys(Keys.DELETE);
        # time.sleep(2)
        # driver.find_element_by_xpath(
        #     "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").clear()
        product_input_text = driver.find_element_by_xpath("//input[@id='input-commodity-name']").text
        logging.debug("product_input_text -> " + product_input_text)
        # actions = action_chains(driver)
        # driver.find_element_by_xpath("//input[@id='input-commodity-name']").click()
        # for i in range(len(product_input_text)):
        #     actions.sendKeys(Keys.ARROW_LEFT)
        #
        # actions.build().perform()
        #
        # for i in range(len(product_input_text)):
        #     actions.sendKeys(Keys.DELETE)
        #
        # time.sleep(1);
        # actions.build().perform()

        for i in range(len(product_input_text)):
            driver.find_element_by_xpath(
                "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").sendKeys(
                Keys.BACKSPACE)
        driver.find_element_by_xpath(
            "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("")
        driver.find_element_by_xpath(
            "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys(products)
        driver.find_element_by_xpath(
            "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/button[1]/i[1]").click()

        while True:
            find_and_select_random_radio_and_click_next(driver)
            time.sleep(1)  # seconds
            try:
                if driver.find_element_by_xpath("//button[contains(text(),'Save product')]").is_displayed():
                    driver.find_element_by_xpath("//button[contains(text(),'Save product')]").click()
                    break
                else:
                    continue
            except:
                pass
    except Exception as ex:
        logging.debug("Exception in product input " + str(ex))
        driver.find_element_by_css_selector("#input-commodity-name").send_keys(products)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/form/div[2]/div/div/section/div/button").click()


def fill_out_country(driver: WebDriver, country: str):
    try:
        time.sleep(1)
        skip_link = find_element(
            driver, find_selector_by_name(SELECTORS, "skipwalkthrough")
        )
        skip_link.click()
    except:
        pass

    try:
        time.sleep(1)
        if driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").is_displayed():
            driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").click()
    except:
        pass

    try:
        if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
            driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
    except:
        pass

    # country
    time.sleep(1)
    country_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "country-btn")
    )
    country_btn.click()
    try:
        time.sleep(1)
        if driver.find_element_by_css_selector("body > div:nth-child(14) > div > div > button").is_displayed():
            driver.find_element_by_css_selector("body > div:nth-child(14) > div > div > button").click()
    except:
        pass

    time.sleep(1)
    if 0 == len(country):
        path_random_country_element = "body > div:nth-child(13) > div > div > div > div > div > div.only-desktop > div.suggested-markets > ul > button:nth-child(" + str(
            random.randint(1, 5)) + ")"
        driver.find_element_by_css_selector(path_random_country_element).click()
    else:
        try:
            if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
                driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
        except:
            pass
        driver.find_element_by_css_selector("#search-input").clear()
        driver.find_element_by_css_selector("#search-input").send_keys(country)

        buttons_elements = driver.find_elements_by_tag_name("button")
        # logging.debug(buttons_elements)
        for button_element in buttons_elements:
            # logging.debug(button_element.text)
            if button_element.text == country.lower():
                button_element.click()
                # time.sleep(5)
                break
        # country_name_btn_xpath = "//button[contains(text(),'"+ country + "')]"
        # driver.find_element_by_xpath(country_name_btn_xpath).click()
    # try:
    #     time.sleep(1)
    #     driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()
    # except:
    #     pass


def fill_out_products_and_country(driver: WebDriver, products: str, country: str):
    fill_out_product(driver, products)

    fill_out_country(driver, country)

def fill_out_products(driver: WebDriver, products: str):
    fill_out_input_fields(driver, products)
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "#search-input")
    )
    product_btn.click()
