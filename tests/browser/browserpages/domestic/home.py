# -*- coding: utf-8 -*-
"""Domestic Home Page Object."""
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
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_url,
    find_element,
    find_elements,
    go_to_url,
    pick_option,
    submit_form,
    take_screenshot,
    wait_for_page_load_after_action,
)
from browserpages.domestic import actions as domestic_actions, markets_listing

NAME = "Home"
SERVICE = Service.DOMESTIC
TYPE = PageType.HOME
URL = URLs.DOMESTIC_LANDING_UK.absolute
PAGE_TITLE = "Welcome to great.gov.uk"

PROMO_VIDEO = Selector(By.CSS_SELECTOR, "div.video-container.Modal-Container video")
CLOSE_VIDEO = Selector(By.ID, "campaign-section-videoplayer-close")
VIDEO_MODAL_WINDOW = Selector(
    By.CSS_SELECTOR, "body > div.video-container.Modal-Container.open"
)
ARTICLES = Selector(By.CSS_SELECTOR, "#eu-exit-news-section .article a")
ADVICE_ARTICLE_LINKS = Selector(By.CSS_SELECTOR, "#resource-advice a")
SIGN_IN_REQUIRED_LINKS = Selector(
    By.CSS_SELECTOR, "#article-list-page li.article a", type=ElementType.LINK
)
SELECTORS = {
    "find new markets": {
        "find new markets section": Selector(
            By.CSS_SELECTOR, "section.sector-potential-section div.padding-bottom-45-m"
        ),
        "select your sector": Selector(By.ID, "id_sector", type=ElementType.SELECT),
        "show markets": Selector(
            By.ID, "sector-submit", type=ElementType.SUBMIT, next_page=markets_listing,
        ),
        "sector selector quick links": Selector(
            By.CSS_SELECTOR, "div.sector-selector-quick-links ul li a"
        ),
        "view all market guides": Selector(
            By.CSS_SELECTOR, "section.sector-potential-section a.view-markets"
        ),
    },
    "how dit helps": {
        "how dit helps section": Selector(
            By.CSS_SELECTOR, "div.sector-selector-quick-links"
        ),
        "how dit helps links": Selector(
            By.CSS_SELECTOR, "div.sector-selector-quick-links a"
        ),
        "how dit helps link images": Selector(
            By.CSS_SELECTOR, "div.sector-selector-quick-links a img"
        ),
    },
    "export goods from the uk": {
        "export goods from the uk section": Selector(
            By.CSS_SELECTOR, "section.export-goods-from-uk"
        ),
        "exporting goods from the uk": Selector(
            By.CSS_SELECTOR, "section.export-goods-from-uk a"
        ),
    },
    "what's new": {
        "what's new section": Selector(
            By.CSS_SELECTOR, "section.padding-bottom-45:not(.export-goods-from-uk)"
        ),
        "what's new section heading": Selector(
            By.CSS_SELECTOR, "section.padding-bottom-45:not(.export-goods-from-uk) h2"
        ),
        "what's new image heading": Selector(
            By.CSS_SELECTOR,
            "section.padding-bottom-45:not(.export-goods-from-uk) h3.campaign-heading",
        ),
        "watch video": Selector(
            By.ID, "hero-campaign-section-watch-video-button", type=ElementType.LINK
        ),
        "what's new links": Selector(
            By.CSS_SELECTOR,
            "section.padding-bottom-45:not(.export-goods-from-uk) a.card-link",
            type=ElementType.LINK,
        ),
    },
    "sign in required": {
        "learn to export": Selector(
            By.CSS_SELECTOR, "#content > section.padding-bottom-15.padding-bottom-30-m.padding-top-45.padding-top-60-m > div > div > div:nth-child(1) > div > a > div > span"
        ),
        "where to export": Selector(
            By.CSS_SELECTOR, "#content > section.padding-bottom-15.padding-bottom-30-m.padding-top-45.padding-top-60-m > div > div > div:nth-child(2) > div > a > div > span"
        ),
        "make an export plan": Selector(
            By.CSS_SELECTOR,
            "#content > section.padding-bottom-15.padding-bottom-30-m.padding-top-45.padding-top-60-m > div > div > div:nth-child(3) > div > a > div > span",
        ),
    }
}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.DOMESTIC_HERO_WITH_LINK)
SELECTORS.update(common_selectors.COOKIE_BANNER)
SELECTORS.update(common_selectors.SSO_LOGGED_OUT)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def should_see_link_to(driver: WebDriver, section: str, item_name: str):
    item_selector = SELECTORS[section.lower()][item_name.lower()]
    menu_item = find_element(driver, item_selector, element_name=item_name)
    with assertion_msg(
        "It looks like '%s' in '%s' section is not visible", item_name, section
    ):
        assert menu_item.is_displayed()


def open(driver: WebDriver, group: str, element: str):
    selector = SELECTORS[group.lower()][element.lower()]
    link = find_element(driver, selector, element_name=element, wait_for_it=True)
    check_if_element_is_visible(link, element_name=element)
    link.click()
    take_screenshot(driver, NAME + " after clicking on: %s link".format(element))


def play_video(driver: WebDriver, *, play_time: int = 5):
    open(driver, group="what's new", element="watch video")
    video_load_delay = 2
    play_js = f'document.querySelector("{PROMO_VIDEO.value}").play()'
    pause = f'document.querySelector("{PROMO_VIDEO.value}").pause()'
    driver.execute_script(play_js)
    if play_time:
        time.sleep(play_time + video_load_delay)
        driver.execute_script(pause)


def get_video_watch_time(driver: WebDriver) -> int:
    watch_time_js = f'return document.querySelector("{PROMO_VIDEO.value}").currentTime'
    duration_js = f'return document.querySelector("{PROMO_VIDEO.value}").duration'
    watch_time = driver.execute_script(watch_time_js)
    duration = driver.execute_script(duration_js)
    logging.debug(f"Video watch time: {watch_time}")
    logging.debug(f"Video duration : {duration}")
    return int(watch_time)


def close_video(driver: WebDriver):
    take_screenshot(driver, NAME + " before closing video modal window")
    close_button = find_element(driver, CLOSE_VIDEO)
    close_button.click()


def should_not_see_video_modal_window(driver: WebDriver):
    time.sleep(1)
    check_if_element_is_not_present(driver, VIDEO_MODAL_WINDOW)


def open_news_article(driver: WebDriver, article_number: int):
    article_links = find_elements(driver, ARTICLES)
    assert len(article_links) >= article_number
    article_links[article_number - 1].click()


def open_any_article(driver: WebDriver) -> str:
    article_links = find_elements(driver, ADVICE_ARTICLE_LINKS)
    link = random.choice(article_links)
    link_text = link.text
    check_if_element_is_visible(link, element_name=link_text)
    with wait_for_page_load_after_action(driver):
        link.click()
    return link_text


def search(driver: WebDriver, phrase: str):
    domestic_actions.search(driver, phrase)


def generate_form_details(actor: Actor, *, custom_details: dict = None) -> dict:
    result = {"select your sector": None}

    if custom_details:
        result.update(custom_details)

    logging.debug(f"Generated form details: {result}")
    return result


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["find new markets"]
    pick_option(driver, form_selectors, details)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["find new markets"])
