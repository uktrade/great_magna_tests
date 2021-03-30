@business-objectives-page
@allure.suite:Great_Magna_Export_Plan_B_O
Feature: GreatMagna - Business Objectives Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1001
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "Why you want to export" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Why you want to export example" on page "Build An Export Plan - Business Objectives"
     And "Robert" decides to enter text at "Why you want to export" on page "Build An Export Plan - Business Objectives"
     And "Robert" decides to validate entered text at "Why you want to export" on page "Build An Export Plan - Business Objectives"

 @allure.link:XOT-1002
   @Great_Magna_Export_Plan_B_O
  Scenario:User should be able to click on "Add goal" and enter the objectives for exporting

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" fill business objective details on page "Build An Export Plan - Business Objectives"
          | Position | Startdate  | Enddate    | Objectives | Owner        | PlannedReviews   |
          | 1     | 01/02/2021 | 01/02/2028 | obj1       | obj1-owner   | obj1-plannedreviews |
          | 2     | 01/02/2021 | 01/02/2028 | obj2       | obj2-owner   | obj2-plannedreviews |
          | 3     | 01/02/2021 | 01/02/2028 | obj3       | obj3-owner   | obj3-plannedreviews |
          | 4     | 01/02/2021 | 01/02/2028 | obj4       | obj4-owner   | obj4-plannedreviews |
          | 5     | 01/02/2021 | 01/02/2028 | obj5       | obj5-owner   | obj5-plannedreviews |
   
   @allure.link:XOT-1002
   @Great_Magna_Export_Plan_B_O
   Scenario:User should be able to click on "Add goal" and enter the objectives for exporting

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
     Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to delete business objectives on page "Build An Export Plan - Business Objectives"
          | Position |
          | 5     |
          | 4     |
          | 3     |
          | 2     |
          | 1     |


#@allure.link:XOT-1005
#   @Great_Magna_Export_Plan
# Scenario:User should be able to click lessons "Move from accidental exporting to strategic exporting" and click back link "Business Objectives"
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#   # And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "Build An Export Plan - Business Objectives"
#     And "Robert" should be on the "LearnToExport - Move from accidental exporting to strategic exporting" page
#     And "Robert" decides to click on section "Business Objectives" on page "LearnToExport - Move from accidental exporting to strategic exporting"


@allure.link:XOT-1006
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on next "Target markets research"page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click section complete on "Build An Export Plan - Business Objectives"
     And "Robert" decides to click on section "Target markets research" on page "Build An Export Plan - Business Objectives"
     And "Robert" should be on the "Build An Export Plan - Target markets research" page

@allure.link:XOT-1007
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home on "Business objective" Page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Business Objectives"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page


 @allure.link:XOT-1008
   @Great-Magna-Export_Plan-progress-bar-test
 Scenario:User should be able to click section complete on "Business objective" page  and back to export plan dashboard

Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Build an export plan"
   Then "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - Business Objectives"
    And "Robert" decides to click on "Build an export plan"
    And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Identify opportunities" page
