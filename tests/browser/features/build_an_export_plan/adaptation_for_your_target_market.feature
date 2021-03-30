@adaptation-for-your-target-market-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Adaptation For Your Target Market Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1028
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Open DataSnapshot" and check whether atleast one language is present

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Open Data Snapshot" on page "Build An Export Plan - Adaptation For Your Target Market"
     And "Robert" decides to click on element "Hide Data Snapshot" on page "Build An Export Plan - Adaptation For Your Target Market"

   @allure.link:XOT-1021
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to view tool tip and enter relevant text in "Changing your product to adapt to your target market"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    #And "Robert" decides to click on element "Labelling educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Labelling" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Labelling" on page "Build An Export Plan - Adaptation For Your Target Market"

    #And "Robert" decides to click on element "Packaging educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Packaging" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Packaging" on page "Build An Export Plan - Adaptation For Your Target Market"

    #And "Robert" decides to click on element "Size educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Size" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Size" on page "Build An Export Plan - Adaptation For Your Target Market"

   # And "Robert" decides to click on element "Product changes to comply educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Product changes to comply" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Product changes to comply" on page "Build An Export Plan - Adaptation For Your Target Market"

    #And "Robert" decides to click on element "Translations educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Translations" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Translations" on page "Build An Export Plan - Adaptation For Your Target Market"

    And "Robert" decides to enter text at "Other changes" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Other changes" on page "Build An Export Plan - Adaptation For Your Target Market"


   @allure.link:XOT-1022
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to view educational tool tip and enter relevant text in "Documents you need to provide to meet the requirements for your target market"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    #And "Robert" decides to click on element "Certificate of origin educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Certificate of origin" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Certificate of origin" on page "Build An Export Plan - Adaptation For Your Target Market"

    #And "Robert" decides to click on element "Insurance certificate educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Insurance certificate" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Insurance certificate" on page "Build An Export Plan - Adaptation For Your Target Market"

    #And "Robert" decides to click on element "Commercial invoice educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Commercial invoice" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "Commercial invoice" on page "Build An Export Plan - Adaptation For Your Target Market"

    #And "Robert" decides to click on element "UK customs declaration educational" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "UK customs declaration" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to validate entered text at "UK customs declaration" on page "Build An Export Plan - Adaptation For Your Target Market"


   @allure.link:XOT-1023
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to add another document and enter text in document and notes then delete "Documents you need to provide to meet the requirements for your target market"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Add another document" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" decides to enter text at "Document name" on page "Build An Export Plan - Adaptation For Your Target Market"
    #And "Robert" decides to validate entered text at "Document name" on page "Build An Export Plan - Adaptation For Your Target Market"
    #And "Robert" decides to enter text at "Notes" on page "Build An Export Plan - Adaptation For Your Target Market"
    #And "Robert" decides to validate entered text at "Notes" on page "Build An Export Plan - Adaptation For Your Target Market"
     And "Robert" decides to click on "Delete" on page "Build An Export Plan - Adaptation For Your Target Market"


     @allure.link:XOT-1028
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home on "Adaptation For Your Target Market" Page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Adaptation For Your Target Market"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

    @allure.link:XOT-1014
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Marketing Approach" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to click on element "Nav Marketing Approach" on page "Build An Export Plan - Adaptation For Your Target Market"
     And "Robert" should be on the "Build An Export Plan - Adaptation For Your Target Market" Page

@allure.link:XOT-1015
   @GGreat_Magna_Export_Plan
  Scenario:User should be able to click page "Marketing Approach" from the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Marketing Approach" on page "Build An Export Plan - Adaptation For Your Target Market"

 @allure.link:XOT-1002
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Add another document" and enter the Document name and Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" fill document details on page "Build An Export Plan - Adaptation For Your Target Market"
          | Position | DocumentName  |   Notes         |
          | 1        | Vat certif    | Vat certificate |
          | 2        | Reg Document  | Reg Document    |
          | 3        | Id Proof      | Id Proof        |
          | 4        | Address Proof | Address Proof   |
          | 5        | Packing List  | Packing List    |

    @allure.link:XOT-1002
   @Great_Magna_Export_Plan
   Scenario:User should be able to click on "Add another document" and delete the document and notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
     Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Adaptation For Your Target Market" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to delete document details on page "Build An Export Plan - Adaptation For Your Target Market"
          | Position |
          | 5     |
          | 4     |
          | 3     |
          | 2     |
          | 1     |