 @where-to-export-page
@allure.suite:Great_Magna_Export_Plan

Feature: GreatMagna - Where To Export Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario Outline:User should be able to "Add place" and " Add Country"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
     And "Robert" decides to enter product name "Coffee" on page "Where To Export - Compare Countries"
    Examples: product name
      | product |
      | Coffee   |