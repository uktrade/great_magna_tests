 @getting-paid-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Getting Paid Page

  Background:
   Given test authentication is done

    @allure.link:XOT-1017
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Payment methods" section and enter Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Payment Methods" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to enter text at "Payment Methods Notes" on page "Build An Export Plan - Getting Paid"

       @allure.link:XOT-1017
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Payment methods" section and enter Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Payment Terms" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to enter text at "Payment Terms Notes" on page "Build An Export Plan - Getting Paid"

       @allure.link:XOT-1017
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Payment methods" section and enter Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Incoterms" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to enter text at "Incoterms Notes" on page "Build An Export Plan - Getting Paid"


  @allure.link:XOT-1014
   @Great_Magna_Export_Plan
  Scenario:User should be able to click lessons link "Manage Exchange Rates"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to click on section "Manage Exchange Rates" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should be on the "LearnToExport - Manage Exchange Rates" page
     And "Robert" decides to click on section "Costs And Pricing" on page "LearnToExport - Manage Exchange Rates"

  @allure.link:XOT-1014
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar links

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Funding and Credit"
     And "Robert" decides to click on element "Nav Getting Paid" on page "Build An Export Plan - Funding and Credit"
     And "Robert" should be on the "Build An Export Plan - Getting Paid" Page

@allure.link:XOT-1015
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Getting Paid" next page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Funding and Credit"

@allure.link:XOT-1016
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Funding and Credit"
