@Great_Magna_Tests
@domestic
@sso
  @1
@allure.suite:SSO
Feature: SSO - Sign in

  Background:
    Given test authentication is done



  @allure.issue:TT-1778
    @2_failed

  Scenario: Visitors should see all expected page elements on "SSO - Sign in"
    When "Robert" goes to the "SSO - Sign in" page

    Then "Robert" should see following sections
      | Sections                      |
      | Header                        |
      | SSO links - logged out        |
      | Breadcrumbs                   |
      | Form                          |
      | Create a great.gov.uk account |
      | Footer                        |



  @allure.issue:TT-1778
   @1_failed

  Scenario: Visitors should see all expected page elements on "SSO - Registration" page
    When "Robert" goes to the "SSO - Registration" page

    Then "Robert" should see following sections
      | Sections               |
      | Header                 |
      | SSO links - logged out |
      | Breadcrumbs            |
      | Form                   |
      | Footer                 |



  @allure.issue:TT-1778

  Scenario: Visitors should see all expected page elements on "Profile - Sign in"
    Given "Robert" visits the "SSO - Sign in" page

    When "Robert" decides to "Create account"

    Then "Robert" should be on the "Profile - Create an account" page
    And "Robert" should see following sections
      | Sections               |
      | Header                 |
      | Breadcrumbs            |
      | Enrolment progress bar |
      | Footer                 |
