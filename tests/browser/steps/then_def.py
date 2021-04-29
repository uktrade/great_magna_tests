# -*- coding: utf-8 -*-
# flake8: noqa
# fmt: off
"""Then steps definitions."""
from behave import then
from behave.runner import Context

from steps.then_impl import (
    should_be_on_page,
    should_be_able_to_see_error_message,
    actor_decides_to_click_country_name_change,
    actor_decides_to_click_product_search_change,
    actor_decides_to_click_refine_interaction_change,
    actor_decides_to_click_trade_data_change,
    actor_decides_to_click_proceed,
    actor_should_be_able_to_see_comodity_code,
    actor_clicked_on_start_again,
    should_see_following_sections,
    should_see_sections,
    actor_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code,
    actor_decides_to_enter_email_address_and_click_on_reset_password,
    actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm,
    actor_should_be_able_to_enter_products_and_country,
    actor_should_be_able_to_enter_products,
    actor_decides_to_click_checkbox_yes_for_lesson_complete,
    actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page,
    actor_should_be_able_to_see_progress_bar_for_section,
    actor_decides_to_enter_text,
    actor_decides_to_enter_value,
    actor_decides_to_validate_entered_text,
    actor_decides_to_select_random_item_list_on_page,
    actor_fill_business_objectives_details_on_page,
    actor_decides_to_delete_business_objectives_on_page,
    actor_decides_to_delete_country_details_on_page,
    actor_decides_to_click_checkbox_section_complete,
    actor_decides_to_select_random_checkbox_on_page,
    actor_decides_to_enter_value,
    actor_fill_document_details_on_page,
    actor_decides_to_delete_document_details_on_page,
    actor_enters_direct_costs_on_page,
    actor_enters_overhead_costs_on_page,
    actor_decides_to_select_funding_options_on_page,
    actor_decides_to_enter_product_name,
    actor_should_be_able_to_click_on_skipwalkthrough,
    actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months,
    actor_decides_to_click_on_search_again,
    actor_decides_to_click_on_product_and_search_again,
    actor_decides_to_click_on_select_save_random_products,
    actor_fill_trip_details_on_page,
    actor_decides_to_delete_trip_details_on_page,
    actor_decides_to_select_radio_button,
    actor_decides_to_enter_country_details,
    actor_decides_to_enter_country_name,
    generic_fill_out_and_submit_form,
    actor_fill_risk_details_on_page,
    actor_should_see_country_details_on_page,
    actor_should_see_last_visited_page_under_section_on_page,
    actor_decides_to_delete_route_to_market_on_page,
    actor_decides_to_delete_funding_options_on_page,
    actor_decides_to_validate_entered_country_details_and_change_from_the_list,
    actor_fills_out_and_submits_the_form,
)

from steps.when_impl import (
    click_on_page_element,
    click_on_page_element_with_wait,
    actor_decides_to_check_random_radio_and_click_on_continue,
    actor_should_be_on_refine_or_tradedata_page,
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page,
    actor_select_or_enter_random_data_click_continue_until_checkanswers_page,
    actor_decides_to_click_back_until_reaches_product_search_page,
    actor_select_random_data_click_continue_until_composition_page,
    actor_enter_random_composition_data_equal_to_hundred_percent,
    actor_enter_random_composition_data_not_equal_to_hundred_percent,
    promo_video_watch,
    promo_video_close,
    click_on_link_element_in_page,
)


@then('"{actor_alias}" decides to watch "{play_time:d}" seconds of the promotional video')
def when_actor_decides_to_watch_promo_video(
        context, actor_alias, *, play_time: int = None):
    promo_video_watch(context, actor_alias, play_time=play_time)


@then('"{actor_alias}" closes the window with promotional video')
def when_actor_decides_to_close_the_promotional_video(context, actor_alias):
    promo_video_close(context, actor_alias)


@then('"{actor_alias}" should be on the "{page_name}" page')
def then_actor_should_be_on_page(context, actor_alias, page_name):
    should_be_on_page(context, actor_alias, page_name)


@then('"{actor_alias}" decides to select random treatment and click continue')
def then_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, *, form_name: str = None):
    actor_decides_to_check_random_radio_and_click_on_continue(context, actor_alias)


@then('"{actor_alias}" should be on the refine or tradedata page')
def then_actor_should_be_on_refine_or_tradedata_page_after_click_continue_in_search(
        context, actor_alias, *, form_name: str = None):
    actor_should_be_on_refine_or_tradedata_page(context, actor_alias)


@then('"{actor_alias}" decides to click "{element_name}"')
def then_actor_decides_to_click_continue(
        context, actor_alias, element_name):
    click_on_page_element(context, actor_alias, element_name)


@then('"{actor_alias}" should be able to see error message "{error_message}" at element "{element_name}"')
def then_actor_should_be_able_to_see_error_message(
        context, actor_alias, error_message, element_name):
    should_be_able_to_see_error_message(context, actor_alias, element_name, error_message)


@then('"{actor_alias}" decides to click on "{element_name}"')
def then_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name):
    click_on_page_element(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click on section "{element_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name, page_name):
    click_on_page_element_with_wait(context, actor_alias, element_name, page_name=page_name)


@then('"{actor_alias}" decides to click with wait "{wait_for_it}" on section "{element_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_page_element_with_wait(
        context, actor_alias, element_name, page_name, wait_for_it):
    wait_or_not = True
    if wait_for_it == "True":
        wait_or_not = True
    else:
        wait_or_not = False
    click_on_page_element_with_wait(context, actor_alias, element_name, page_name=page_name, wait_for_it=wait_or_not)


@then('"{actor_alias}" decides to click on element "{element_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name, page_name):
    click_on_link_element_in_page(context, actor_alias, element_name, page_name=page_name)


@then('"{actor_alias}" decides to select random classification and click continue')
def then_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, *, form_name: str = None):
    actor_decides_to_check_random_radio_and_click_on_continue(context, actor_alias)


@then(
    '"{actor_alias}" decides to select random data and click continue for maximum "{max_number_pages}" times until it reaches Tradedata or CheckYourAnswers page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(context, actor_alias, max_number_pages,
                                                                                 True, True)


@then(
    '"{actor_alias}" decides to select random data and click continue for maximum "{max_number_pages}" times until it reaches CheckYourAnswers page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(context, actor_alias, max_number_pages,
                                                                                 False, True)


@then(
    '"{actor_alias}" decides to select/enter random data and click continue for maximum "{max_number_pages}" times until it reaches CheckYourAnswers page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_or_enter_random_data_click_continue_until_checkanswers_page(context, actor_alias, max_number_pages)


@then(
    '"{actor_alias}" decides to select random data and click continue for maximum "{max_number_pages}" times until it reaches Tradedata page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(context, actor_alias, max_number_pages,
                                                                                 True, False)


@then(
    '"{actor_alias}" decides to select random treatment and click continue for maximum "{max_number_pages}" times until it reaches Composition page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_composition_page(context, actor_alias, max_number_pages)


@then('"{actor_alias}" decides to enter random composition percents Equal to 100 and click "{element_name}"')
def then_actor_enter_random_composition_data_equal_to_hundred_percent(
        context, actor_alias, element_name):
    actor_enter_random_composition_data_equal_to_hundred_percent(context, actor_alias)
    click_on_page_element(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click Country Name "{element_name}"')
def then_actor_decides_to_click_country_name_change(
        context, actor_alias, element_name):
    actor_decides_to_click_country_name_change(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click Search term "{element_name}"')
def then_actor_decides_to_click_product_search_change(
        context, actor_alias, element_name):
    actor_decides_to_click_product_search_change(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click random Refinement "{element_name}"')
def then_actor_decides_to_click_random_refine_change(
        context, actor_alias, element_name):
    actor_decides_to_click_refine_interaction_change(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click proceed "{element_name}"')
def then_actor_decides_to_click_proceed(
        context, actor_alias, element_name):
    actor_decides_to_click_proceed(context, actor_alias, element_name)


@then('"{actor_alias}" should be able to see commodity code "{code}" for "{product}"')
def then_actor_should_be_able_to_see_comodity_code(
        context, actor_alias, code, product):
    actor_should_be_able_to_see_comodity_code(context, actor_alias, code, product)


@then('"{actor_alias}" decides to click on "{keyword_to_click}" to go to Home')
def then_actor_clicked_on_start_again(
        context, actor_alias, keyword_to_click):
    actor_clicked_on_start_again(context, actor_alias, keyword_to_click)


@then('"{actor_alias}" decides to enter random composition percents NotEqual to 100 and click "{element_name}"')
def then_actor_enter_random_composition_data_not_equal_to_hundred_percent(
        context, actor_alias, element_name):
    actor_enter_random_composition_data_not_equal_to_hundred_percent(context, actor_alias)
    click_on_page_element(context, actor_alias, element_name)


@then(
    '"{actor_alias}" decides to click on "{element_name}" for maximum "{max_number_pages}" times until it reaches "{page_name}" page')
def then_actor_decides_to_click_country_name_change(
        context, actor_alias, element_name, max_number_pages, page_name):
    actor_decides_to_click_back_until_reaches_product_search_page(context, actor_alias, element_name, max_number_pages,
                                                                  page_name)


@then('"{actor_alias}" should see following sections')
def then_should_see_sections(context, actor_alias):
    should_see_following_sections(context, actor_alias, sections_table=context.table)


@then(
    '"{actor_alias}" should be able to see confirmation code page from email "{email_address}", password "{password}" and enter code')
def then_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code(context, actor_alias,
                                                                                         email_address, password):
    actor_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code(context, email_address,
                                                                                          password)


@then('"{actor_alias}" decides to enter emailaddress "{email_address}" and click on reset password')
def then_actor_decides_to_enter_email_address_and_click_on_reset_password(
        context, actor_alias, email_address):
    actor_decides_to_enter_email_address_and_click_on_reset_password(context, email_address)


@then(
    '"{actor_alias}" should be able to click on reset password link from email "{email_address}", "{password}" and enters new password "{new_password}" and confirm')
def then_actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm(
        context, actor_alias, email_address, password, new_password):
    actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm(
        context, actor_alias, email_address, password, new_password)


@then('"{actor_alias}" should be able to enter products "{products}" and country "{country}"')
def then_actor_should_be_able_to_enter_products_and_country(context, actor_alias, products, country):
    actor_should_be_able_to_enter_products_and_country(context, products, country)


@then('"{actor_alias}" should be able to enter products "{products}"')
def then_actor_should_be_able_to_enter_products(context, actor_alias, products):
    actor_should_be_able_to_enter_products(context, products)


@then('"{actor_alias}" decides to click checkbox Yes and click continue on "{page_name}"')
def then_actor_decides_to_click_on_lesson_complete_and_click_continue(context, actor_alias, page_name):
    actor_decides_to_click_checkbox_yes_for_lesson_complete(context, page_name)
    click_on_page_element(context, actor_alias, "Continue learning", page_name=page_name)


@then('"{actor_alias}" decides to click checkbox Yes on "{page_name}"')
def then_actor_decides_to_click_on_lesson_complete_and_click_continue(context, actor_alias, page_name):
    actor_decides_to_click_checkbox_yes_for_lesson_complete(context, page_name)


@then('"{actor_alias}" decides to click section complete on "{page_name}"')
def then_actor_decides_to_click_on_section_complete_and_click_continue(context, actor_alias, page_name):
    actor_decides_to_click_checkbox_section_complete(context, page_name)


# @then('"{actor_alias}" decides to click "{element_name}"')
# def then_actor_decides_to_click_bottom_back(context, actor_alias,element_name):
#     actor_decides_to_click_on_bottom_back(context, actor_alias,element_name)

@then(
    '"{actor_alias}" decides to click continue for maximum "{max_number_pages}" times from page "{from_page_name}" until it reaches "{page_name}"')
def then_actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page(
        context, actor_alias, max_number_pages, from_page_name, page_name):
    actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page(context, actor_alias,
                                                                                       max_number_pages, from_page_name,
                                                                                       page_name)


@then('"{actor_alias}" should be able to see progress bar for section "{element_name}" on "{page_name}" page')
def then_actor_should_be_able_to_see_progress_bar_for_section(
        context, actor_alias, element_name, page_name):
    actor_should_be_able_to_see_progress_bar_for_section(context, actor_alias, element_name, page_name)


@then('"{actor_alias}" decides to enter text at "{element_name}" on page "{page_name}"')
def then_actor_decides_to_enter_text(context, actor_alias, element_name, page_name):
    actor_decides_to_enter_text(context, element_name, page_name)


@then('"{actor_alias}" decides to validate entered text at "{element_name}" on page "{page_name}"')
def then_actor_decides_to_validate_entered_text(context, actor_alias, element_name, page_name):
    actor_decides_to_validate_entered_text(context, element_name, page_name)


@then('"{actor_alias}" decides to select random item for "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_random_item_list_on_page(context, actor_alias, element_name, page_name):
    actor_decides_to_select_random_item_list_on_page(context, actor_alias, element_name, page_name)


@then('"{actor_alias}" fill business objective details on page "{page_name}"')
def then_actor_fill_business_objectives_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_business_objectives_details_on_page(context, actor_alias, row["Position"], row["Startdate"],
                                                       row["Enddate"], row["Objectives"], row["Owner"],
                                                       row["PlannedReviews"], page_name)


@then('"{actor_alias}" decides to delete business objectives on page "{page_name}"')
def then_actor_decides_to_delete_business_objectives_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_business_objectives_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" fill risk details on page "{page_name}"')
def then_actor_fill_risk_details_on_page(context, actor_alias,page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_risk_details_on_page(context, actor_alias, row["Position"], row["Risktext"], row["Contingencyplan"],page_name)

@then('"{actor_alias}" decides to delete country details on page "{page_name}"')
def then_actor_decides_to_delete_country_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_country_details_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to select random checkbox "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_random_checkbox_on_page(context, actor_alias, element_name, page_name):
    actor_decides_to_select_random_checkbox_on_page(context, actor_alias, element_name, page_name)


@then('"{actor_alias}" decides to enter value in "{element_name}" on page "{page_name}"')
def then_actor_decides_to_enter_value(context, actor_alias, element_name, page_name):
    actor_decides_to_enter_value(context, element_name, page_name)


@then('"{actor_alias}" fill document details on page "{page_name}"')
def then_actor_fill_document_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_document_details_on_page(context, actor_alias, row["Position"], row["DocumentName"], row["Notes"],
                                            page_name)


@then('"{actor_alias}" decides to delete document details on page "{page_name}"')
def then_actor_decides_to_delete_document_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_document_details_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" enters direct costs price on page "{page_name}"')
def then_actor_enters_direct_costs_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_enters_direct_costs_on_page(context, actor_alias, row["Productcost"], row["Labourcost"],
                                          row["Additionalmargin"], page_name)


@then('"{actor_alias}" enters overhead costs price on page "{page_name}"')
def then_actor_enters_overhead_costs_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_enters_overhead_costs_on_page(context, actor_alias, row["Product Adaptation"],
                                            row["Freight and Logistics"], row["Agent and Distribution fees"],
                                            row["Marketing"], row["Insurance"], page_name)


@then('"{actor_alias}" decides to select random funding options on page "{page_name}"')
def then_actor_decides_to_select_random_option_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_select_funding_options_on_page(context, actor_alias, row["Position"], row["Amount"], page_name)


@then('"{actor_alias}" decides to enter product name "{product_name}" on page "{page_name}"')
def then_actor_decides_to_enter_product_name(
        context, actor_alias, product_name, *, form_name: str = None, page_name):
    actor_decides_to_enter_product_name(context, actor_alias, product_name, page_name)


@then('"{actor_alias}" decides to enter country name "{country_name}" on the "{page_name}" Page')
def then_actor_decides_to_enter_country_name(
        context, actor_alias, country_name, *, form_name: str = None, page_name):
    actor_decides_to_enter_country_name(context, actor_alias, country_name, page_name)


@then('"{actor_alias}" should be able to click on SkipWalkthrough')
def then_actor_should_be_able_to_click_on_skipwalkthrough(
        context, actor_alias):
    actor_should_be_able_to_click_on_skipwalkthrough(context, actor_alias)


@then('"{actor_alias}" should be able to click on I have exported in the last 12 months')
def when_actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(
        context, actor_alias):
    actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(context, actor_alias)


@then('"{actor_alias}" decides to click on Search again on the "{page_name}" page')
def then_actor_decides_to_click_on_search_again(context, actor_alias, page_name):
    actor_decides_to_click_on_search_again(context, actor_alias, page_name)


@then('"{actor_alias}" decides to click on Product and Search again for "{product_name}" on the "{page_name}" Page')
def then_actor_decides_to_click_on_product_and_search_again(context, actor_alias, product_name, page_name):
    actor_decides_to_click_on_product_and_search_again(context, actor_alias, product_name, page_name)


@then('"{actor_alias}" decides to click on select and save random product options on the "{page_name}" page')
def then_actor_decides_to_click_on_select_save_random_products(context, actor_alias, page_name):
    actor_decides_to_click_on_select_save_random_products(context, actor_alias, page_name)


@then('"{actor_alias}" fill trip details on page "{page_name}"')
def then_actor_fill_trip_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_trip_details_on_page(context, actor_alias, row["Position"], row["TripName"], page_name)


@then('"{actor_alias}" decides to delete trip details on page "{page_name}"')
def then_actor_decides_to_delete_trip_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_trip_details_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to select radio button "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_radio_button(context, actor_alias, element_name, page_name):
    actor_decides_to_select_radio_button(context, element_name, page_name)


@then(
    '"{actor_alias}" decides to enter maximum "{country_max}" country names with display "{display_tab_count}" tabs on page "{page_name}"')
def then_actor_decides_to_enter_country_details(context, actor_alias, country_max, display_tab_count, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_enter_country_details(context, actor_alias, row["CountryName"]
                                               , country_place_number=row["CountryPlaceNumber"]
                                               , country_max=country_max
                                               , display_tab_count=display_tab_count
                                               , page_name=page_name)


@then('"{actor_alias}" fills out and submits the form')
def when_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *, form_name: str = None, check_captcha_dev_mode: bool = True
):
    generic_fill_out_and_submit_form(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=check_captcha_dev_mode,
    )

@then('"{actor_alias}" fills out and submits the contact us form')
def then_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *,page_name):
    actor_fills_out_and_submits_the_form(context, actor_alias, page_name)

@then('"{actor_alias}" should see country details on page "{page_name}"')
def then_actor_should_see_country_details_on_page(context, actor_alias, page_name):
    actor_should_see_country_details_on_page(context, actor_alias, page_name, on_all_tabs=False)


@then('"{actor_alias}" should see country details on all tabs on page "{page_name}"')
def then_actor_should_see_country_details_on_all_tabs_on_page(context, actor_alias, page_name):
    actor_should_see_country_details_on_page(context, actor_alias, page_name, on_all_tabs=True)


@then('"{actor_alias}" should see "{text_to_see}" text under section "{section_name}" on page "{page_name}"')
def then_actor_should_see_last_visited_page_under_section_on_page(context, actor_alias, text_to_see, section_name,
                                                                  page_name):
    actor_should_see_last_visited_page_under_section_on_page(context, actor_alias, text_to_see, section_name, page_name)


@then('"{actor_alias}" decides to delete route to market on page "{page_name}"')
def then_actor_decides_to_delete_route_to_market_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_route_to_market_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to delete funding options on page "{page_name}"')
def then_actor_decides_to_delete_funding_options_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_funding_options_on_page(context, actor_alias, row["Position"], page_name)

@then('"{actor_alias}" decides to validate entered country details and change from the list "{page_name}"')
def then_actor_decides_to_validate_entered_country_details_and_change_from_the_list(context, actor_alias, country_max,list_selection, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_validate_entered_country_details_and_change_from_the_list(context, actor_alias, row["CountryName"]
                                               , country_place_number=row["CountryPlaceNumber"]
                                               , country_max=country_max
                                               ,list_selection=list_selection
                                               , page_name=page_name)