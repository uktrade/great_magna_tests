# -*- coding: utf-8 -*-
"""When step implementations."""
import logging
import random
from inspect import signature
from types import MethodType
from typing import Dict
from urllib.parse import urljoin
import time

from behave.model import Table
from behave.runner import Context
from retrying import retry
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared.utils import check_for_errors
from browserpages import (
    search,
    get_page_object,
    greatmagna,
    learntoexport,
)

from browserpages.common_actions import (
    accept_all_cookies,
    add_actor,
    assert_catcha_in_dev_mode,
    avoid_browser_stack_idle_timeout_exception,
    barred_actor,
    find_and_click_on_page_element,
    find_elements,
    find_selector_by_name,
    get_actor,
    get_full_page_name,
    get_last_visited_page,
    go_to_url,
    scroll_to,
    selenium_action,
    take_screenshot,
    try_alternative_click_on_exception,
    unauthenticated_actor,
    untick_selected_checkboxes,
    update_actor,
    update_actor_forms_data,
    wait_for_page_load_after_action,

)
from steps import has_action
from browserutils.gtm import get_gtm_event_definitions, trigger_js_event

NUMBERS = {
    "random": 0,
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "sixth": 6,
}


def retry_if_webdriver_error(exception):
    """Return True if we should retry on WebDriverException, False otherwise"""
    return isinstance(exception, (TimeoutException, WebDriverException))


def retry_if_assertion_error(exception):
    """Return True if we should retry on AssertionError, False otherwise"""
    return isinstance(exception, AssertionError)


# BrowserStack times out after 60 seconds of inactivity
# https://www.browserstack.com/automate/timeouts
@retry(
    wait_fixed=5000,
    stop_max_attempt_number=5,
    retry_on_exception=retry_if_webdriver_error,
    wrap_exception=False,
)
def visit_page(context: Context, actor_alias: str, page_name: str):
    """Will visit specific page.

    NOTE:
    In order for the retry scheme to work properly you should have
    the webdriver' page load timeout set to value lower than the retry's
    `wait_fixed` timer, e.g `driver.set_page_load_timeout(time_to_wait=30)`
    """

    def is_special_case(page_name: str) -> bool:
        parts = page_name.split(" - ")
        return len(parts) == 3

    if not get_actor(context, actor_alias):
        add_actor(context, unauthenticated_actor(actor_alias))

    page = get_page_object(page_name)

    has_action(page, "visit")

    if is_special_case(page_name) and hasattr(page, "SubURLs"):
        subpage_name = page_name.split(" - ")[1].lower()
        special_url = page.SubURLs[subpage_name]
        logging.debug(
            f"{actor_alias} will visit '{page_name}' subpage using: '{special_url}"
        )
        page.visit(context.driver, page_name=subpage_name)
    else:
        logging.debug(
            f"{actor_alias} will visit '{page_name}' page using: '{page.URL}'"
        )
        page.visit(context.driver)

    take_screenshot(context.driver, f"visit page {page_name}")
    accept_all_cookies(context.driver)
    check_for_errors(context.driver.page_source, context.driver.current_url)
    update_actor(context, actor_alias, visited_page=page)


def set_small_screen(context: Context):
    context.driver.set_window_position(0, 0)
    context.driver.set_window_size(768, 1024)


def should_be_on_page(context: Context, actor_alias: str, page_name: str):
    page = get_page_object(page_name)
    # revisit_page_on_access_denied(context.driver, page, page_name)
    take_screenshot(context.driver, f"should be on {page_name}")
    check_for_errors(context.driver.page_source, context.driver.current_url)
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


def clear_the_cookies(context: Context, actor_alias: str):
    try:
        cookies = context.driver.get_cookies()
        logging.debug("COOKIES: %s", cookies)
        context.driver.delete_all_cookies()
        logging.debug("Successfully cleared cookies for %s", actor_alias)
        cookies = context.driver.get_cookies()
        logging.debug("Driver cookies after clearing them: %s", cookies)
    except WebDriverException:
        logging.error("Failed to clear cookies for %s", actor_alias)


def generic_accept_all_cookies(context: Context, actor_alias: str):
    driver = context.driver
    accept_all_cookies(driver)
    logging.debug(f"{actor_alias} accepted all cookies on {driver.current_url}")


def click_on_page_element(
        context: Context, actor_alias: str, element_name: str, *, page_name: str = None
):
    if page_name:
        page = get_page_object(page_name)
    else:
        page = get_last_visited_page(context, actor_alias)
    logging.debug(page)
    find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
    logging.debug(
        "%s decided to click on '%s' on '%s' page", actor_alias, element_name, page.NAME
    )


def click_on_page_element_with_wait(
        context: Context, actor_alias: str, element_name: str, *, page_name: str = None, wait_for_it: bool = True
):
    if page_name:
        page = get_page_object(page_name)
    else:
        page = get_last_visited_page(context, actor_alias)
    logging.debug(page)
    find_and_click_on_page_element(context.driver, page.SELECTORS, element_name, wait_for_it=wait_for_it)
    logging.debug(
        "%s decided to click on '%s' on '%s' page", actor_alias, element_name, page.NAME
    )


@retry(
    wait_fixed=1000,
    stop_max_attempt_number=8,
    retry_on_exception=retry_if_assertion_error,
    wrap_exception=False,
)
def generic_fill_out_and_submit_form(
        context: Context,
        actor_alias: str,
        *,
        custom_details_table: Table = None,
        retry_on_errors: bool = False,
        go_back: bool = False,
        form_name: str = None,
        check_captcha_dev_mode: bool = False,
):
    if check_captcha_dev_mode:
        assert_catcha_in_dev_mode(context.driver)
    actor = get_actor(context, actor_alias)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "generate_form_details")
    has_action(page, "fill_out")
    has_action(page, "submit")
    if form_name:
        error = f"generate_form_details() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.generate_form_details).parameters.get("form_name"), error
        error = f"fill_out() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.fill_out).parameters.get("form_name"), error
        error = f"submit() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.submit).parameters.get("form_name"), error
    if custom_details_table:
        custom_details_table.require_column("field")
        custom_details_table.require_column("value")
        value_mapping = {"unchecked": False, "checked": True, "empty": None}
        custom_details = {}
        for row in custom_details_table.rows:
            key = row["field"].lower()
            value = row["value"]
            custom_details[key] = value_mapping.get(value, value)
        if form_name:
            details = page.generate_form_details(
                actor, custom_details=custom_details, form_name=form_name
            )
        else:
            details = page.generate_form_details(actor, custom_details=custom_details)
    else:
        if form_name:
            details = page.generate_form_details(actor, form_name=form_name)
        else:
            details = page.generate_form_details(actor)
    logging.debug(f"{actor_alias} will fill out the form with: {details}")

    update_actor_forms_data(context, actor, details)

    if form_name:
        page.fill_out(context.driver, details, form_name=form_name)
    else:
        page.fill_out(context.driver, details)

    if hasattr(page, "get_form_details"):
        logging.debug(f"Getting form details from filled out form: {page}")
        form_data = page.get_form_details(context.driver)
        if form_data:
            update_actor_forms_data(context, actor, form_data)
    else:
        if details:
            update_actor_forms_data(context, actor, details)

    if form_name:
        page.submit(context.driver, form_name=form_name)
    else:
        page.submit(context.driver)
    # if retry_on_errors:
    #     check_for_errors_or_non_trading_companies(context.driver, go_back=go_back)


@retry(
    wait_fixed=1000,
    stop_max_attempt_number=8,
    retry_on_exception=retry_if_assertion_error,
    wrap_exception=False,
)
def generic_fill_out(
        context: Context,
        actor_alias: str,
        *,
        custom_details_table: Table = None,
        retry_on_errors: bool = False,
        go_back: bool = False,
        form_name: str = None,
        check_captcha_dev_mode: bool = True,
):
    if check_captcha_dev_mode:
        assert_catcha_in_dev_mode(context.driver)
    actor = get_actor(context, actor_alias)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "generate_form_details")
    has_action(page, "fill_out")
    if form_name:
        error = f"generate_form_details() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.generate_form_details).parameters.get("form_name"), error
        error = f"fill_out() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.fill_out).parameters.get("form_name"), error
    if custom_details_table:
        custom_details_table.require_column("field")
        custom_details_table.require_column("value")
        value_mapping = {"unchecked": False, "checked": True, "empty": None}
        custom_details = {}
        for row in custom_details_table.rows:
            key = row["field"].lower()
            value = row["value"]
            custom_details[key] = value_mapping.get(value, value)
        if form_name:
            details = page.generate_form_details(
                actor, custom_details=custom_details, form_name=form_name
            )
        else:
            details = page.generate_form_details(actor, custom_details=custom_details)
    else:
        if form_name:
            details = page.generate_form_details(actor, form_name=form_name)
        else:
            details = page.generate_form_details(actor)
    logging.debug(f"{actor_alias} will fill out the form with: {details}")

    update_actor_forms_data(context, actor, details)

    if form_name:
        page.fill_out(context.driver, details, form_name=form_name)
    else:
        page.fill_out(context.driver, details)

    if hasattr(page, "get_form_details"):
        logging.debug(f"Getting form details from filled out form: {page}")
        form_data = page.get_form_details(context.driver)
        if form_data:
            update_actor_forms_data(context, actor, form_data)
    else:
        if details:
            update_actor_forms_data(context, actor, details)


def generic_submit_form(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "submit")
    page.submit(context.driver)


def actor_decides_to_fill_country_and_click_on_continue(
        context, actor_alias, country_name):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "countrysearch")
    page.countrysearch(context.driver, country_name=country_name)


def generic_country_name_to_fill_country_and_click_on_continue(
        context, actor_alias, element_name, form_name):
    generic_fill_out(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=False,
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "searchcontinue")
    page.searchcontinue(context.driver)


def generic_product_name_to_fill_country_and_click_on_continue(
        context, actor_alias, element_name, form_name):
    generic_fill_out(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=False,
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "searchcontinue")
    page.searchcontinue(context.driver)


def actor_decides_to_fill_product_and_click_on_continue(
        context, actor_alias, product_name):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "productsearch")
    page.productsearch(context.driver, product_name=product_name)


def actor_decides_to_check_random_radio_and_click_on_continue(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_select_random_radio_and_click_continue")
    page.find_and_select_random_radio_and_click_continue(context.driver)


def actor_should_be_on_refine_or_tradedata_page(
        context, actor_alias):
    actor_should_be_on_appropriate_page(context, actor_alias)


def actor_should_be_on_appropriate_page(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    current_page_url = str(context.driver.current_url)
    # logging.debug(f"actor_should_be_on_appropriate_page:current_page_url -> {current_page_url}")
    is_refinement_page = False
    is_tradedata_page = False
    is_check_answers_page = False
    if "refine/?interaction" in current_page_url:
        is_refinement_page = True
    if "tradedata/?code" in current_page_url:
        is_tradedata_page = True
    if "check-your-answers" in current_page_url:
        is_check_answers_page = True

    if is_refinement_page:
        should_be_on_page(context, actor_alias, "Search - Refinement interaction")
        return
    if is_tradedata_page:
        should_be_on_page(context, actor_alias, "Search - Tradedata Codes")
        return
    error = f"Landed on unrecognized page"
    assert False, error


def actor_decides_not_to_enter_any_text_and_click_on_page_element(context, actor_alias, element_name):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "searchcontinue")
    page.searchcontinue(context.driver)


def actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(
        context, actor_alias, max_number_pages, is_trade_data_page, is_check_your_answers_page):
    landed_on_tradedata_page = False
    landed_on_checkanswers_page = False
    counter = 0
    while counter < int(max_number_pages):
        counter += 1
        page = get_last_visited_page(context, actor_alias)
        has_action(page, "find_and_select_random_radio_and_click_continue")
        page.find_and_select_random_radio_and_click_continue(context.driver)
        # time.sleep(1)
        current_page_url = str(context.driver.current_url)
        # logging.debug(f"actor_select_random_data_click_continue_until_tradedata_page:current_page_url -> {current_page_url}")
        if "tradedata/?code" in current_page_url and is_trade_data_page:
            landed_on_tradedata_page = True
            break
        if "check-your-answers" in current_page_url and is_check_your_answers_page:
            landed_on_checkanswers_page = True
            break

    if not landed_on_tradedata_page and not landed_on_checkanswers_page:
        error = f"Couldn't reach Tradedata or CheckYourAnswers page after {max_number_pages} attempts!"
        assert False, error


def actor_select_or_enter_random_data_click_continue_until_checkanswers_page(
        context, actor_alias, max_number_pages):
    counter = 0
    while counter < int(max_number_pages):
        current_page_url = str(context.driver.current_url)
        # logging.debug(f"current_page_url -> {current_page_url}")
        # time.sleep(1)
        if "tradedata/?code" in current_page_url:
            page = get_page_object("Search - Tradedata codes")
            has_action(page, "find_and_select_random_radio_and_click_continue")
            has_action(page, "searchcontinue")
            page.find_and_select_random_radio_and_click_continue(context.driver)
            page.searchcontinue(context.driver)
        elif "check-your-answers" in current_page_url:
            break
        elif "refine/?interaction" in current_page_url:
            try:
                page = get_page_object("Search - Refinement Interaction")
                has_action(page, "find_and_select_random_radio_and_click_continue")
                page.find_and_select_random_radio_and_click_continue(context.driver)
                # time.sleep(1)
                composition_text_element = context.driver.find_element_by_xpath("//*[@id=\"composition_message\"]")
                composition_text = str(composition_text_element.text)
                if "The numbers need to add up to 100." in composition_text:
                    page = get_page_object("Search - Refinement Interaction")
                    has_action(page, "find_and_enter_random_composition_percent")
                    page.find_and_enter_random_composition_percent(context.driver, "100")
                    find_and_click_on_page_element(context.driver, page.SELECTORS, "Continue")
            except NoSuchElementException:
                pass
        counter += 1


def actor_decides_to_click_back_until_reaches_product_search_page(
        context, actor_alias, element_name, max_number_pages, page_name):
    counter = 0
    while counter < int(max_number_pages):
        current_page_url = str(context.driver.current_url)
        # logging.debug(f"current_page_url -> {current_page_url}")
        if "tradedata/?code" in current_page_url:
            page = get_page_object("Search - Tradedata codes")
            find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
        elif "check-your-answers" in current_page_url:
            page = get_page_object("ImportTariff - CheckYourAnswers")
            find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
        elif "search/" in current_page_url:
            page = get_page_object(page_name)
            break
        elif "refine/?interaction" in current_page_url:
            page = get_page_object("Search - Refinement Interaction")
            find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
        else:
            error = f"Landed on unrecognized page after {counter} attempts!"
            assert False, error

        counter += 1


def actor_select_random_data_click_continue_until_composition_page(
        context, actor_alias, max_number_pages):
    landed_on_composition_page = False
    counter = 0
    while counter < int(max_number_pages):
        counter += 1

        current_page_url = str(context.driver.current_url)
        # logging.debug(f"actor_select_random_data_click_continue_until_composition_page:current_page_url -> {current_page_url}")

        try:
            page = get_last_visited_page(context, actor_alias)
            has_action(page, "find_and_select_random_radio_and_click_continue")
            page.find_and_select_random_radio_and_click_continue(context.driver)
            # page = get_last_visited_page(context, actor_alias)
            # logging.debug(
            #     f"actor_select_random_data_click_continue_until_composition_page:get_last_visited_page ->  {page.NAME}")
            # should_be_on_page(context, actor_alias, f"Search - {page.NAMES[1]}")
            composition_text_element = context.driver.find_element_by_xpath("//*[@id=\"composition_message\"]")
            composition_text = str(composition_text_element.text)
            # logging.debug(
            #     f"actor_select_random_data_click_continue_until_composition_page:composition_text ->  {composition_text}")

            if "The numbers need to add up to 100." in composition_text:
                landed_on_composition_page = True
                # logging.debug(
                #     f"actor_select_random_data_click_continue_until_composition_page:Reached Composition page!")
        except NoSuchElementException:
            logging.debug(
                f"actor_select_random_data_click_continue_until_composition_page:Couldn't reach Composition page after {counter} attempts!")

        if landed_on_composition_page:
            break

    if not landed_on_composition_page:
        error = f"Couldn't reach Composition page after {max_number_pages} attempts!"
        assert False, error


def actor_enter_random_composition_data_equal_to_hundred_percent(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_enter_random_composition_percent")
    page.find_and_enter_random_composition_percent(context.driver, "100")


def actor_enter_random_composition_data_not_equal_to_hundred_percent(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_enter_random_composition_percent")
    page.find_and_enter_random_composition_percent(context.driver, "80")


def actor_decides_to_enter_blank_spaces_click_on_continue(
        context, actor_alias, product_name, element_name):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "productsearch")
    page.productsearch(context.driver, product_name=product_name)
    click_on_page_element(context, actor_alias, element_name)


def actor_decides_to_enter_email_address_and_click_login(
        context, actor_alias, email_address, password):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "login")
    email_address = str(email_address).strip()  # trimming
    password = str(password).strip()  # trimming
    page.login(context.driver, email_address=email_address, password=password)


def actor_decides_to_enter_email_address_and_click_sign_up(
        context, actor_alias, email_address, password):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "sign_up")
    email_address = email_address.replace("xxxx", str(random.randint(6666, 9999)))
    page.sign_up(context.driver, email_address=email_address, password=password)


def actor_should_be_able_to_click_on_skipwalkthrough(
        context, actor_alias):
    # time.sleep(5)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_skip_walk_through")
    # has_action(page, "click_avatar")
    page.click_skip_walk_through(context.driver)
    # page.click_avatar(context.driver)


def actor_should_be_able_to_click_on_avatar(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_avatar")
    page.click_avatar(context.driver)


def actor_should_be_able_to_click_on_SignOut(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_signout")
    page.click_signout(context.driver)


def actor_decides_to_page_tour_and_click_on_page_element(
        context, actor_alias, element_name):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_show_me_around")
    page.click_show_me_around(context.driver)


def promo_video_watch(context: Context, actor_alias: str, *, play_time: int = None):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "play_video")
    page.play_video(context.driver, play_time=play_time)
    logging.debug("%s was able to play the video", actor_alias)


def promo_video_close(context: Context, actor_alias: str):
    learntoexport.choose_the_right_route_to_market.close_video(context.driver)
    logging.debug("%s closed the video", actor_alias)


def click_on_link_element_in_page(
        context: Context, actor_alias: str, element_name: str, *, page_name: str = None
):
    if page_name:
        page = get_page_object(page_name)
    else:
        page = get_last_visited_page(context, actor_alias)
    # logging.debug(page)
    has_action(page, "find_and_click")
    page.find_and_click(context.driver, element_selector_name=element_name)


def generic_submit_form(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "submit")
    page.submit(context.driver)
