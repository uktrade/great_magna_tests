@about-your-business-page
@allure.suite:Great_Magna_Export_Plan_A_Y_B_P
Feature: GreatMagna - About your Business Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1010
   @Great_Magna_Export_Plan_A_Y_B_P
     @Great_Magna_Export_Plan
  Scenario:User should be able to view "How you started" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "How you started example" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to click on element "How you started educational" on page "Build An Export Plan - About Your Business"
    And "Robert" decides to enter text at "How you started" on page "Build An Export Plan - About Your Business"
    And "Robert" decides to validate entered text at "How you started" on page "Build An Export Plan - About Your Business"

 @allure.link:XOT-1011
   @Great_Magna_Export_Plan_A_Y_B_P
   @Great_Magna_Export_Plan
  Scenario:User should be able to view  "Where you're based" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Where you're based example" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to enter text at "Where you're based" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to validate entered text at "Where you're based" on page "Build An Export Plan - About Your Business"

@allure.link:XOT-1012
   @Great_Magna_Export_Plan_A_Y_B_P
  @Great_Magna_Export_Plan
  Scenario:User should be able to enter "How you make your products" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "How you make your products example" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to enter text at "How you make your products" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to validate entered text at "How you make your products" on page "Build An Export Plan - About Your Business"
#
  @allure.link:XOT-1013
   @Great_Magna_Export_Plan_A_Y_B_P
    @Great_Magna_Export_Plan
  Scenario:User should be able to enter "Your product packaging" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "About your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Your product packaging example" on page "Build An Export Plan - About Your Business"
    And "Robert" decides to enter text at "Your product packaging" on page "Build An Export Plan - About Your Business"
    And "Robert" decides to validate entered text at "Your product packaging" on page "Build An Export Plan - About Your Business"

@allure.link:XOT-1015
   @Great_Magna_Export_Plan_A_Y_B_P
  @Great_Magna_Export_Plan
  Scenario:User should be able to click on section complete and  "Business objective link" at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - About Your Business"
    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - About Your Business"
    And "Robert" should be on the "Build An Export Plan - Business Objectives" page

@allure.link:XOT-1016
   @Great_Magna_Export_Plan_A_Y_B_P
  @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - About Your Business"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

  @allure.link:XOT-1017
   @Great_Magna_Export_Plan_A_Y_B_P
    @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Business performance" section and select random turnover

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Your business performance dropdown" on page "Build An Export Plan - About Your business"

     @allure.link:XOT-1018
   @Great_Magna_Export_Plan_A_Y_B_P
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Business Objectives" page

    Given "Robert" visited "GreatMagna - Login" page
     When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
      And "Robert" should be on the "GreatMagna - Dashboard" Page
     #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to click on element "Nav Business Objectives" on page "Build An Export Plan - About Your Business"
     And "Robert" should be on the "Build An Export Plan - Business Objectives" Page

     @allure.link:XOT-1019
       @Great_Magna_Export_Plan_A_Y_B_P
   @Great-Magna-Export_Plan-progress-bar-test
   @Great_Magna_Export_Plan
 Scenario:User should be able to click section complete on "About Your Business" page  and back to export plan dashboard

Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Build an export plan"
   Then "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - About Your Business"
    And "Robert" decides to click on "Build an export plan"

#@allure.link:XOT-1016
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to click on Top Export plan home in "About your business" and should be on Export plan dashboard page
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - About Your Business"
#     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

 @allure.link:XOT-1002
   @Great_Magna_Export_Plan_B_O_Last_1
   @Great_Magna_Export_Plan_A_Y_B_P
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Drop down" on About your business page and click on dashboard should see "About your business page" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - About Your Business" Page
   And "Robert" decides to click on element "Your product packaging example" on page "Build An Export Plan - About Your Business"
   #And "Robert" decides to select random item for "Your business performance dropdown" on page "Build An Export Plan - About Your business"
    And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - About Your Business"
    And "Robert" should see "About Your Business" text under section "Export Plan" on page "GreatMagna - Dashboard"
