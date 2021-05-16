# -*- coding: utf-8 -*-
"""Selectors for various common page components"""
import copy

from great_magna_tests_shared .constants import (
    MD5_CHECKSUM_EIG_LOGO,
    MD5_CHECKSUM_EVENTS_BIG_FOOTER_LOGO,
    MD5_CHECKSUM_EVENTS_BIG_HEADER_LOGO,
    MD5_CHECKSUM_GREAT_LOGO,
    MD5_CHECKSUM_INVEST_IN_GREAT,
)
from browserpages import ElementType
from browserpages.common_actions import By, Selector

DOMESTIC_HERO_WITH_LINK = {
    "hero": {
        "hero banner": Selector(By.ID, "hero"),
        "title": Selector(By.CSS_SELECTOR, "#hero h1"),
        "view export market guides": Selector(
            By.CSS_SELECTOR, "#hero a", type=ElementType.LINK
        ),
    }
}
DOMESTIC_HERO_WO_LINK = {
    "hero": {
        "hero banner": Selector(By.ID, "hero"),
        "title": Selector(By.CSS_SELECTOR, "#hero h1"),
    }
}

DOMESTIC_HEADER = {
    "header": {
        # cookie notice
        "itself": Selector(By.ID, "header-cookie-notice", is_visible=False),
        "find out more about cookies": Selector(
            By.CSS_SELECTOR, "#header-cookie-notice a", is_visible=False
        ),
        # global header
        "global header": Selector(By.ID, "great-global-header"),
        "great global logo": Selector(By.ID, "great-global-header-logo"),
        "for uk businesses": Selector(By.ID, "great-global-header-domestic-link"),
        "for international businesses": Selector(
            By.ID, "great-global-header-international-link"
        ),
        # header menu
        "header menu": Selector(By.CSS_SELECTOR, ".menu"),
        "invest in great logo": Selector(By.ID, "great-header-logo"),
        "advice": Selector(By.ID, "header-advice-desktop", type=ElementType.LINK),
        "markets": Selector(By.ID, "header-markets-desktop", type=ElementType.LINK),
        "services": Selector(By.ID, "header-services-desktop", type=ElementType.LINK),
        "search box": Selector(
            By.ID, "great-header-search-box", type=ElementType.INPUT
        ),
        "search button": Selector(
            By.CSS_SELECTOR,
            "#great-header-search-box ~ button",
            type=ElementType.BUTTON,
        ),
    }
}
COOKIE_BANNER = {
    "cookie banner": {
        "banner": Selector(
            By.CSS_SELECTOR, "div[aria-label='Cookies consent manager']"
        ),
        "accept all cookies": Selector(
            By.CSS_SELECTOR,
            "body > div.ReactModalPortal a[href='#']",
            type=ElementType.LINK,
        ),
        "reject all cookies": Selector(
            By.CSS_SELECTOR,
            "body > div.ReactModalPortal a.button[href$='cookies/']",
            type=ElementType.LINK,
        ),
    }
}
SSO_LOGGED_OUT = {
    "sso links - logged out": {
        "sign in": Selector(By.ID, "header-sign-in-link", is_visible=False)
    }
}

BETA_BAR = {
    "beta bar": {
        "itself": Selector(By.ID, "header-beta-bar"),
        "badge": Selector(By.CSS_SELECTOR, "#header-beta-bar .phase-tag"),
        "message": Selector(By.CSS_SELECTOR, "#header-beta-bar span"),
        "link": Selector(By.CSS_SELECTOR, "#header-beta-bar a"),
    }
}

BREADCRUMBS = {
    "breadcrumbs": {
        "itself": Selector(By.CSS_SELECTOR, ".breadcrumbs"),
        "current page": Selector(
            By.CSS_SELECTOR, ".breadcrumbs li[aria-current='page']"
        ),
        "links": Selector(By.CSS_SELECTOR, ".breadcrumbs a"),
    }
}

ERROR_REPORTING = {
    "error reporting": {
        "itself": Selector(By.CSS_SELECTOR, "section.error-reporting"),
        "report a problem with the page": Selector(
            By.ID, "error-reporting-section-contact-us"
        ),
    }
}

DOMESTIC_FOOTER = {
    "footer": {
        "great footer logo": Selector(By.ID, "great-footer-great-logo"),
        "contact us": Selector(By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(1) > a"),
        "privacy and cookies": Selector(By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(2) > a"),
        "terms and conditions": Selector(By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(3) > a"),
        "performance": Selector(By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(5) > a"),
        "department for international trade on gov.uk": Selector(By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(6) > a"),
        #"go to the page for international businesses": Selector(
            #By.ID, "footer-international"),
        "dit footer logo": Selector(By.ID, "great-global-footer-logo"),
        "copyright notice": Selector(By.ID, "great-footer-copyright"),
    }
}

FAVICON = Selector(By.CSS_SELECTOR, "link[rel='shortcut icon']")
EXOPPS_FAVICON = Selector(By.CSS_SELECTOR, "link[rel='icon']")
EIG_LOGO = Selector(By.CSS_SELECTOR, "#great-header-logo > img")
SIGN_IN_LINK = Selector(By.ID, "header-sign-in-link")

LOGOS = {
    "eig": {"selector": EIG_LOGO, "md5": MD5_CHECKSUM_EIG_LOGO},
    "great - header": {
        "selector": Selector(By.CSS_SELECTOR, "#great-header-logo img"),
        "md5": MD5_CHECKSUM_GREAT_LOGO,
    },
    "great - footer": {
        "selector": Selector(By.ID, "great-footer-great-logo"),
        "md5": MD5_CHECKSUM_GREAT_LOGO,
    },
    "invest in great - header": {
        "selector": Selector(By.CSS_SELECTOR, "#great-header-logo img"),
        "md5": MD5_CHECKSUM_INVEST_IN_GREAT,
    },
    "events business is great - header": {
        "selector": Selector(By.CSS_SELECTOR, "header img"),
        "md5": MD5_CHECKSUM_EVENTS_BIG_HEADER_LOGO,
    },
    "events business is great - footer": {
        "selector": Selector(By.CSS_SELECTOR, "#footer_section img"),
        "md5": MD5_CHECKSUM_EVENTS_BIG_FOOTER_LOGO,
    },
}


INTERNATIONAL_HEADER = {
    "header": {
        # cookie notice
        "itself": Selector(By.ID, "header-cookie-notice", is_visible=False),
        "find out more about cookies": Selector(
            By.CSS_SELECTOR, "#header-cookie-notice a", is_visible=False
        ),
        # global header
        "global header": Selector(By.ID, "great-global-header"),
        "great global logo": Selector(By.ID, "great-global-header-logo"),
        "for uk businesses": Selector(By.ID, "great-global-header-domestic-link"),
        "for international businesses": Selector(
            By.ID, "great-global-header-international-link"
        ),
        # Logo
        "invest in great logo": Selector(By.ID, "great-header-logo"),
        # language selector
        "language selector": Selector(
            By.ID, "great-header-language-select", type=ElementType.SELECT
        ),
        # main menu
        "header menu": Selector(By.CSS_SELECTOR, "div.menu"),
        "about the uk": Selector(By.LINK_TEXT, "About the UK", type=ElementType.LINK),
        "expand to the uk": Selector(
            By.LINK_TEXT, "Expand to the UK", type=ElementType.LINK
        ),
        "invest capital in the uk": Selector(
            By.LINK_TEXT, "Invest capital in the UK", type=ElementType.LINK
        ),
        "buy from the uk": Selector(
            By.LINK_TEXT, "Buy from the UK", type=ElementType.LINK
        ),
        "about us": Selector(By.LINK_TEXT, "About us", type=ElementType.LINK),
    }
}
INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR = copy.deepcopy(INTERNATIONAL_HEADER)
INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR["header"].pop("language selector")

INTERNATIONAL_FOOTER = {
    "footer": {
        "great footer logo": Selector(By.ID, "great-footer-great-logo"),
        "contact us footer": Selector(By.ID, "footer-contact"),
        "privacy and cookies": Selector(By.ID, "footer-privacy-and-cookies"),
        "terms and conditions": Selector(By.ID, "footer-terms-and-conditions"),
        "department for international trade on gov.uk": Selector(By.ID, "footer-dit"),
        "go to the page for uk businesses": Selector(By.ID, "footer-domestic"),
        "dit footer logo": Selector(By.ID, "great-global-footer-logo"),
        "copyright notice": Selector(By.ID, "great-footer-copyright"),
    }
}

INTERNATIONAL_HERO = {
    "hero": {
        "itself": Selector(By.ID, "hero"),
        "heading": Selector(By.CSS_SELECTOR, "#hero h1"),
    }
}


ABOUT_UK_SUBHEADER = {
    "about the uk subheader": {
        "about uk subheader itself": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav",
        ),
        "overview": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav li:nth-child(1) a",
        ),
        "why choose the uk": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav li:nth-child(2) a",
        ),
        "industries": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav li:nth-child(3) a",
        ),
        "regions": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav li:nth-child(4) a",
        ),
        "contact us": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav li:nth-child(5) a",
        ),
    }
}


ABOUT_US_SUBHEADER = {
    "about us subheader": {
        "about us subheader itself": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav",
        ),
        "overview": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav li:nth-child(1) a",
        ),
        "contact us": Selector(
            By.CSS_SELECTOR, "div.great-sub-header > nav li:nth-child(2) a",
        ),
    }
}

FAS_HEADER = {
    "fas header": {
        "fas header itself": Selector(By.CSS_SELECTOR, "nav.sub-nav"),
        "how we help": Selector(By.CSS_SELECTOR, "nav.sub-nav li:nth-child(1) a"),
        "find a supplier": Selector(By.CSS_SELECTOR, "nav.sub-nav li:nth-child(2) a"),
        "contact us": Selector(By.CSS_SELECTOR, "nav.sub-nav li:nth-child(3) a"),
    }
}
