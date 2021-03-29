@about-your-business-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - About your Business Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1010
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to view "How you started" section and enter text

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
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to view "Where you're based" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #nd "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Where you're based example" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to enter text at "Where you're based" on page "Build An Export Plan - About Your Business"
     And "Robert" decides to validate entered text at "Where you're based" on page "Build An Export Plan - About Your Business"

@allure.link:XOT-1012
   @GGreat_Magna_Export_Plan
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
   @GGreat_Magna_Export_Plan
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

#  @allure.link:XOT-1014
#   @GGreat_Magna_Export_Plan
#  Scenario:User should be able to click lessons link "Move from accidental exporting to strategic exporting" and back to "About your Business" page
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "About your Business" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "Build An Export Plan - About your Business"
#    And "Robert" should be on the "LearnToExport - Move from accidental exporting to strategic exporting" page
#    And "Robert" decides to click on section "About your Business" on page "LearnToExport - Move from accidental exporting to strategic exporting"

@allure.link:XOT-1015
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on "Business objective" next page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - About Your Business"
    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - About Your Business"

@allure.link:XOT-1016
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - About Your Business"

  @allure.link:XOT-1017
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on "Business performance" section and select random turnover

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Your business performance dropdown" on page "Build An Export Plan - About Your business"

     @allure.link:XOT-1014
   @GGreat_Magna_Export_Plan
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

     @allure.link:XOT-124
   @Great-Magna-Export_Plan-progress-bar-test
 Scenario:User should be able to click section complete on "About Your Business" page  and back to export plan dashboard

Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Build an export plan"
   Then "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - About Your Business"
    And "Robert" decides to click on "Build an export plan"
    #And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Identify opportunities" page
