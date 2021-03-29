 @costs-and-pricing-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Costs And Pricing Page

   Background:
   Given test authentication is done

  @allure.link:XOT-1014
   @GGreat_Magna_Export_Plan
  Scenario: User should be able to click on navigation bar links

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to click on element "Nav Adaptation For Your Target Market" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should be on the "Build An Export Plan - Adaptation For Your Target Market" Page

@allure.link:XOT-1015
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on "Funding and Credit" next page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Costs And Pricing"

@allure.link:XOT-1016
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Costs And Pricing"

    @allure.link:XOT-1017
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on "No. of units and time" section and select random units and time

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to enter value in "Number of units" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to select random item for "Number of units" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to enter value in "Time frame" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to select random item for "Time Frame" on page "Build An Export Plan - Costs And Pricing"


@allure.link:XOT-1002
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "Direct costs"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Product Cost educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Labour Cost educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" enters direct costs price on page "Build An Export Plan - Costs And Pricing"
          | Productcost  | Labourcost    | Additionalmargin |
          |     600      |      35       |         25       |

    #And "Robert" decides to validate entered text at "Insurance certificate" on page "Build An Export Plan - Adaptation For Your Target Market"

   @allure.link:XOT-1002
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "Overhead costs"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Product Adaptation educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Freight and Logistics educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Agent and Distribution fees educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Marketing educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Insurance educational" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" enters overhead costs price on page "Build An Export Plan - Costs And Pricing"
          | Product Adaptation  | Freight and Logistics | Agent and Distribution fees | Marketing | Insurance |
          |        210          |          35           |            44               |     55    |     66    |

    And "Robert" decides to validate entered text at "Insurance certificate" on page "Build An Export Plan - Adaptation For Your Target Market"


   @allure.link:XOT-1002
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "your net price","Local taxes" and "Duty per unit" value

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Net Price educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Net Price example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Net Price" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local Taxes educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local taxes example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Local taxes" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Duty educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Duty" on page "Build An Export Plan - Costs And Pricing"

 @allure.link:XOT-1002
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "your net price","Local taxes" and "Duty per unit" value

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Net Price educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Net Price example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Net Price" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local Taxes educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local taxes example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Local taxes" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Duty educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Duty" on page "Build An Export Plan - Costs And Pricing"

 @allure.link:XOT-1002
   @Great_Magna_Export_Plan
  Scenario:User should be able to "select currency" and enter invoicing currency

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on section "Manage Exchange Rates" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" should be on the "LearnToExport - Manage Exchange Rates" page
    And "Robert" decides to click on section "Costs And Pricing" on page "LearnToExport - Manage Exchange Rates"
    And "Robert" decides to select random item for "Select Currency" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Gross Price per unit" on page "Build An Export Plan - Costs And Pricing"
