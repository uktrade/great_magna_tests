@Great_Magna_Tests
@vfm
@allure.suite:Great_Magna_Show_Me_Around
Feature:GreatMagna - Vfm Page

   @allure.link:XOT-011
   @Great-Magna-Vfm
   Scenario Outline:Visitor should be able answer the questions

  Given "Robert" visited "GreatMagna - Login" page
  When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
  And "Robert" should be on the "GreatMagna - Dashboard" Page
  Then "Robert" decides to click on element "Dashboard" on page "GreatMagna - Dashboard"
  And "Robert" should be on the "GreatMagna - VFM" Page
  And "Robert" decides to select random item for "VFM" on page "GreatMagna - Dashboard"
  And "Robert" should be on the "GreatMagna - Dashboard" Page
  Examples: email address and password
      | email address | password |
      | santoshtesting10008+9215@gmail.com | Testing@123! |