@smoke
@about-your-business-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - About your Business Page
   Background:
   Given test authentication is done

#  @allure.link:XOT-1013
#   @GGreat_Magna_Export_Plan
#  Scenario:User should be able to enter Your product packaging section and enter text and validate
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "About your Business" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Your product packaging example" on page "Build An Export Plan - About Your Business"
#     And "Robert" decides to enter text at "Your product packaging" on page "Build An Export Plan - About Your Business"
#     And "Robert" decides to validate entered text at "Your product packaging" on page "Build An Export Plan - About Your Business"
#


@allure.link:XOT-1015
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on business objective next page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - About Your Business"

@allure.link:XOT-1016
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - About Your Business"


  @allure.link:XOT-1017
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on business performance section and select random turnover

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Your business performance dropdown" on page "Build An Export Plan - About Your business"


#      @allure.link:XOT-1014
#   @GGreat_Magna_Export_Plan
#  Scenario:User should be able to click on navigation bar links
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Costs And Pricing"
#     And "Robert" decides to click on element "Nav Adaptation For Your Target Market" on page "Build An Export Plan - Costs And Pricing"
#     And "Robert" should be on the "Build An Export Plan - Adaptation For Your Target Market" Page
