# -*- coding: utf-8 -*-
# flake8: noqa
# fmt: off
"""When step definitions."""
from behave import register_type, when
from behave.runner import Context
import time
import parse
from steps.then_impl import (
    should_be_on_page,
)
from steps.when_impl import (
    click_on_page_element,
    visit_page,
    generic_fill_out,
    generic_fill_out_and_submit_form,
    generic_country_name_to_fill_country_and_click_on_continue,
    generic_product_name_to_fill_country_and_click_on_continue,
    actor_decides_to_fill_country_and_click_on_continue,
    actor_decides_to_fill_product_and_click_on_continue,
    actor_decides_to_check_random_radio_and_click_on_continue,
    actor_decides_not_to_enter_any_text_and_click_on_page_element,
    actor_decides_to_enter_blank_spaces_click_on_continue,
    actor_decides_to_enter_email_address_and_click_login,
    actor_should_be_able_to_click_on_skipwalkthrough,
    actor_should_be_able_to_click_on_avatar,
    actor_should_be_able_to_click_on_SignOut,
    actor_decides_to_page_tour_and_click_on_page_element,
    actor_decides_to_enter_email_address_and_click_sign_up,
    generic_accept_all_cookies,
    promo_video_watch,
    promo_video_close,
)


@when('"{actor_alias}" decides to watch "{play_time:d}" seconds of the promotional video')
def when_actor_decides_to_watch_promo_video(
        context, actor_alias, *, play_time: int = None):
    promo_video_watch(context, actor_alias, play_time=play_time)


@when('"{actor_alias}" closes the window with promotional video')
def when_actor_decides_to_close_the_promotional_video(context, actor_alias):
    promo_video_close(context, actor_alias)


@when('"{actor_alias}" goes to the "{page_name}" page')
def when_actor_goes_to_page(context, actor_alias, page_name):
    visit_page(context, actor_alias, page_name)


@when('"{actor_alias}" decides to find out more about "{element_name}"')
@when('"{actor_alias}" decides to use "{element_name}" button')
@when('"{actor_alias}" decides to use "{element_name}" link')
@when('"{actor_alias}" decides to open "{element_name}"')
@when('"{actor_alias}" decides to click on "{element_name}"')
@when('"{actor_alias}" decides to see "{element_name}"')
@when('"{actor_alias}" decides to "{element_name}"')
def when_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name):
    click_on_page_element(context, actor_alias, element_name)


@when('"{actor_alias}" fills out and submits "{form_name}" form')
@when('"{actor_alias}" fills out and submits the form')
def when_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *, form_name: str = None, check_captcha_dev_mode: bool = False
):
    generic_fill_out_and_submit_form(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=check_captcha_dev_mode,
    )


@when('"{actor_alias}" decides to enter country name')
def when_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *, form_name: str = None, check_captcha_dev_mode: bool = False
):
    generic_fill_out(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=check_captcha_dev_mode,
    )


@when('"{actor_alias}" decides to enter country name "{country_name}" and click continue')
def when_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, country_name, *, form_name: str = None):
    actor_decides_to_fill_country_and_click_on_continue(context, actor_alias, country_name)


@when('"{actor_alias}" decides to enter product name "{product_name}" and click continue')
def when_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, product_name, *, form_name: str = None):
    actor_decides_to_fill_product_and_click_on_continue(context, actor_alias, product_name)


@when('"{actor_alias}" decides to select random treatment and click continue')
def when_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, *, form_name: str = None):
    actor_decides_to_check_random_radio_and_click_on_continue(context, actor_alias)


@when('"{actor_alias}" decides to enter country name and click "{element_name}"')
def when_actor_decides_to_fill_country_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    generic_country_name_to_fill_country_and_click_on_continue(context, actor_alias, element_name, form_name)


@when('"{actor_alias}" decides to enter product name and click "{element_name}"')
def when_actor_decides_to_fill_product_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    generic_product_name_to_fill_country_and_click_on_continue(context, actor_alias, element_name, form_name)


@when('"{actor_alias}" decides not to enter any text and click "{element_name}"')
def when_actor_decides_not_to_enter_any_text_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    actor_decides_not_to_enter_any_text_and_click_on_page_element(context, actor_alias, element_name)


@when('"{actor_alias}" decides to enter Blank Spaces in product name "{product_name}" and click "{element_name}"')
def when_actor_decides_to_enter_blank_spaces_click_on_continue(
        context, actor_alias, product_name, element_name, *, form_name: str = None):
    actor_decides_to_enter_blank_spaces_click_on_continue(context, actor_alias, product_name, element_name)


@when('"{actor_alias}" decides to enter email address "{email_address}", password "{password}" and click Login')
def when_actor_decides_to_enter_email_address_and_click_login(
        context, actor_alias, email_address, password):
    actor_decides_to_enter_email_address_and_click_login(context, actor_alias, email_address, password)


@when('"{actor_alias}" should be on the "{page_name}" page')
def when_actor_should_be_on_page(
        context, actor_alias, page_name):
    should_be_on_page(context, actor_alias, page_name)


@when('"{actor_alias}" should be able to click on SkipWalkthrough')
def when_actor_should_be_able_to_click_on_skipwalkthrough(
        context, actor_alias):
    actor_should_be_able_to_click_on_skipwalkthrough(context, actor_alias)


@when('"{actor_alias}" should be able to click on Avatar')
def when_actor_should_be_able_to_click_on_avatar(
        context, actor_alias):
    actor_should_be_able_to_click_on_avatar(context, actor_alias)


@when('"{actor_alias}" should be able to click on SignOut')
def when_actor_should_be_able_to_click_on_SignOut(
        context, actor_alias):
    actor_should_be_able_to_click_on_SignOut(context, actor_alias)


@when('"{actor_alias}" decides to page tour and click "{element_name}"')
def when_actor_decides_to_page_tour_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    actor_decides_to_page_tour_and_click_on_page_element(context, actor_alias, element_name)


@when('"{actor_alias}" decides to enter email address "{email_address}", password "{password}" and click Sign up')
def when_actor_decides_to_enter_email_address_and_click_sign_up(
        context, actor_alias, email_address, password):
    actor_decides_to_enter_email_address_and_click_sign_up(context, actor_alias, email_address, password)

# @when('"{actor_alias}" decides to accept all cookies')
# def when_actor_decides_to_accept_all_cookies(
#         context, actor_alias):
#     generic_accept_all_cookies(context, actor_alias)
