# -*- coding: utf-8 -*-
from enum import Enum, unique
from functools import partial
from typing import Union
from urllib.parse import urljoin

from .settings import (
    GREAT_MAGNA_URL,
    SSO_URL,
    SSO_API_URL,
)


class Url:
    def __init__(
            self, service_url: str, relative_endpoint: str, *, template: str = None
    ):
        join_endpoint = partial(urljoin, service_url)
        self.relative: str = relative_endpoint
        self.absolute: str = join_endpoint(relative_endpoint)
        self.template: Union[str, None] = template
        self.absolute_template: Union[str, None] = (
            join_endpoint(template) if template else None
        )


class GreatMagnaUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(GREAT_MAGNA_URL, endpoint, template=template)


class SSOUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(SSO_URL, endpoint, template=template)


class SSOApiUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(SSO_API_URL, endpoint, template=template)


@unique
class URLs(Enum):
    """This Enum is to help discover, refactor, find usage of URLs"""

    def __str__(self) -> str:
        return (
            f"{self._name_} absolute URL: {self.value.absolute} relative "
            f"URL: {self.value.relative}"
        )

    @property
    def absolute(self) -> str:
        return self.value.absolute

    @property
    def relative(self) -> str:
        return self.value.relative

    @property
    def template(self) -> Union[str, None]:
        return self.value.template

    @property
    def absolute_template(self) -> Union[str, None]:
        return self.value.absolute_template

    # SSO UI
    SSO_LANDING = SSOUrl("")
    SSO_EMAIL_CONFIRM = SSOUrl("accounts/confirm-email/")
    SSO_INACTIVE = SSOUrl("accounts/inactive/")
    SSO_LOGIN = SSOUrl("accounts/login/", template="accounts/login/?next={next}")
    SSO_LOGOUT = SSOUrl("accounts/logout/")
    SSO_PASSWORD_CHANGE = SSOUrl("accounts/password/change/")
    SSO_PASSWORD_RESET = SSOUrl("accounts/password/reset/")
    SSO_PASSWORD_SET = SSOUrl("accounts/password/set/")
    SSO_SIGNUP = SSOUrl("accounts/signup/")

    # SSO API
    SSO_API_LANDING = SSOApiUrl("")
    SSO_API_HEALTHCECK = SSOApiUrl("api/v1/healthcheck/")
    SSO_API_HEALTHCHECK_PING = SSOApiUrl("api/v1/healthcheck/ping/")
    SSO_API_USER = SSOApiUrl("api/v1/session-user/")

    # Great Magna Pages
    GREAT_MAGNA_START = GreatMagnaUrl("")
    GREAT_MAGNA_SIGNUP = GreatMagnaUrl("signup/")
    GREAT_MAGNA_LOGIN = GreatMagnaUrl("login/")
    GREAT_MAGNA_FORGOTTEN_PASSWORD = GreatMagnaUrl("https://great.staging.uktrade.digital/sso/accounts/password/reset/")
    GREAT_MAGNA_LEARN_TO_EXPORT = GreatMagnaUrl("learn/categories/")
    GREAT_MAGNA_SEARCH = GreatMagnaUrl("search/")
    GREAT_MAGNA_DASHBOARD = GreatMagnaUrl("dashboard/")
    GREAT_MAGNA_SHOW_ME_AROUND = GreatMagnaUrl("dashboard/")
    GREAT_MAGNA_SIGN_OUT = GreatMagnaUrl("dashboard/")
    GREAT_MAGNA_PROFILE_ABOUT = GreatMagnaUrl("profile/about/")
    GREAT_MAGNA_CONTACT_US = GreatMagnaUrl("contact-us/help/")

    GREAT_MAGNA_WHERE_TO_EXPORT = GreatMagnaUrl("where-to-export/")

    GREAT_MAGNA_LESSONS_GET_STARTED = GreatMagnaUrl("learn/categories/getting-started/")
    GREAT_MAGNA_LESSONS_INTRODUCTION_TO_LESSONS_AND_LEARNING = GreatMagnaUrl(
        "learn/categories/getting-started/lesson-basics/introduction-lessons-and-learning/")
    GREAT_MAGNA_LESSONS_NEW_LESSON_ADDED = GreatMagnaUrl(
        "learn/categories/getting-started/new-topic-added/new-lesson-added/")
    GREAT_MAGNA_LESSONS_HOW_LESSONS_CAN_HELP = GreatMagnaUrl(
        "learn/categories/getting-started/introduction-learning/how-lessons-can-help-you-make-export-plan/")


    GREAT_MAGNA_LESSONS_IDENTIFY_OPPORTUNITIES_AND_RESEARCH_THE_MARKET = GreatMagnaUrl(
        "learn/categories/market-research/")
    GREAT_MAGNA_LESSONS_CHOOSING_THE_RIGHT_OPPORTUNITIES = GreatMagnaUrl(
        "learn/categories/market-research/evaluate-opportunities/opportunity-right-you/")
    GREAT_MAGNA_LESSONS_MOVE_FROM_ACCIDENTAL_EXPORTING_TO_STRATEGIC_EXPORTING = GreatMagnaUrl(
        "learn/categories/market-research/evaluate-opportunities/move-accidental-exporting-strategic-exporting/")
    GREAT_MAGNA_LESSONS_IN_MARKET_RESEARCH = GreatMagnaUrl(
        "learn/categories/market-research/market-research-approaches/-market-research/")
    GREAT_MAGNA_LESSONS_QUANTIFY_CUSTOMER_DEMAND_HOW_MUCH_YOU_MIGHT_SELL = GreatMagnaUrl(
        "learn/categories/market-research/calculate-customer-demand/quantifying-customer-demand-how-much-might-you-sell/")
    GREAT_MAGNA_LESSONS_USING_WHAT_YOU_KNOW = GreatMagnaUrl(
        "/learn/categories/market-research/calculate-customer-demand/using-what-you-know-to-help-inform-your-positioning-and-competitive-advantage/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_MARKET_TRENDS = GreatMagnaUrl(
        "/learn/categories/market-research/calculate-customer-demand/understand-market-trends/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_MARKET_BARRIERS = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/understand-market-barriers/")
    GREAT_MAGNA_LESSONS_HOW_TO_ASSESS_EASE_OF_ENTRY_INTO_A_NEW_MARKET = GreatMagnaUrl(
        "learn/categories/market -research/research-countries-and-choose-destination-markets/how-assess-ease-entry-new-market/")
    GREAT_MAGNA_LESSONS_LOCAL_INFRASTRUCTURE = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/local-infrastructure/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_HOW_YOU_MAY_NEED_TO_ADAPT_YOUR_PRODUCT_TO_MEET_INTERNATIONAL_STANDARDS = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/understand-how-you-may-need-adapt-your-product-meet-international-standards/")
    GREAT_MAGNA_LESSONS_INFORMATION_YOU_NEED_TO_CHOOSE_A_TARGET_COUNTRY = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/information-you-need-choose-target-country/")

    GREAT_MAGNA_LESSONS_PREPARE_TO_SELL_INTO_A_NEW_COUNTRY = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/")
    GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_ROUTE_TO_MARKET = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/choose-right-route-market/")
    GREAT_MAGNA_LESSONS_SELL_DIRECT_TO_YOUR_CUSTOMER = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/sell-direct-your-customer/")
    GREAT_MAGNA_LESSONS_SELL_WITH_INTERNATIONAL_E_COMMERCE = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/international-e-commerce/")
    GREAT_MAGNA_LESSONS_SET_UP_JOINT_VENTURES_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/set-joint-ventures-abroad/")
    GREAT_MAGNA_LESSONS_SETTING_UP_A_FRANCHISE_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/setting-franchise-abroad/")
    GREAT_MAGNA_LESSONS_DECIDE_WHETHER_TO_USE_LICENSING = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/decide-whether-use-licensing/")
    GREAT_MAGNA_LESSONS_HOW_TO_SET_UP_A_BUSINESS_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/how-set-business-abroad/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_THE_LOCAL_BUSINESS_CULTURE_IN_YOUR_TARGET_MARKET = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/different-ways-of-doing-business-across-borders/understand-local-business-culture-your-target-market/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_PRODUCT_LIABILITY = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/manage-intellectual-property-and-legal-protection-risk/understanding-product-liability/")
    GREAT_MAGNA_LESSONS_PROTECT_YOUR_INTELLECTUAL_PROPERTY_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/manage-intellectual-property-and-legal-protection-risk/protect-your-intellectual-property-abroad/")
    GREAT_MAGNA_LESSONS_HOW_TO_PREPARE_FOR_A_TRADE_MISSION = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-events/how-prepare-trade-mission/")
    GREAT_MAGNA_LESSONS_HOW_TO_PREPARE_FOR_A_TRADE_SHOW_AS_AN_ATTENDEE = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-events/how-prepare-trade-show-attendee/")
    GREAT_MAGNA_LESSONS_HOW_TO_PREPARE_FOR_A_TRADE_SHOW_AS_AN_EXHIBITOR = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-events/how-prepare-trade-show-exhibitor/")
    GREAT_MAGNA_LESSONS_HOW_TO_ADAPT_YOUR_WEBSITE_FOR_AN_INTERNATIONAL_AUDIENCE = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-online/how-adapt-your-website-international-audience/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_DIGITAL_MARKETING = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-online/understand-digital-marketing/")
    GREAT_MAGNA_LESSONS_PROTECT_YOUR_BUSINESS_FROM_BRIBERY_AND_CORRUPTION = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/managing-safety-corruption-and-business-integrity-risk/protect-your-business-bribery-and-corruption/")
    GREAT_MAGNA_LESSONS_OPERATING_WITH_BUSINESS_INTEGRITY = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/managing-safety-corruption-and-business-integrity-risk/operating-business-integrity/")
    GREAT_MAGNA_LESSONS_PROTECT_YOUR_DATA_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/managing-safety-corruption-and-business-integrity-risk/protect-your-data-abroad/")
    GREAT_MAGNA_HOW_TO_DRAFT_A_CONTRACT = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/winning-bids-and-expansion/how-draft-contract/")

    GREAT_MAGNA_LESSONS_REGULATIONS_LICENSING_AND_LOGISTICS = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/")
    GREAT_MAGNA_LESSONS_HOW_TO_ADAPT_YOUR_LABELLING_AND_PACKAGING = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-goods-into-the-destination-country/labelling-and-packaging/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_DUTIES_AND_TAXES = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-goods-into-the-destination-country/understand-duties-and-taxes/")
    GREAT_MAGNA_LESSONS_CHOOSE_WHICH_INCOTERMS_ARE_RIGHT_FOR_YOU = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/logistics-and-freight-forwarders/incoterms/")
    GREAT_MAGNA_LESSONS_FREIGHT_FORWARDERS = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/logistics-and-freight-forwarders/freight-forwarders/")
    GREAT_MAGNA_LESSONS_REGULATIONS_AROUND_E_COMMERCE = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/understand-services-rules-and-regulations/regulations-around-e-commerce/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_REGULATIONS_AROUND_SUPPLYING_A_SERVICE = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/understand-services-rules-and-regulations/understand-regulations-around-supplying-service/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_DATA_REGULATIONS_AND_DATA_PROTECTION = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/understand-services-rules-and-regulations/understand-data-regulations-and-data-protection/")

    GREAT_MAGNA_LESSONS_FUNDING_FINANCE_AND_GETTING_PAID = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/")
    GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_FUNDING_AND_CREDIT_OPTIONS = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/manage-cash-flow/funding-and-credit-options-doing-business-across-borders/")
    GREAT_MAGNA_LESSONS_HOW_TO_AVOID_CASHFLOW_CHALLENGES_WHEN_EXPORTING = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/manage-cash-flow/how-avoid-cashflow-challenges-when-exporting/")
    GREAT_MAGNA_LESSONS_HOW_TO_INSURE_AGAINST_NON_PAYMENT = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/insure-against-non-payment/")
    GREAT_MAGNA_LESSONS_HOW_TO_CREATE_AN_EXPORT_INVOICE = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/how-create-export-invoice/")
    GREAT_MAGNA_LESSONS_DECIDE_WHEN_TO_GET_PAID = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/decide-when-get-paid-export-orders/")
    GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_PAYMENT_METHOD = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/payment-methods-exporters/")
    GREAT_MAGNA_LESSONS_HOW_TO_MANAGE_EXCHANGE_RATES = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/exchange-rates-and-moving-money/managing-exchange-rates/")

    GREAT_MAGNA_EXPORT_PLAN_DASHBOARD = GreatMagnaUrl("export-plan/dashboard/")
    GREAT_MAGNA_UPLOAD_LOGO = GreatMagnaUrl("export-plan/logo")
    GREAT_MAGNA_EXPORT_PLAN_ABOUT_YOUR_BUSINESS = GreatMagnaUrl(
        "export-plan/section/about-your-business/")
    GREAT_MAGNA_EXPORT_PLAN_BUSINESS_OBJECTIVES = GreatMagnaUrl(
        "export-plan/section/business-objectives/")
    GREAT_MAGNA_EXPORT_PLAN_MARKETING_APPROACH = GreatMagnaUrl(
        "export-plan/section/marketing-approach/")
    GREAT_MAGNA_EXPORT_PLAN_TARGET_MARKET_RESEARCH = GreatMagnaUrl(
        "export-plan/section/target-markets-research/")
    GREAT_MAGNA_EXPORT_PLAN_ADAPTATION_FOR_YOUR_TARGET_MARKET = GreatMagnaUrl(
        "export-plan/section/adaptation-for-your-target-market/")
    GREAT_MAGNA_EXPORT_PLAN_COSTS_AND_PRICING = GreatMagnaUrl(
        "export-plan/section/costs-and-pricing/")
    GREAT_MAGNA_EXPORT_PLAN_FUNDING_AND_CREDIT = GreatMagnaUrl(
        "export-plan/section/funding-and-credit/")
    GREAT_MAGNA_EXPORT_PLAN_GETTING_PAID = GreatMagnaUrl(
        "export-plan/section/getting-paid/")
    GREAT_MAGNA_EXPORT_PLAN_TRAVEL_PLAN = GreatMagnaUrl(
        "export-plan/section/travel-and-business-policies/")
    GREAT_MAGNA_EXPORT_PLAN_BUSINESS_RISK = GreatMagnaUrl(
        "export-plan/section/business-risk/")
