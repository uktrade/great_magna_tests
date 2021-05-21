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

NAME = "search"
SERVICE = Service.GREATMAGNA
TYPE = PageType.SEARCH
URL = URLs.GREAT_MAGNA_SEARCH.absolute
PAGE_TITLE = "Search Page"

SELECTORS = {
    "search": {
        "select_product": Selector(
            By.CSS_SELECTOR, "#cta-container > button"
        ),
        "product-btn": Selector(
            By.CSS_SELECTOR, "#set-product-button > span > button"
        ),
        "search next button": Selector(
            By.XPATH, "//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/div/div/button"
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
            By.XPATH, "//body/div[7]/div/div/form/div[2]/div/span/div/section[1]/div[2]/button"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def fill_out_products_and_country(driver: WebDriver, products: str, country: str):
    fill_out_input_fields(driver, products, country)


def fill_out_products(driver: WebDriver, products: str):
    fill_out_input_fields(driver, products)

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
    select_product_search_again_top_bottom(driver, product_name=product_name)


def search_again_top_bottom(driver: WebDriver):
    try:
        search_again_top_btn = find_element(
            driver, find_selector_by_name(SELECTORS, "top search again")
        )
        search_again_top_btn.click()
    except:
        try:
            search_again_btm_btn = find_element(
                driver, find_selector_by_name(SELECTORS, "bottom search again")
            )
            search_again_btm_btn.click()
        except:
            pass


def select_product_search_again_top_bottom(driver: WebDriver, product_name: str):
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "product-btn")
    )
    product_btn.click()
    search_again_top_bottom(driver)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/label/div/input").clear()
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/label/div/input").send_keys(
        product_name)
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/button").click()


def search_select_save_random_next(driver: WebDriver):
    counter = 0
    while True:

        if counter >= 50:
            break
        # logging.debug("Counter: " + str(counter))

        driver.implicitly_wait(1)

        # check for save button
        save_btn_found = False
        try:
            save_product_btn = driver.find_element_by_xpath(
                "//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/div[2]/button")
            save_btn_found = True
        except Exception as ex:
            logging.debug("save button not found.Exception: " + str(ex))

        if save_btn_found == True:
            logging.debug("Save button found")
            save_product_btn.click()
            return
        # look for div's and radio buttons
        # try:
        parent_1_div_element = driver.find_element_by_xpath(
            "//body/div[4]/div/div/form/div[2]/div/span/div/section/div")
        #      #   "/html/body/div[7]/div/div/form/div[2]/div/span/div/section/div")  # ("interaction grid m-v-xs")
        # except Exception as e:
        #     parent_1_div_element = driver.find_element_by_xpath("//body/div[7]/div[1]/div[1]/form[1]/div[2]/div[1]/span[1]/div[1]/section[1]/div[1]")#"interaction grid m-v-xs")
        child_1_div_element = parent_1_div_element.find_element_by_tag_name("div")  # ("c-fullwidth")
        main_div_element = child_1_div_element.find_element_by_tag_name("div")
        # radio button labels
        label_elements = main_div_element.find_elements_by_tag_name("label")
        radio_elements = []
        for label_element in label_elements:
            radio_ele = None
            try:
                radio_ele = label_element.find_element_by_tag_name("input")
            except Exception as e:
                continue
            radio_elements.append(radio_ele)
        logging.debug('number of labels - ' + str(len(radio_elements)))
        random_label_index = random.randint(0, len(radio_elements) - 1)
        logging.debug('Index of radio buttons to be selected -> ' + str(random_label_index))

        radio_btn_selected = radio_elements[random_label_index]
        radio_btn_selected.click()

        driver.implicitly_wait(1)
        search_next_btn = find_element(
            driver, find_selector_by_name(SELECTORS, "search next button")
        )
        search_next_btn.click()

        counter += 1


def fill_out_country(driver: WebDriver, country: str):
    # search using the provide country name from the test case
    driver.find_element_by_css_selector("#search-input").clear()
    driver.find_element_by_css_selector("#search-input").send_keys(country)

    # look out for the list displayed after entering country name and select random/provided country
    ul_list_element = driver.find_element_by_xpath(
        "//body/div[8]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/ul")

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


def fill_out_country_and_validate_ui(driver: WebDriver, country: str, display_tab_count: int = 5):
    # fill out country name
    fill_out_country(driver, country)

    # after entering the country name, check if there are required tabs displayed on the UI
    tabs_element = driver.find_element_by_xpath("//body/main/div[3]/span/div[1]/div/ol")
    tab_button_elements = tabs_element.find_elements_by_tag_name("button")
    logging.debug(tab_button_elements)
    logging.debug(len(tab_button_elements))
    if len(tab_button_elements) != display_tab_count:
        raise Exception("Invalid Tab count")


def enter_country_details(driver: WebDriver, country_name: str, country_place_number: int = 1
                          , country_max: int = 10
                          , display_tab_count: int = 5):
    driver.implicitly_wait(1)
    # logging.debug("country_place_number " + str(country_place_number))
    # logging.debug("country_max " + str(country_max))
    # logging.debug("display_tab_count " + str(display_tab_count))
    table_element = None
    try:
        # check if the country table already exists
        # table_element = driver.find_element_by_xpath("/html/body/main/div[3]/span/div[2]/span/table")
        # if table doesnt not exists then "add a place" button must exists
        # if table_element == None:
        if (country_place_number == 1):
            find_and_click(driver, element_selector_name="add a place")
    except Exception as e:
        table_element = None
        find_and_click(driver, element_selector_name="add a place")

    # logging.debug("table_element " + str(table_element))

    if (country_place_number == 1):  # and table_element == None):
        fill_out_country_and_validate_ui(driver, country_name, display_tab_count=display_tab_count)
        return

    if country_place_number <= country_max:
        # if table already exists, then "add place (x) of (y)" button must exists
        add_place_num_btn_element = driver.find_element_by_xpath("//body/main/div[3]/span/div[2]/button")
        button_text = add_place_num_btn_element.text
        user_entered_button_text = "Add place " + str(country_place_number) + " of " + str(country_max)
        if button_text != user_entered_button_text:
            raise Exception(
                "Invalid Add Place button index - " + str(button_text) + " vs " + str(user_entered_button_text))

        # if proper button index found, then click the button to add the country place name
        add_place_num_btn_element.click()

        fill_out_country_and_validate_ui(driver, country_name, display_tab_count=display_tab_count)
        time.sleep(2)
    else:
        logging.debug(
            "Country " + str(country_name) + " cannot be added as the CountryPlaceNumber exceeding max limit.")


def delete_all_country_details(driver: WebDriver, position: str):
    country_details_div_element_xpath = "//body/main/div[3]/span/div[2]/span/table/tbody/tr" + "[" + position + "]"
    del_btn_ele_xpath = country_details_div_element_xpath + "/th/div/button/i"

    driver.find_element_by_xpath(del_btn_ele_xpath).click()
    time.sleep(1)


def check_country_details(driver: WebDriver, on_all_tabs: bool = False):
    driver.implicitly_wait(1)
    country_details_table_element = driver.find_element_by_xpath("//body/main/div[3]/span/div[2]/span/table/tbody")
    if on_all_tabs == False:
        tr_elements = country_details_table_element.find_elements_by_tag_name("tr")

        data_not_available_countries = {}
        for tr_element in tr_elements:
            th_element = tr_element.find_element_by_xpath("th")
            td_elements = tr_element.find_elements_by_tag_name("td")
            # country name
            country_tag_element = th_element.find_element_by_xpath("div")
            country_name = country_tag_element.find_element_by_xpath("div").text
            # items in the table : Total Population, .....
            for td_element in td_elements:
                if "Data not available" in str(td_element.text).strip():
                    if country_name not in data_not_available_countries:
                        data_not_available_countries[country_name] = "Data not available"

        if len(data_not_available_countries) != 0:
            raise Exception("Country missing details " + str(data_not_available_countries))
    else:
        country_tab_elements = driver.find_element_by_xpath("//body/main/div[3]/span/div[1]/div/ol")
        tab_elements = country_tab_elements.find_elements_by_tag_name("button")

        data_not_available_tabs = {}

        for tab_element in tab_elements:
            tab_element.click()
            country_details_table_element = driver.find_element_by_xpath(
                "//body/main/div[3]/span/div[2]/span/table/tbody")
            tr_elements = country_details_table_element.find_elements_by_tag_name("tr")
            data_not_available_countries = {}
            for tr_element in tr_elements:
                th_element = tr_element.find_element_by_xpath("th")
                td_elements = tr_element.find_elements_by_tag_name("td")
                # country name
                country_tag_element = th_element.find_element_by_xpath("div")
                country_name = country_tag_element.find_element_by_xpath("div").text

                # items in the table : Total Population, .....
                for td_element in td_elements:
                    if "Data not available" in str(td_element.text).strip():
                        if country_name not in data_not_available_countries:
                            data_not_available_countries[country_name] = "Data not available"

            tab_name = tab_element.text
            if len(data_not_available_countries) != 0:
                data_not_available_tabs[tab_name] = data_not_available_countries

        if len(data_not_available_tabs) != 0:
            raise Exception("Country missing details " + str(data_not_available_tabs))


def validate_entered_country_details(driver: WebDriver, country_name: str, country_place_number: int = 1
                                     , country_max: int = 10
                                     , list_selection: int = 10):
    driver.implicitly_wait(1)

    table_element = None
    try:
        # check if the country table already exists
        table_element = driver.find_element_by_xpath("/html/body/main/div[3]/span/div[2]/span/table")
        # if table doesnt not exists then "add a place" button must exists
        if table_element == None:
            find_and_click(driver, element_selector_name="add a place")
    except Exception as e:
        table_element = None
        find_and_click(driver, element_selector_name="add a place")

    logging.debug("table_element " + str(table_element))

    if (country_place_number == 1 and table_element == None):
        fill_out_country_and_validate_ui(driver, country_name, list_selection=list_selection)
        return

    if country_place_number <= country_max:
        # if table already exists, then "add place (x) of (y)" button must exists
        add_place_num_btn_element = driver.find_element_by_xpath("//body/main/div[3]/span/div[2]/button")
        button_text = add_place_num_btn_element.text
        user_entered_button_text = "Add place " + str(country_place_number) + " of " + str(country_max)
        if button_text != user_entered_button_text:
            raise Exception("Invalid Add Place button index")

        # if proper button index found, then click the button to add the country place name
        add_place_num_btn_element.click()

        fill_out_country_and_validate_ui(driver, country_name, list_selection=list_selection)
        time.sleep(2)
    else:
        logging.debug(
            "Country " + str(country_name) + " cannot be added as the CountryPlaceNumber exceeding max limit.")

    list_country = "//body/main/div[4]/div/section/div[2]/div/ul/li" + "[" + country_place_number + "]"
    list_selection = list_country + "/button"
    driver.find_element_by_xpath(list_selection).click()
    time.sleep(2)


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

        select_product_text = driver.find_element_by_xpath("//input[@id='input-commodity-name']").text
        logging.debug("select_product_text -> " + select_product_text)

        for i in range(len(select_product_text)):
            driver.find_element_by_xpath(
                 "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").sendKeys(
                Keys.BACKSPACE)
        driver.find_element_by_xpath(
                 "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("")
        driver.find_element_by_xpath(
                 "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys(products)
        driver.find_element_by_xpath(
                "//body/div[4]/div/div/form/div[2]/div/div/div[2]/button/i").click()

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
