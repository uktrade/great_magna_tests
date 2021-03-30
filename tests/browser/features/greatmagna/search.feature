@search-page
@allure.suite:Great_Magna_Search
Feature: Search product & country in personalisation

  Background:
    Given Test authentication is done

  @allure.link:XOT-081
  @Great-Magna-Search-1
 Scenario Outline: User should be able to search I want to export products in country

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" should be able to enter products "<products>" and country "<country>"
        Examples: Products and Country
         | products                 | country      |
         | Vehicle                  | India      |
#         | Leather                  | Poland       |
#         | Red Roses                | Netherlands  |
#         | Steel                    | India        |
#         | Shirt                    | South Korea  |


   @allure.link:XOT-082
   @Great-Magna-Search
  Scenario: Visitor should be able to go to Dashboard page on click "Back"
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" should be able to enter products "Vehicle"

    And "Robert" decides to click on "Search again"

    And "Robert" should be on the "GreatMagna - Dashboard" page

#  @allure.link:XOT-083
#  @Great-Magna-Search
#  Scenario Outline: Visitor should be able to see error message on failure to enter product
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" should be able to enter products "<products>"
#    And "Robert" should be able to see error message "No results found for" on the "GreatMagna - Dashboard" Page
#    And "Robert" decides to click on "Search again"
#    Examples: Products and Country
#         | products                 | country       |
#         | @@@@@@                   | !!!!!!!       |
#         | ILoveLondonIwanttotest   | ££££££££      |
#         | 123456789                | %%%%%%%%      |
#         |           .,//           | ±±±__<>:"{}_  |
