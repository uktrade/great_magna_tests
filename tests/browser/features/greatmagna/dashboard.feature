@Great_Magna_Tests
@dashboard-page
@allure.suite:Great_Magna_Dashboard
Feature: GreatMagna - Dashboard Page

   Background:
    Given Test authentication is done

   @allure.link:XOT-021
   @Great-Magna-Dashboard
  Scenario Outline:User should be able to view Dashboard pages

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" should see following sections
      | sections             |
      | Learn to export      |
      | Compare Countries    |
      | Build an export plan |
      Examples: email address and password
          | email address | password |
          | santoshtesting10008+888@gmail.com | Testing@123! |

#
   @allure.link:XOT-022
   @Great-Magna-Dashboard
  Scenario Outline:User should be click on the questions for vfm

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on I have exported in the last 12 months
      Examples: email address and password
          | email address | password |
          | santoshtesting10008+888@gmail.com | Testing@123! |


   @allure.link:XOT-023
   @Great-Magna-Dashboard
  Scenario:User should be able to click Menu and the links

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
     Then "Robert" decides to click "Menu"
    And "Robert" decides to click "Home"
    And "Robert" decides to click "Learn to export"
    And "Robert" decides to click "Compare Countries"
    And "Robert" decides to click "Make An Export Plan"
    And "Robert" decides to click "Advice"
    And "Robert" decides to click "Markets"
#      Examples: email address and password
#          | email address | password |
#          | santoshtesting10008+888@gmail.com | Testing@123! |

 @allure.link:XOT-024
  @Great-Magna-Export_Plan_Dashboard_12
  Scenario: New User should be able to navigate to Dashbaord and click on Export plan section and click on Got to export plan and Start BUtton

  Given "Robert" visited "GreatMagna - Login" page
  When "Robert" decides to enter email address "santoshtesting10008+7619@gmail.com", password "Testing@123!" and click Login
  Then "Robert" should be on the "GreatMagna - Dashboard" Page
  And "Robert" decides to click on "Go To export plan"
  And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
  And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Export Plan Dashboard"
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   And "Robert" decides to click on "Start"
   And "Robert" should be on the "Build An Export Plan - About Your Business" Page


@allure.link:XOT-025
  @Great-Magna-Sign-Up
  Scenario Outline: First time landing on the dashboard page
  Given "Robert" visited "GreatMagna - Sign Up" page
  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
  Then "Robert" should be on the "GreatMagna - Dashboard" Page
  Examples: email address and password
     |      emailaddress                 | password    |
     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
  And "Robert" decides to click on "Build an export plan"
  And "Robert" "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
  And "Robert" decides to enter product name "Televisions" on page "Build An Export Plan - Travel Plan"
  And "Robert" decides to enter country name "Angola" on the "Build An Export Plan - Travel Plan" page

@allure.link:XOT-026
  @Great_Magna_Export_Plan
      @export_plan_dashboard_sections
  Scenario: User should see all Dashboard sections and services
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" should see following sections
      | sections         |
      | Header           |
      | Dashboard        |
      | I want to export |
      | Menu             |
      | Learn to export  |
      | Export plan      |
      | where to export  |
      | Footer           |

  @allure.link:XOT-027
  @Great_Magna_Export_Plan
   @export_plan_menu_list
    @failed_great_magna
  Scenario: User should see all Dashboard sections and services
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Menu"
    And "Robert" should see following sections
      | sections                 |
      | Home                     |
      | Learn to export     new  |
      | Where to export     new  |
      | Make an export plan new  |
      | Account                  |
      | Advice                   |
      | Markets                  |
      | Services                 |
      | Sign out                 |


@allure.link:XOT-1011
   @Great_Magna_Export_Plan_pdf_download
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Download as PDF" on the dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" should be able to see progress bar for section "10 out of 10" on "Build An Export Plan - Export Plan Dashboard" page
    And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Download as PDF" on page "GreatMagna - Dashboard"
    And "Robert" decides to click on element "Go to export plan" on page "GreatMagna - Dashboard"
    #And "Robert" decides to verify all sections complete on "Download as PDF" on page "Build An Export Plan - Export Plan Dashboard""

    @allure.link:XOT-027
  @Great_Magna_Export_Plan
   @footer_links
  Scenario: User should see all footer links
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    Then "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should see following sections
      | sections                                      |
      | Contact us                                    |
      | Privacy and cookies                           |
      | Terms and conditions                          |
      | Accessibility                                 |
      | Performance                                   |
      | Department for International Trade on GOV.UK  |
      | Go to the page for international business     |




