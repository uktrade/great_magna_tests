#@domestic
#@ukef
#@allure.suite:Domestic
#Feature: Domestic - UK Export Finance page & contact-us form
#
#  Background:
#    Given test authentication is done
#
#
#  @allure.link:TT-585
#   @ukef_1
#  Scenario: Any Exporter should see the all expected sections on the "UKEF Trade Finance" page
#    Given "Robert" visits the "Domestic - Trade Finance" page
#
#    Then "Robert" should see following sections
#      | Sections                    |
#      | Breadcrumbs                 |
#      | Hero                        |
#      | Tell us about your business |
#      | Advantages                  |
#      | Video                       |
#      | Contact us                  |
#      | Error Reporting             |
#
#
#  @allure.link:TT-585
#  @video
#  @skip-in-firefox
#  Scenario: Any Exporter should be able to watch promotional video on the "UKEF Trade Finance" page
#    Given "Robert" visits the "Domestic - Trade Finance" page
#
#    When "Robert" decides to watch "6" seconds of the promotional video
#
#    Then "Robert" should be able to watch at least first "5" seconds of the promotional video
#
#
#  @allure.link:TT-585
#  Scenario: Any Exporter should be able to get to "Finance Advice" page from the "UKEF Trade Finance" page
#    Given "Robert" visits the "Domestic - Trade Finance" page
#
#    When "Robert" decides to "Read more about getting money to grow your business"
#
#    Then "Robert" should be on the "Domestic - Advice article list" page
#
#
#  @allure.link:TT-585
#  Scenario Outline: Any Exporter should be able to navigate to "Domestic - <expected>" page using "<breadcrumb>" on the "UKEF Trade Finance" page
#    Given "Robert" visits the "Domestic - Trade Finance" page
#
#    When "Robert" decides to click on "<breadcrumb>"
#
#    Then "Robert" should be on the "Domestic - <expected>" page if not be redirected to "International - Landing" page
#
#    Examples: Breadcrumbs
#      | breadcrumb   | expected    |
#      | great.gov.uk | Home        |
#      | UKEF         | Get Finance |
#
#
#  @allure.link:TT-585
#  Scenario: Any Exporter should be able to get to the "Contact UKEF" form from "Domestic - Trade Finance"
#    Given "Robert" visits the "Domestic - Trade Finance" page
#
#    When "Robert" decides to "Tell us about your business"
#
#    Then "Robert" should be on the "Domestic - Your details - UKEF Contact us" page
#    And "Robert" should see following sections
#      | Sections        |
#      | Breadcrumbs     |
#      | Form            |
#      | Error Reporting |
#
#
#  @allure.link:TT-585
#  @captcha
#  @dev-only
#  Scenario: Any Exporter should be able to contact UKEF team by submitting the "Check your eligibility" form
#    Given "Robert" visits the "Domestic - Your details - UKEF Contact us" page
#
#    When "Robert" fills out and submits the form
#    Then "Robert" should be on the "Domestic - Company details - UKEF Contact us" page
#
#    When "Robert" fills out and submits the form
#    Then "Robert" should be on the "Domestic - Tell us how we can help - UKEF Contact us" page
#
#    When "Robert" fills out and submits the form
#    Then "Robert" should be on the "Domestic - Thank you - UKEF Contact us" page
#
#
#  @allure.link:TT-585
#  @captcha
#  @dev-only
#  Scenario: Any Exporter should not be able to submit "Check you eligibility" form without filling out all required fields
#    Given "Robert" visits the "Domestic - Your details - UKEF Contact us" page
#    When "Robert" submits the form
#    Then "Robert" should be on the "Domestic - Your details - UKEF Contact us" page
#    And "Robert" should see error message saying that mandatory fields are required
#
#    When "Robert" fills out and submits the form
#    Then "Robert" should be on the "Domestic - Company details - UKEF Contact us" page
#    When "Robert" submits the form
#    Then "Robert" should be on the "Domestic - Company details - UKEF Contact us" page
#    And "Robert" should see error message saying that mandatory fields are required
#
#    When "Robert" fills out and submits the form
#    Then "Robert" should be on the "Domestic - Tell us how we can help - UKEF Contact us" page
#    When "Robert" submits the form
#    Then "Robert" should be on the "Domestic - Tell us how we can help - UKEF Contact us" page
#    And "Robert" should see error message saying that mandatory fields are required
#
#    When "Robert" fills out and submits the form
#    Then "Robert" should be on the "Domestic - Thank you - UKEF Contact us" page
