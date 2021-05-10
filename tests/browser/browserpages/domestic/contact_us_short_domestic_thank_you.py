# -*- coding: utf-8 -*-
"""Domestic - Short Domestic Contact us - Thank you for your enquiry."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages.common_actions import Selector, check_url

NAME = "Thank you for your enquiry"
NAMES = [
    "Thank you for your enquiry",
    "Thank you for your enquiry (Events)",
    "Thank you for your enquiry (Defence and Security Organisation (DSO))",
    "Thank you for your enquiry (Other)",
    "Thank you for your enquiry (I haven't had a response from the opportunity I applied for)",
    "Thank you for your enquiry (My daily alerts are not relevant to me)",
    "Thank you for your enquiry (I have not received an email confirmation)",
    "Thank you for your enquiry (I need to reset my password)",
    "Thank you for your enquiry (My Companies House login is not working)",
    "Thank you for your enquiry (I do not know where to enter my verification code)",
    "Thank you for your enquiry (I have not received my letter containing the verification code)",
    "Thank you for your enquiry (I have not received a verification code)",
]
SERVICE = Service.DOMESTIC
TYPE = PageType.SHORT_DOMESTIC_CONTACT_US
URL = URLs.CONTACT_US_FORM_DOMESTIC_SUCCESS.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

PDF_LINKS = Selector(By.CSS_SELECTOR, "#documents-section a.link")
SELECTORS = {
    "confirmation": {
        "itself": Selector(By.ID, "confirmation-section"),
        "heading": Selector(
            By.CSS_SELECTOR, "#confirmation-section div.heading-container"
        ),
    },
    "what happens next": {
        "itself": Selector(By.ID, "next-container"),
        "heading": Selector(By.CSS_SELECTOR, "#next-container h2"),
        "text": Selector(By.CSS_SELECTOR, "#next-container p"),
        "continue to great.gov.uk": Selector(By.CSS_SELECTOR, "#next-container a"),
    },
    "report this page": {
        "self": Selector(By.CSS_SELECTOR, "section.error-reporting"),
        "report link": Selector(By.CSS_SELECTOR, "section.error-reporting a"),
    },
}
url_template = URLs.CONTACT_US_DOMESTIC_SUCCESS.absolute_template
SubURLs = {
    "thank you for your enquiry": URL,
    "thank you for your enquiry (events)": url_template.format(page="events"),
    "thank you for your enquiry (defence and security organisation (dso))": url_template.format(
        page="defence-and-security-organisation"
    ),
    "thank you for your enquiry (other)": URL,
    "thank you for your enquiry (i haven't had a response from the opportunity i applied for)": URL,
    "thank you for your enquiry (my daily alerts are not relevant to me)": URL,
    "thank you for your enquiry (i have not received an email confirmation)": URL,
    "thank you for your enquiry (i need to reset my password)": URL,
    "thank you for your enquiry (my companies house login is not working)": URL,
    "thank you for your enquiry (i do not know where to enter my verification code)": URL,
    "thank you for your enquiry (i have not received my letter containing the verification code)": URL,
    "thank you for your enquiry (i have not received a verification code)": URL,
}


def should_be_here(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name.lower()] if page_name else URL
    check_url(driver, url, exact_match=True)
