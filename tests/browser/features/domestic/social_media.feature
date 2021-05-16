#@domestic
#@sharing
#@social-media
#@allure.suite:Domestic
#Feature: Domestic - Sharing on Social Media and via emails
#
#  Background:
#    Given test authentication is done
#
#  @allure.link:CMS-686
#    @allure.issue:CMS-733
#    @advice
#    @article
#    @social-media_1
#    @<social_media>
#  Scenario Outline: Any Exporter should be able to share Advice article via "<social_media>"
#    Given "Robert" is on randomly selected Advice article page
#
#    When "Robert" decides to share the article via "<social_media>"
#
#    Then "Robert" should be taken to a new tab with the "<social_media>" share page opened
#    And "Robert" should see that "<social_media>" share page has been pre-populated with message and the link to the article
#
#    Examples:
#      | social_media |
#      | Facebook     |
#      | Twitter      |
#
#
#  @allure.link:CMS-686
#  @allure.issue:CMS-733
#  @advice
#  @article
#  @linkedin
#  @social-media_2
#  Scenario: Any Exporter should be able to share Advice article via "LinkedIn"
#    Given "Robert" is on randomly selected Advice article page
#
#    When "Robert" decides to share the article via "LinkedIn"
#
#    Then "Robert" should see that "LinkedIn" share link contains link to the article
#
#
#  @allure.link:CMS-686
#  @allure.issue:CMS-733
#  @advice
#  @article
#  @social-media_3
#  @email
#  Scenario: Any Exporter should be able to share Advice article via "email"
#    Given "Robert" is on randomly selected Advice article page
#
#    When "Robert" decides to share the article via "email"
#
#    Then "Robert" should see that the share via email link will pre-populate the message subject and body with Article title and URL
