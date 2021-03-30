@navigation-bar-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Export plan Navigation Bar
   Background:
   Given test authentication is done

   @allure.link:XOT-1010
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar links

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - About your Business"
     And "Robert" decides to click on element "Nav Business Objectives" on page "Build An Export Plan - About your Business"
     And "Robert" should be on the "Build An Export Plan - Business Objectives" Page