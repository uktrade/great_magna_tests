@business-risk-page
@allure.suite:Great_Magna_Export_Plan_B_R

Feature: GreatMagna - Business Risk Page
   Background:
   Given test authentication is done

     @placeholder_test
     @skip
   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Business Risk" Page and click back button

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on element "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
    And "Robert" decides to click on element "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "ok Button" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page



@allure.link:XOT-1016
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Top Export plan home in Business Risk and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Business Risk"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

@allure.link:XOT-1019
  @Great_Magna_Export_Plan
   @Great-Magna-Export_Plan-progress-bar-test
 Scenario:User should be able to click on "Download export plan" at the bottom of the page

Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Build an export plan"
   Then "Robert" decides to click on section "Business risk" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - Business risk"
    And "Robert" decides to click on section "Download export plan" on page "Build An Export Plan - Business risk"


       @allure.link:XOT-1019
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Download export plan"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Business risk" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Business risk"
      And "Robert" decides to click on element "Nav Download export plan" on page "Build An Export Plan - Business risk"
     And "Robert" decides to click on element "Share" on page "Build An Export Plan - Business risk"



    @allure.link:XOT-1007
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home on "Travel plan" and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
       And "Robert" decides to click section complete on "Build An Export Plan - Business Risk"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Business Risk"
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
  And "Robert" "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
  And "Robert" decides to enter product name "Sofa" on page "Build An Export Plan - Business Risk"


 @allure.link:XOT-1002
   @Great_Magna_Export_Plan_B_R_1
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Add A Risk" and enter the Risk details for exporting

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" fill risk details on page "Build An Export Plan - Business Risk"
          | Position | Risktext  | Contingencyplan |
          | 1     | Risk-1 | Contingencyplan |
          | 2     | Risk-2 | Contingencyplan |
          | 3     | Risk-3 | Contingencyplan |
          | 4     | Risk-4 | Contingencyplan |
          | 5     | Risk-5 | Contingencyplan |

     @allure.link:XOT-1002
   @Great_Magna_Export_Plan
  Scenario:User should be able to click section complete on Business Risk page and click on dashboard should see "Business Risk" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Business Risk" Page
    And "Robert" decides to click section complete on "Build An Export Plan - Business Risk"
     And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Business Risk"
     And "Robert" should see "Business Risk" text under section "Export Plan" on page "GreatMagna - Dashboard"


   @allure.link:XOT-1002
   @Great_Magna_Export_Plan_B_R_1_111
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Add A Risk" and click on Examples and educational moment

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Add A Risk" on page "Build An Export Plan - Business Risk"
    And "Robert" decides to click on element "Risk example" on page "Build An Export Plan - Business Risk"
    And "Robert" decides to click on element "Risk educational" on page "Build An Export Plan - Business Risk"
    And "Robert" decides to click on element "Risk likelihood educational" on page "Build An Export Plan - Business Risk"
    And "Robert" decides to click on element "Risk impact educational" on page "Build An Export Plan - Business Risk"
    And "Robert" decides to click on element "contingency plan educational" on page "Build An Export Plan - Business Risk"
    And "Robert" decides to click on element "contingency plan example" on page "Build An Export Plan - Business Risk"

