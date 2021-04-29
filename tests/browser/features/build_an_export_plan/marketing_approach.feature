@marketing-approach-page
@allure.suite:Great_Magna_Export_Plan_M_A
Feature: GreatMagna - Marketing approach Page
 Background:
   Given test authentication is done


  @allure.link:XOT-1017
   @Great_Magna_Export_Plan_B_O_D_1_123
  Scenario:User should be able to click on "Route to market" section and select random "route" and "how will you promote product"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Add route to market" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to select random item for "Route to market" on page "Build An Export Plan - Marketing approach"

#   @allure.link:XOT-1002
#   @Great_Magna_Export_Plan_B_O
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to click on "Add goal" and enter the objectives for exporting
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#   #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" fill business objective details on page "Build An Export Plan - Business Objectives"
#          | Position | Startdate  | Enddate    | Objectives | Owner        | PlannedReviews   |
#          | 1     | 01/02/2021 | 01/02/2028 | obj1       | obj1-owner   | obj1-plannedreviews |
#          | 2     | 01/02/2021 | 01/02/2028 | obj2       | obj2-owner   | obj2-plannedreviews |
#          | 3     | 01/02/2021 | 01/02/2028 | obj3       | obj3-owner   | obj3-plannedreviews |
#          | 4     | 01/02/2021 | 01/02/2028 | obj4       | obj4-owner   | obj4-plannedreviews |
#          | 5     | 01/02/2021 | 01/02/2028 | obj5       | obj5-owner   | obj5-plannedreviews |

  @allure.link:XOT-1003
     @Great_Magna_Export_Plan
   @Great_Magna_Export_Plan_B_O_D_1_123
   Scenario:User should be able to delete Route to market

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
     Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to delete route to market on page "Build An Export Plan - Marketing approach"
          | Position |
          | 5    |
          | 4    |
          | 3    |
          | 2    |
          | 1    |

   @allure.link:XOT-1014
   @Great_Magna_Export_Plan
  Scenario:User should be able to click lessons link "Selling direct to your customer"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "What Marketing resources example" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on section "Selling direct to your customer" on page "Build An Export Plan - Marketing approach"
     And "Robert" should be on the "LearnToExport - Selling direct to your customer" page
     And "Robert" decides to click on section "Marketing approach" on page "LearnToExport - Selling direct to your customer"

#   @allure.link:XOT-1021
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to view Marketing approach pages
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "open" on page "Build An Export Plan - Marketing approach"
#     And "Robert" decides to click on element "0-14 year olds" on page "Build An Export Plan - Marketing approach"
#     And "Robert" decides to click on element "confirm" on page "Build An Export Plan - Marketing approach"

   @allure.link:XOT-1014
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Costs and pricing" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Marketing approach"
     And "Robert" decides to click on element "Nav Costs And Pricing" on page "Build An Export Plan - Marketing approach"
     And "Robert" should be on the "Build An Export Plan - Costs And Pricing" Page

   @allure.link:XOT-1015
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on page "Costs And Pricing link" at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - Marketing approach"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Marketing approach"
    And "Robert" should be on the "Build An Export Plan - Costs And Pricing" page

   @allure.link:XOT-1016
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Marketing approach"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page



  @allure.link:XOT-1016
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Top Export plan home in Marketing approach and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Marketing approach"
      And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

  @allure.link:XOT-031
  @Great-Magna-Sign-Up
  Scenario Outline: New User should be able to navigate to Export Plan and click on "Travel Plan" Page and enter the "Add Product"

  Given "Robert" visited "GreatMagna - Sign Up" page
  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
  Then "Robert" should be on the "GreatMagna - Dashboard" Page
  Examples: email address and password
     |      emailaddress                 | password    |
     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
  And "Robert" decides to click on "Build an export plan"
  And "Robert" "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
  And "Robert" decides to enter product name "Chair" on page "Build An Export Plan - Marketing approach"
  And "Robert" decides to enter country name "Brazil" on the "Build An Export Plan - Marketing approach" page

    @allure.link:XOT-1002
   @Great_Magna_Export_Plan_115
  Scenario:User should be able to click on "Add route to market" on Marketing approach page and click on dashboard should see "Marketing approach" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Marketing approach" Page
    And "Robert" decides to click on element "Add route to market" on page "Build An Export Plan - Marketing approach"
   And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Marketing approach"
     And "Robert" should see "Marketing approach" text under section "Export Plan" on page "GreatMagna - Dashboard"
