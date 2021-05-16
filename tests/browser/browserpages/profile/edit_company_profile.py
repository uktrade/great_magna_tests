# -*- coding: utf-8 -*-
"""Profile - Edit Company Profile"""
import logging

from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages.common_actions import check_url, go_to_url

NAME = "Edit Company Profile"
SERVICE = Service.PROFILE
TYPE = PageType.PROFILE
URL = URLs.PROFILE_BUSINESS_PROFILE.absolute
PAGE_TITLE = "Business profile - great.gov.uk"

SELECTORS = {}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=True)
    logging.debug("All expected elements are visible on '%s' page", NAME)
