@marketing-approach-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Marketing approach Page
 Background:
   Given test authentication is done


  @allure.link:XOT-1017
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on "Route to market" section and select random "route" and "how will you promote product"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Add route to market" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to select random item for "Route to market" on page "Build An Export Plan - Marketing approach"


  @allure.link:XOT-1014
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click lessons link "Selling direct to your customer"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "What Marketing resources example" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on section "Selling direct to your customer" on page "Build An Export Plan - Marketing approach"
     And "Robert" should be on the "LearnToExport - Selling direct to your customer" page
     And "Robert" decides to click on section "Marketing approach" on page "LearnToExport - Selling direct to your customer"

   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario:User should be able to view Marketing approach pages

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "open" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on element "0-14 year olds" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on element "confirm" on page "Build An Export Plan - Marketing approach"

 @allure.link:XOT-1014
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar links

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on element "Nav Funding and Credit" on page "Build An Export Plan - Marketing approach"
     And "Robert" should be on the "Build An Export Plan - Funding and Credit" Page

@allure.link:XOT-1015
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on "Costs and Pricing" next page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Marketing approach"

@allure.link:XOT-1016
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Marketing approach"
