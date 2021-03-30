@travel-plan-page
@allure.suite:Great_Magna_Export_Plan

Feature: GreatMagna - Travel Plan Page
   Background:
   Given test authentication is done
   @beta
   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Travel plan" and click Back button

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on element "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
    And "Robert" decides to click on element "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "ok Button" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
