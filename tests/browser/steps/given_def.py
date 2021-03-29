# -*- coding: utf-8 -*-
# flake8: noqa
# fmt: off
"""Given step definitions."""
from behave import given
from behave.runner import Context
from browserpages.common_actions import generic_set_basic_auth_creds

from steps.then_impl import (
    should_be_on_page,
)
from steps.when_impl import (
    click_on_page_element,
    set_small_screen,
    visit_page,
)


@given('test authentication is done')
@given('test authentication is done for "{service_name}"')
def given_user_did_basic_auth(context: Context, *, service_name: str = None):
    generic_set_basic_auth_creds(context.driver, service_name=service_name)


@given('"{actor_alias}" has a small screen')
def given_actor_has_small_screen(context, actor_alias):
    set_small_screen(context)


@given('"{actor_alias}" went to the "{page_name}" page')
@given('"{actor_alias}" goes to the "{page_name}" page')
@given('"{actor_alias}" visited the "{page_name}" page')
@given('"{actor_alias}" visited "{page_name}" page')
@given('"{actor_alias}" visits the "{page_name}" page')
def given_actor_visits_page(context, actor_alias, page_name):
    visit_page(context, actor_alias, page_name)


@given('"{actor_alias}" got to the "{page_name}" page')
@given('"{actor_alias}" is on the "{page_name}" page')
def given_actor_is_on_page(context, actor_alias, page_name):
    should_be_on_page(context, actor_alias, page_name)


@given('"{actor_alias}" decided to use "{element_name}" button')
@given('"{actor_alias}" decided to use "{element_name}" link')
@given('"{actor_alias}" decided to "{element_name}"')
def given_actor_decided_to_click_on_page_element(
        context, actor_alias, element_name):
    click_on_page_element(context, actor_alias, element_name)
