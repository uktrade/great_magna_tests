# -*- coding: utf-8 -*-
"""Then step implementations."""
import logging
from collections import defaultdict
from inspect import signature
from typing import List, Union
from urllib.parse import urlparse
import time
import requests
from behave.model import Table
from behave.runner import Context
from datadiff import diff
from retrying import retry
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

from great_magna_tests_shared.utils import blue, check_for_errors, get_comparison_details
from browserpages import (
    get_page_object,
)
from browserpages.common_actions import (
    accept_all_cookies,
    assertion_msg,
    avoid_browser_stack_idle_timeout_exception,
    get_actor,
    get_full_page_name,
    get_last_visited_page,
    selenium_action,
    take_screenshot,
    update_actor,
)
from steps import has_action
from browserutils.browser import clear_driver_cookies

from browserutils.gtm import (
    get_gtm_data_layer_events,
    get_gtm_data_layer_properties,
    replace_string_representations,
)


def should_be_on_page(context: Context, actor_alias: str, page_name: str):
    page = get_page_object(page_name)
    page_source = context.driver.page_source
    # revisit_page_on_access_denied(context.driver, page, page_name)
    take_screenshot(context.driver, f"should be on {page_name}")
    check_for_errors(page_source, context.driver.current_url)
    accept_all_cookies(context.driver)
    has_action(page, "should_be_here")
    if hasattr(page, "SubURLs"):
        special_page_name = page_name.split(" - ")[1].lower()
        if signature(page.should_be_here).parameters.get("page_name"):
            page.should_be_here(context.driver, page_name=special_page_name)
        else:
            raise TypeError(
                f"{page.__name__}.should_be_here() doesn't accept 'page_name' keyword "
                f"argument but it should as this Page Object has 'SubURLs' attribute."
            )
    else:
        page.should_be_here(context.driver)
    update_actor(context, actor_alias, visited_page=page)
    logging.debug(
        f"{actor_alias} is on {page.SERVICE} - {page.NAME} - {page.TYPE} -> " f"{page}"
    )


def should_be_able_to_see_error_message(context, actor_alias, element_name, expected_error_message):
    default_page = "GreatMagna - Login"
    page = get_page_object(default_page)
    has_action(page, "should_be_error_message")
    if page.should_be_error_message(context.driver, element_name, expected_error_message) == False:
        error = f"Error message not found on the page {page.NAME}"
        assert False, error


def actor_decides_to_check_random_radio_and_click_on_continue(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_select_random_radio_and_click_continue")
    page.find_and_select_random_radio_and_click_continue(context.driver)


def actor_decides_to_click_country_name_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_and_click_change_link")
    page.find_and_click_change_link(context.driver, "country_name_change")


def actor_decides_to_click_product_search_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_and_click_change_link")
    current_url = context.driver.current_url
    if "look-up" in current_url:
        page.find_and_click_change_link(context.driver, "lookup_product_search_change")
    else:
        page.find_and_click_change_link(context.driver, "product_search_change")


def actor_decides_to_click_refine_interaction_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_elements_and_click_change_link")
    page.find_elements_and_click_change_link(context.driver, "refine")


def actor_decides_to_click_trade_data_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_elements_and_click_change_link")
    page.find_elements_and_click_change_link(context.driver, "tradedata")


def actor_decides_to_click_proceed(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_and_click_change_link")
    page.find_and_click_change_link(context.driver, "submit")


def actor_should_be_able_to_see_comodity_code(
        context, actor_alias, code, product):
    page = get_page_object("ImportTariff - Confirmation Code")
    has_action(page, "find_and_select_comodity_code")
    if page.find_and_select_comodity_code(context.driver, code, product) == False:
        error = f"Couldn't find Comodity code on the Confirmation page"
        assert False, error


def actor_clicked_on_start_again(
        context, actor_alias, keyword_to_click):
    page = get_page_object("ImportTariff - Confirmation Code")
    has_action(page, "find_and_click_start_again")
    page.find_and_click_start_again(context.driver, keyword_to_click)


def should_see_following_sections(context: Context, actor_alias: str, sections_table: Table = None, *,
                                  sections_list: list = None, ):
    sections = sections_list or [row[0] for row in sections_table]
    logging.debug(
        "%s will look for following sections: '%s' on %s",
        actor_alias,
        sections,
        context.driver.current_url,
    )
    page = get_last_visited_page(context, actor_alias)
    # page = get_page_object("GreatMagna - Dashboard")
    has_action(page, "should_see_following_sections")
    page.should_see_following_sections(context.driver, sections)


def actor_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code(context: Context
                                                                                          , email_address: str,
                                                                                          password: str):
    page = get_page_object("GreatMagna - Sign Up")
    has_action(page, "confirmation_code")
    page.confirmation_code(context.driver, email_address, password)


def actor_decides_to_enter_email_address_and_click_on_reset_password(context: Context, email_address: str):
    page = get_page_object("GreatMagna - forgotten password")
    has_action(page, "fill_out_email_address")
    details_dict = {"emailaddress": email_address}
    page.fill_out_email_address(context.driver, details_dict)


def actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm(
        context: Context, actor_alias: str, email_address: str, password: str, new_password: str):
    page = get_page_object("GreatMagna - forgotten password")
    has_action(page, "read_reset_password_email")
    page.read_reset_password_email(context.driver, email_address, password, new_password)


def actor_should_be_able_to_enter_products_and_country(context, products, country):
    page = get_page_object("GreatMagna - Dashboard")
    has_action(page, "fill_out_products_and_country")
    page.fill_out_products_and_country(context.driver, products, country)


def actor_should_be_able_to_enter_products(context, products):
    page = get_page_object("GreatMagna - Dashboard")
    has_action(page, "fill_out_products")
    page.fill_out_products(context.driver, products)


def actor_decides_to_click_checkbox_yes_for_lesson_complete(context, page_name: str):
    page = get_page_object(page_name)
    has_action(page, "check_lesson_complete_yes")
    page.check_lesson_complete_yes(context.driver, "lesson yes checkbox")


def actor_decides_to_click_checkbox_section_complete(context, page_name: str):
    page = get_page_object(page_name)
    has_action(page, "check_section_complete_yes")
    page.check_section_complete_yes(context.driver, "yes checkbox")


# def actor_decides_to_click_on_bottom_back(context: Context, actor_alias: str,element_name : str):
#     page = get_page_object("LearnToExport - Introduction to Lessons and Learning Page")
#     has_action(page, "bottom_back")
#     page.bottom_back(context.driver,element_name)


def actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page(
        context, actor_alias, max_number_pages, from_page_name, to_page_name):
    counter = 0
    while counter < int(max_number_pages):
        page = get_page_object(from_page_name)
        # logging.debug("visiting page  - "+ page.NAME)
        has_action(page, "find_and_click")
        page.find_and_click(context.driver, element_selector_name="continue learning")
        current_page_url = str(context.driver.current_url)
        # logging.debug("Last visited page - "+current_page_url)
        # time.sleep(1)
        counter += 1
        if to_page_name in current_page_url:
            break


def actor_should_be_able_to_see_progress_bar_for_section(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_progress_bar")
    page.find_progress_bar(context.driver, element_name)


def actor_decides_to_enter_text(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_text")
    page.enter_text(context.driver, element_name)


def actor_decides_to_validate_entered_text(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "validate_entered_text")
    if False == page.validate_entered_text(context.driver, element_name):
        error = f"Randomly entered text not found in the text input area on the page {page.NAME}"
        assert False, error


def actor_decides_to_select_random_item_list_on_page(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_item_list")
    page.find_and_select_random_item_list(context.driver, element_name)


def actor_fill_business_objectives_details_on_page(context, actor_alias, position, startdate, enddate, objectives,
                                                   owner, plannedreviews, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_business_objectives_details")
    page.enter_business_objectives_details(context.driver, position, startdate, enddate, objectives, owner,
                                           plannedreviews)


def actor_decides_to_delete_business_objectives_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_business_objectives")
    page.delete_all_business_objectives(context.driver, position)


def should_see_sections(
        context: Context,
        actor_alias: str,
        sections_table: Table = None,
        *,
        sections_list: list = None,
):
    sections = sections_list or [row[0] for row in sections_table]
    logging.debug(
        "%s will look for following sections: '%s' on %s",
        actor_alias,
        sections,
        context.driver.current_url,
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_sections")
    page.should_see_sections(context.driver, sections)


def actor_decides_to_select_random_checkbox_on_page(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "random_select_checkbox")
    page.random_select_checkbox(context.driver, element_name)


def actor_decides_to_enter_value(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_value")
    page.enter_value(context.driver, element_name)


def actor_fill_document_details_on_page(context, actor_alias, position, documentname, notes, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_document_details")
    page.enter_document_details(context.driver, position, documentname, notes)


def actor_decides_to_delete_document_details_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_document_details")
    page.delete_all_document_details(context.driver, position)


def actor_enters_direct_costs_on_page(context, actor_alias, productcost, labourcost, additionalmargin, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_direct_costs")
    page.enter_direct_costs(context.driver, productcost, labourcost, additionalmargin)


def actor_enters_overhead_costs_on_page(context, actor_alias, productadaptation, freightandlogistics,
                                        agentanddistributionfees, marketing, finance, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_overhead_costs")
    page.enter_overhead_costs(context.driver, productadaptation, freightandlogistics, agentanddistributionfees,
                              marketing, finance)


def actor_decides_to_select_funding_options_on_page(context, actor_alias, position, amount, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_funding_options")
    page.find_and_select_random_funding_options(context.driver, position, amount)


def actor_decides_to_enter_product_name(context, actor_alias, product_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "where_to_export")
    page.where_to_export(context.driver, product_name=product_name)


def actor_should_be_able_to_click_on_skipwalkthrough(
        context, actor_alias):
    # time.sleep(5)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_skip_walk_through")
    # has_action(page, "click_avatar")
    page.click_skip_walk_through(context.driver)
    # page.click_avatar(context.driver)


def actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_on_i_have_exported_in_the_last_12_months")
    page.click_on_i_have_exported_in_the_last_12_months(context.driver)


def actor_decides_to_click_on_search_again(context, actor_alias, page_name):
    page = get_page_object(page_name)
    has_action(page, "search_again_top_bottom")
    page.search_again_top_bottom(context.driver)


def actor_decides_to_click_on_product_and_search_again(context, actor_alias, product_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "select_product_search_again_top_bottom")
    page.select_product_search_again_top_bottom(context.driver, product_name)


def actor_decides_to_click_on_select_save_random_products(context, actor_alias, page_name):
    page = get_page_object(page_name)
    has_action(page, "search_select_save_random_next")
    page.search_select_save_random_next(context.driver)


def actor_fill_trip_details_on_page(context, actor_alias, position, tripname, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_trip_details")
    page.enter_trip_details(context.driver, position, tripname)


def actor_decides_to_delete_trip_details_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_trip_details")
    page.delete_all_trip_details(context.driver, position)


def actor_decides_to_select_radio_button(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "select_radio_button")
    page.select_radio_button(context.driver, element_name=element_name)


def actor_decides_to_enter_country_details(context, actor_alias, countryname, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_country_details")
    page.enter_country_details(context.driver, countryname)
