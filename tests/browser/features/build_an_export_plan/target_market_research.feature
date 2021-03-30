@target-markets-research-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Target Markets Research Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario:User should be able to "Open DataSnapshot" and select random age group and confirm

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Data Snapshot" on page "Build An Export Plan - Target Markets Research"
     #And "Robert" decides to click on section "Open" on page "Build An Export Plan - Target Markets Research"
    And "Robert" decides to select random checkbox "Age Group" on page "Build An Export Plan - Target Markets Research"

   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "Describe the consumer demand" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Describe the consumer demand example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "Describe the consumer demand" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "Describe the consumer demand" on page "Build An Export Plan - Target Markets Research"

@allure.link:XOT-1022
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "Who are your competitors" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Who are your competitors example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "Who are your competitors" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "Who are your competitors" on page "Build An Export Plan - Target Markets Research"



@allure.link:XOT-1023
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "What are the product trends" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "What are the product trends example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "What are the product trends" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "What are the product trends" on page "Build An Export Plan - Target Markets Research"

   @allure.link:XOT-1024
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "What’s your unique selling proposition" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "What’s your unique selling proposition example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "What’s your unique selling proposition" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "What’s your unique selling proposition" on page "Build An Export Plan - Target Markets Research"

   @allure.link:XOT-1024
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter price in  "What’s the average price for your product"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to enter value in "What’s the average price for your product" on page "Build An Export Plan - Target Markets Research"


@allure.link:XOT-1026
   @Great_Magna_Export_Plan
 Scenario:User should be able to click lesson link "Work out customer demand" and click link back to "Target Markets Research"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to click on section "Work out customer demand" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "LearnToExport - Work out customer demand" page
     And "Robert" decides to click on section "Target Markets Research" on page "LearnToExport - Work out customer demand"

#
#   @allure.link:XOT-1026
#   @Great_Magna_Export_Plan
# Scenario:User should be able to click lesson link "Using what you know" and click link back to"Target Markets Research"
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
#  And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Target Markets Research"
#     And "Robert" decides to click on section "Using what you know" on page "Build An Export Plan - Target Markets Research"
#     And "Robert" should be on the "LearnToExport - Using what you know" page
#     And "Robert" decides to click on section "Target Markets Research" on page "LearnToExport - Using what you know"
#
#
#
#      @allure.link:XOT-1026
#   @Great_Magna_Export_Plan
# Scenario:User should be able to click lesson link "Understand market trends" and click link back to "Target Markets Research"
#
#    Given "Robert" visited "GreatMagna - Login" page
 #   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
 #  # And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
#  And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Target Markets Research"
#     And "Robert" decides to click on section "Understand market trends" on page "Build An Export Plan - Target Markets Research"
#     And "Robert" should be on the "LearnToExport - Understand market trends" page
#     And "Robert" decides to click on section "Target Markets Research" on page "LearnToExport - Understand market trends"


@allure.link:XOT-1027
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on page "Adaptation for your target market" from the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Adaptation for your target market" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "Build An Export Plan - Adaptation for your target market" page

@allure.link:XOT-1028
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Target Markets Research"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

     @allure.link:XOT-1014
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Adaptation for your target market" page

    Given "Robert" visited "GreatMagna - Login" page
     When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
      And "Robert" should be on the "GreatMagna - Dashboard" Page
     And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to click on element "Nav Adaptation for your target market" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "Build An Export Plan - Adaptation for your target market" Page
