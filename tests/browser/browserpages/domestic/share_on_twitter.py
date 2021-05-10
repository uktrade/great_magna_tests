# -*- coding: utf-8 -*-
"""Share on Twitter Page Object."""
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared.enums import PageType, Service
from browserpages.common_actions import (
    Selector,
    assertion_msg,
    check_for_expected_sections_elements,
    find_element,
)

NAME = "Share on Twitter"
SERVICE = Service.TWITTER
TYPE = PageType.SHARE
URL = urljoin("https://twitter.com/", "intent/tweet?text=")
PAGE_TITLE = "Post a Tweet on Twitter"

MESSAGE_BOX = Selector(By.ID, "status")
SELECTORS = {"general": {"message_box": MESSAGE_BOX}}


def should_be_here(driver: WebDriver):
    check_for_expected_sections_elements(driver, SELECTORS)


def check_if_populated(driver: WebDriver, shared_url: str):
    status_update_message = find_element(driver, MESSAGE_BOX)
    with assertion_msg(
        "Expected to see article URL '%s' in LinkedIn's status update "
        "textbox, but couldn't find it in : %s",
        shared_url,
        status_update_message.text,
    ):
        assert shared_url in status_update_message.text
