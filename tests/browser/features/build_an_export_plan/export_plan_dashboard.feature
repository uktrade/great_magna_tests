@Great_Magna_Tests
@upload-logo-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Export plan Upload logo
   Background:
   Given test authentication is done

   @allure.link:XOT-1010
   @Great_Magna_Export_Plan_upload
  Scenario Outline:User should be able to upload logo

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" uploads "<valid_image>" as company's logo
#     And "Robert" decides to click on section "Export Plan Dashboard - Upload Logo" on page "Build An Export Plan - Export Plan Dashboard"
     #And "Robert" decides to click on "choose file" and save continue
#
#  Scenario Outline: Supplier should be able to upload "<valid_image>" image to set company's logo
#    Given "Peter Alder" created a "published LTD, PLC or Royal Charter" profile for a random company "Y"
#
#    When "Peter Alder" uploads "<valid_image>" as company's logo
#
#    Then "Peter Alder" should see that logo on FAB Company's Directory Profile page
#    And "Peter Alder" should see a PNG logo thumbnail on FAS Company's Directory Profile page

    Examples:
      | valid_image                                  |
      | Anfiteatro_El_Jem.jpeg                       |
#      | Kobe_Port_Tower.jpg                          |
#      | archive-org-solid-background.png             |
#      | Wikipedia-logo-v2-en-alpa-channel.png        |
#      | Animated_PNG_example_bouncing_beach_ball.png |


  @allure.link:XOT-1011
   @Great_Magna_Export_Plan_pdf
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Save your plan as PDF"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on element "Save your plan as PDF" on page "Build An Export Plan - Export Plan Dashboard"


     @allure.link:XOT-1011
  @Great_Magna_Export_Plan
      @export_plan_sections
  Scenario: User should see all the Export plan pages and all services
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" should see following sections
      | sections                |
      | Header                  |
      | About your business     |
      | Business Objectives     |
      | Target markets research |
      | Adapting your product   |
      | Marketing approach      |
      | Costs and pricing       |
      | Funding and credit      |
      | Getting paid            |
      | Travel plan             |
      | Business Risk           |
      | Logo                    |
      | Save your plan as PDF   |
