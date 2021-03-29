 @funding-and-credit-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Funding and Credit Page

   Background:
   Given test authentication is done


         @allure.link:XOT-1017
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "How much funding you need"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to enter value in "How much funding" on page "Build An Export Plan - Funding and Credit"


       @allure.link:XOT-1017
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Add a funding option" and select random option and enter value

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Funding and Credit"
#    And "Robert" decides to click on section "Choose the right funding and Credit Options" on page "Build An Export Plan - Funding and Credit"
#    And "Robert" should be on the "LearnToExport - Choose the right funding and Credit Options" page

     And "Robert" decides to select random funding options on page "Build An Export Plan - Funding and Credit"
          | Position | Amount  |
          | 1        | 5000    |
          | 2        | 1000    |
#          | 3        | 12000   |
#          | 4        | 25000   |
#          | 5        | 35000   |

     #And "Robert" decides to select random item for "Time Frame" on page "Build An Export Plan - Costs And Pricing"


  @allure.link:XOT-1014
   @Great_Magna_Export_Plan
  Scenario:User should be able to click lessons link "Avoid cashflow challenges when exporting"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to click on section "Avoid cashflow challenges when exporting" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should be on the "LearnToExport - Avoid cashflow challenges when exporting" page
     And "Robert" decides to click on section "Costs And Pricing" on page "LearnToExport - Avoid cashflow challenges when exporting"

      @allure.link:XOT-1014
   @Great_Magna_Export_Plan
  Scenario:User should be able to click lessons link "Choose the right funding and credit options"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to click on section "Choose the right funding" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should be on the "LearnToExport - Choose the right funding" page
     And "Robert" decides to click on section "Costs And Pricing" on page "LearnToExport - Choose the right funding"

  @allure.link:XOT-1014
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar links

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
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
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Funding and Credit"

@allure.link:XOT-1016
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Funding and Credit"
