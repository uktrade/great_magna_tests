# -*- coding: utf-8 -*-
"""Domestic - Domestic Contact us - Great.gov.uk account"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType
from browserpages.common_actions import Selector, check_url, go_to_url

NAME = "Great.gov.uk account"
NAMES = [
    "I have not received an email confirmation",
    "I need to reset my password",
    "My Companies House login is not working",
    "I do not know where to enter my verification code",
    "I have not received my letter containing the verification code",
    "I have not received a verification code",
]
SERVICE = Service.DOMESTIC
TYPE = PageType.DEDICATED_SUPPORT_CONTENT
URL = URLs.CONTACT_US_GREAT_ACCOUNT.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

# fmt: off
SubURLs = {
    "great.gov.uk account": URL,
    "i have not received an email confirmation":
        URLs.CONTACT_US_GREAT_ACCOUNT_NO_VERIFICATION_EMAIL.absolute,
    "i need to reset my password":
        URLs.CONTACT_US_GREAT_ACCOUNT_PASSWORD_RESET.absolute,
    "my companies house login is not working":
        URLs.CONTACT_US_GREAT_ACCOUNT_CH_LOGIN.absolute,
    "i do not know where to enter my verification code":
        URLs.CONTACT_US_GREAT_ACCOUNT_VERIFICATION_LETTER_CODE.absolute,
    "i have not received my letter containing the verification code":
        URLs.CONTACT_US_GREAT_ACCOUNT_NO_VERIFICATION_LETTER.absolute,
    "i have not received a verification code":
        URLs.CONTACT_US_GREAT_ACCOUNT_VERIFICATION_MISSING.absolute,
}
# fmt: on

SUBMIT_BUTTON = Selector(
    By.CSS_SELECTOR, "div.exred-triage-form button", type=ElementType.BUTTON
)
SELECTORS = {
    "breadcrumbs": {
        "itself": Selector(By.CSS_SELECTOR, "div.breadcrumbs"),
        "links": Selector(By.CSS_SELECTOR, "div.breadcrumbs a"),
    },
    "support content": {
        "itself": Selector(By.CSS_SELECTOR, "div.container section"),
        "heading": Selector(By.CSS_SELECTOR, "section h1"),
        "content": Selector(By.CSS_SELECTOR, "section p"),
        "submit an enquiry": Selector(
            By.CSS_SELECTOR, "#further-help-link > a", type=ElementType.LINK
        ),
        "resend my code": Selector(
            By.PARTIAL_LINK_TEXT,
            "Resend my code",
            type=ElementType.LINK,
            is_visible=False,
        ),
    },
    "error reporting": {
        "itself": Selector(By.CSS_SELECTOR, "section.error-reporting"),
        "link": Selector(By.ID, "error-reporting-section-contact-us"),
    },
}


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name.lower()] if page_name else URL
    check_url(driver, url, exact_match=False)
    msg = f"Got 404 on {driver.current_url}"
    assert "This page cannot be found" not in driver.page_source, msg
