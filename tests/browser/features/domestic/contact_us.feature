@domestic
@contact-us
@allure.suite:Domestic
Feature: Domestic - Contact us

  Background:
    Given test authentication is done


  @allure.link:TT-758
  @enquirer-location
  @contact-us_1
  Scenario: Enquirers should see all expected contact location options on the "Domestic - Contact us"
    Given "Robert" visits the "Domestic - Contact us" page

    Then "Robert" should be on the "Domestic - Contact us" page
    And "Robert" should see following form choices
      | radio elements |
      | The UK         |
      | Outside the UK |


  @allure.link:TT-758
  @enquirer-location
  @contact-us_2
  @domestic-enquiry-page
  Scenario: Domestic Enquirers should see all expected contact options on the "Domestic - What can we help you with?" page
    Given "Robert" visits the "Domestic - Contact us" page

    When "Robert" says that his business is in "The UK"

    Then "Robert" should be on the "Domestic - What can we help you with? - Domestic Contact us" page
    And "Robert" should see following form choices
      | radio elements                            |
      | Find your local trade office              |
      | Advice to export from the UK              |
      | Great.gov.uk account and services support |
      | UK Export Finance (UKEF)                  |
      | Brexit enquiries                          |
      | Events                                    |
      | Defence and Security Organisation (DSO)   |
      | Other                                     |


  @allure.link:TT-363
  @office-finder
  @contact-us_3
  Scenario: Domestic Enquirers should be able to get to the "New Office finder - Home" page
    Given "Robert" visits the "Domestic - Contact us" page

    When "Robert" says that his business is in "the UK"
    And "Robert" chooses "Find your local trade office" option

    Then "Robert" should be on the "Domestic - New Office Finder" page


  @allure.link:TT-363
  @office-finder
  @contact-us_4
  Scenario Outline: Domestic Enquirers should be able to get to find contact details for "<appropriate>" office in "<city>"
    Given "Robert" visits the "Domestic - New Office Finder" page

    When "Robert" searches for local trade office near "<post-code>"

    Then "Robert" should be on the "Domestic - New Office Finder - search results" page
    And "Robert" should see contact details for "<appropriate>" office in "<city>"

    Examples: postcodes and trade offices
      | post-code | appropriate       | city        |
      | LL57 1ST  | Business Wales    | Sarn Mynach |
      | LE5 3BF   | DIT East Midlands | Leicester   |

    @full
    Examples: postcodes and trade offices
      | post-code | appropriate                  | city       |
      | AL10 8EP  | DIT East of England          | Hatfield   |
      | SW1A 2AA  | DIT London                   | London     |
      | DH1 1SQ   | DIT North East               | Durham     |
      | M15 6PQ   | DIT North West               | Manchester |
      | PO15 5DE  | DIT South East               | Fareham    |
      | BS1 4RL   | DIT South West               | Bristol    |
      | B3 2RT    | DIT West Midlands            | Birmingham |
      | S70 2PS   | DIT Yorkshire and the Humber | Barnsley   |
      | BT2 8DN   | Invest NI                    | Belfast    |
      | G3 6AP    | Scottish Enterprise          | Glasgow    |


  @wip
  @allure.link:TT-363
  @office-finder
  @contact-us_5
   @failed
  Scenario: Domestic Enquirers should be able to get to the NEW Office finder page
    Given "Robert" visits the "Domestic - New Office Finder" page

    When "Robert" found his local trade office by providing his company's postcode
    And "Robert" decides to "Contact the local trade office"

    Then "Robert" should be on the "Domestic - Short contact form (Office Finder)" page


  @wip
  @allure.link:TT-363
  @captcha
  @dev-only
  @office-finder
  @contact-us_6
  @failed
  Scenario: Domestic Enquirers should be able to contact
    Given "Robert" got to the "Short contact-us form" page via "Find local trade office"

    When "Robert" fills out and submits the form

    Then "Robert" should be on the "Thank you for your enquiry" page
    And an email is submitted to "appropriate local office based on the postcode provided"


  @allure.link:TT-758
  @exporting-from-the-UK
  @contact-us_7
  Scenario: Domestic Enquirers should be able to get to the "Long (Export Advice Comment) - Contact us" form
    Given "Robert" visits the "Domestic - Contact us" page

    When "Robert" says that his business is in "the UK"
    And "Robert" chooses "Advice to export from the UK" option

    Then "Robert" should be on the "Domestic - Long (Export Advice Comment) - Contact us" page


  @allure.link:TT-758
  @ita
  @captcha
  @exporting-from-the-UK
  @contact-us_8
  @failed
  Scenario: Domestic Enquirers should be able to contact relevant ITA based on the postcode provided
    Given "Robert" got to the "Domestic - Long (Export Advice Comment)" page via "The UK -> Advice to export from the UK"

    When "Robert" fills out and submits the form
    Then "Robert" should be on the "Domestic - Long (Personal details) - Contact us" page
    When "Robert" fills out and submits the form
    Then "Robert" should be on the "Domestic - Long (Business details) - Contact us" page
    When "Robert" fills out and submits the form

    Then "Robert" should be on the "Domestic - Thank you for your enquiry" page
    And "Robert" should receive "Thank you for your enquiry" confirmation email
    # TODO check if this email is being actually sent
#    And an email is submitted to relevant "ITA" (based on the postcode provided)


  @allure.link:TT-758
  @account-support
  @contact-us_9
  Scenario: Domestic enquirers should see all expected help options on the "Great.gov.uk account and services support" page
    Given "Robert" got to the "Domestic - Great.gov.uk account and services support" page via "The UK -> Great.gov.uk account and services support"

    Then "Robert" should see following form choices
      | radio elements               |
      | Export opportunities service |
      | Your account on Great.gov.uk |
      | Other                        |


  @allure.link:TT-758
  @exopps
  @account-support
  @contact-us_10
  Scenario: Domestic enquirers should see all expected help options for "Export opportunities service"
    Given "Robert" got to the "Domestic - Export opportunities service" page via "The UK -> Great.gov.uk account and services support -> Export opportunities service"

    Then "Robert" should see following form choices
      | radio elements                                              |
      | I haven't had a response from the opportunity I applied for |
      | My daily alerts are not relevant to me                      |
      | Other                                                       |


  @allure.link:TT-758
  @greatgovuk-account
  @account-support
  @contact-us_11
  Scenario: Domestic enquirers should see all expected help options for "Great.gov.uk account"
    Given "Robert" got to the "Domestic - Great.gov.uk account" page via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk"

    Then "Robert" should see following form choices
      | radio elements                                                 |
      | I have not received an email confirmation                      |
      | I need to reset my password                                    |
#      | I cannot find my company                                       |
      | My Companies House login is not working                        |
      | I do not know where to enter my verification code              |
      | I have not received my letter containing the verification code |
      | I have not received a verification code                        |
      | Other                                                          |


  @allure.link:TT-758
  @short-domestic
  @account-support
  @contact-us_12
  @failed
  Scenario: Domestic enquirers should be able to get to the "Short Contact Us" form via "The UK -> Great.gov.uk account and services support -> Other"
    Given "Robert" got to the "Domestic - Great.gov.uk account and services support" page via "The UK -> Great.gov.uk account and services support"

    When "Robert" chooses "Other" option

    Then "Robert" should be on the "Domestic - Short contact form (Tell us how we can help)" page


  @allure.link:TT-758
  @short-domestic
  @greatgovuk-account
  @contact-us_13
  @support
  Scenario: Domestic enquirers should be able to get to the "Short Contact Us" form via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk -> Other"
    Given "Robert" got to the "Domestic - Great.gov.uk account" page via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk"

    When "Robert" chooses "Other" option

    Then "Robert" should be on the "Domestic - Short contact form (Tell us how we can help)" page


  @allure.link:TT-758
  @greatgovuk-account
  @support
  @contact-us_14
  Scenario: Domestic enquirers should be able to find answers to sought topic about "Your account on Great.gov.uk"
    Given "Robert" got to the "Domestic - Great.gov.uk account" page via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk"

    When "Robert" chooses any available option except "Other"

    Then "Robert" should be on the "Domestic - Great.gov.uk account - Dedicated Support Content" page


  @allure.link:TT-758
    @exopps
    @support
    @contact-us_15
  Scenario Outline: Exporters should be able to find answers to Export Opportunities related topic "<selected>"
    Given "Robert" got to the "Domestic - Export opportunities service" page via "The UK -> Great.gov.uk account and services support -> Export opportunities service"

    When "Robert" chooses "<selected>" option

    Then "Robert" should be on the "Domestic - <selected> - Dedicated Support Content" page

    Examples:
      | selected                                                    |
      | I haven't had a response from the opportunity I applied for |
      | My daily alerts are not relevant to me                      |


  @allure.link:TT-758
    @zendesk
    @dev-only
    @captcha
    @account-support
    @contact-us_16
    @failed
  Scenario Outline: Domestic Enquirers should be able to contact Great Support team via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk -> <selected topic>"
    Given "Robert" got to the "Domestic - <selected topic> - Dedicated Support Content" page via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk -> <selected topic>"

    When "Robert" decides to "Submit an enquiry"
    And "Robert" is on the "Domestic - Short contact form (Tell us how we can help)" page
    And "Robert" fills out and submits the form

    Then "Robert" should be on the "Domestic - Thank you for your enquiry (<selected topic>)" page
    And a "zendesk" notification entitled "great.gov.uk contact form" should be sent to "Robert"

    Examples:
      | selected topic                            |
      | I have not received an email confirmation |

    @full
    Examples:
      | selected topic                                                 |
      | I have not received an email confirmation                      |
      | I need to reset my password                                    |
      | My Companies House login is not working                        |
      | I do not know where to enter my verification code              |
      | I have not received my letter containing the verification code |
      | I have not received a verification code                        |


  @allure.link:TT-758
    @zendesk
    @dev-only
    @captcha
    @exopps
    @contact-us_17
  Scenario Outline: Exporters should be to contact Export Opportunities team via Zendesk using "Short contact form" page accessed via "The UK -> Great.gov.uk account and services support -> Export opportunities service -> <selected topic>"
    Given "Robert" got to the "Domestic - <selected topic> - Dedicated Support Content" page via "The UK -> Great.gov.uk account and services support -> Export opportunities service -> <selected topic>"

    When "Robert" decides to "Submit an enquiry"
    And "Robert" is on the "Domestic - Short contact form (Tell us how we can help)" page
    And "Robert" fills out and submits the form

    Then "Robert" should be on the "Domestic - Thank you for your enquiry (<selected topic>) - Short Domestic Contact us" page
    And a "zendesk" notification entitled "great.gov.uk contact form" should be sent to "Robert"

    Examples:
      | selected topic                                              |
      | I haven't had a response from the opportunity I applied for |
      | My daily alerts are not relevant to me                      |


  # Choosing "Other" on the "Your account on Great.gov.uk" page takes us
  # directly to the short contact us form
  @allure.link:TT-758
    @zendesk
    @dev-only
    @captcha
    @account-support
    @contact-us_18
    @failed
  Scenario Outline: Domestic Enquirers should be able to contact Great Support team via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk -> <selected topic>"
    Given "Robert" got to the "Domestic - Short contact form (Tell us how we can help)" page via "The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk -> <selected topic>"

    When "Robert" fills out and submits the form

    Then "Robert" should be on the "Domestic - Thank you for your enquiry (<selected topic>) - Short Domestic Contact us" page
    And a "zendesk" notification entitled "great.gov.uk contact form" should be sent to "Robert"

    Examples:
      | selected topic |
      | Other          |


  @allure.link:TT-758
  @ukef
  @contact-us_19
  Scenario: Exporters should be able to get to the UKEF Check your eligibility contact-us form
    Given "Robert" got to the "Domestic - What can we help you with? - Domestic Contact us" page via "The UK"

    When "Robert" chooses "UK Export Finance (UKEF)" option

    Then "Robert" should be on the "Domestic - Your details - UKEF Contact us" page


  # already partially covered by stories for TT-585
  @dev-only
  @captcha
  @ukef
  @contact-us_20
  @failed
  Scenario: Exporters should be able to contact UKEF mailbox
    Given "Robert" got to the "Domestic - Your details - UKEF Contact us" page via "The UK -> UK Export Finance (UKEF)"

    When "Robert" fills out and submits the form

    Then "Robert" should be on the "Domestic - Thank you - UKEF Contact us" page
    # No confirmation email is sent to the user
    # TODO check if email is sent to dedicated mailbox
    And an email is submitted to "UKEF mailbox"


  @allure.link:TT-758
    @investing-overseas
    @events
    @dso
    @short-form
    @contact-us_21
  Scenario Outline: Domestic enquirers should get to the "Short contact us form" via "The UK -> <selected option>"
    Given "Robert" got to the "Domestic - What can we help you with? - Domestic Contact us" page via "The UK"

    When "Robert" chooses "<selected option>" option

    Then "Robert" should be on the "Domestic - Short contact form (<selected option>)" page

    Examples:
      | selected option                         |
      | Events                                  |
      | Defence and Security Organisation (DSO) |
      | Other                                   |

  #change to eu exit and eu enquiries
  @allure.link:TT-758
  @allure.link:CMS-506
  @eu-exit
  @feature-flagged
  @contact-us_22
  @failed
  Scenario: Exporters should be able to get to the "Domestic EU exit help short contact-us form"
    Given "Robert" got to the "Domestic - What can we help you with? - Domestic Contact us" page via "The UK"

    When "Robert" chooses "Brexit enquiries" option

    Then "Robert" should be on the "Domestic - Brexit help" page

  #change to eu exit and eu enquiries
  @allure.link:TT-758
  @zendesk
  @allure.link:CMS-506
  @captcha
  @eu-exit
  @contact-us_23
  @failed
  Scenario: Exporters should be able to contact "Brexit help mailbox"
    Given "Robert" got to the "Domestic - Brexit help" page via "The UK -> Brexit enquiries"

    When "Robert" fills out and submits the form

    Then "Robert" should be on the "Domestic - Brexit help - Thank you" page
    And a "zendesk" notification entitled "Brexit contact form" should be sent to "Robert"


  @allure.link:TT-758
    @dev-only
    @captcha
    @short-form
    @contact-us
  Scenario Outline: Exporters should be able to contact "<expected recipient>" using "Short contact form (<selected option>)" page accessed via "The UK -> <selected option>"
    Given "Robert" got to the "Domestic - Short contact form (<selected option>)" page via "The UK -> <selected option>"

    When "Robert" fills out and submits the form

    Then "Robert" should be on the "Domestic - Thank you for your enquiry (<selected option>) - Short Domestic Contact us" page
    And "Robert" should receive "<appropriate>" confirmation email
    And an email notification about "Robert"'s enquiry should be send to "<expected recipient>"

    Examples:
      | selected option                         | appropriate                                                  | expected recipient |
      | Events                                  | Thank you for your Events enquiry                            | Events mailbox     |
      | Defence and Security Organisation (DSO) | Thank you for your Defence and Security Organisation enquiry | DSO mailbox        |
      | Other                                   | Thank you for your enquiry                                   | DIT Enquiry unit   |


  @allure.link:TT-758
  @international
  @contact-us_24
  Scenario: International Enquirers should be able to see all expected contact options on the "International - What would you like to know more about?" page
    Given "Robert" visits the "Domestic - Contact us" page

    When "Robert" says that his business is "Outside the UK"

    Then "Robert" should be on the "Domestic - What would you like to know more about? - International Contact us" page
    And "Robert" should see following form choices
      | radio elements              |
      | Expanding to the UK         |
      | Investing capital in the UK |
      | Find a UK business partner  |
      | The transition period       |
      | Other                       |


  @allure.link:TT-758
    @international
    @contact-us_25
    @failed
  Scenario Outline: International Enquirers should be able to get to the "<expected>" form for "<selected>"
    Given "Robert" got to the "Domestic - What would you like to know more about? - International Contact us" page via "Outside the UK"

    When "Robert" chooses "<selected>" option

    Then "Robert" should be on the "<expected>" page

    Examples:
      | selected                    | expected                                                |
      | Expanding to the UK         | Invest - Contact us                                     |
      | Investing capital in the UK | International - Contact the Capital Investment team     |
      | Find a UK business partner  | International - Find a UK business partner - Contact us |
      | The transition period       | International - Transition period enquiries             |
      | Other                       | International - Contact us                              |


  @allure.link:TT-758
    @going-back
    @contact-us_26
    @failed
  Scenario Outline: Enquirers should be able to navigate back to previous pages from "<path>" back to "<expected>" page
    Given "Robert" navigates via "<path>"

    When "Robert" decides to use "back" link

    Then "Robert" should be on the "<expected>" page

    Examples:
      | path                                                                                | expected                                                    |
      | The UK                                                                              | Domestic - Contact us                                       |
      | Outside the UK                                                                      | Domestic - Contact us                                       |
      | The UK -> Great.gov.uk account and services support                                 | Domestic - What can we help you with? - Domestic Contact us |
      | The UK -> Great.gov.uk account and services support -> Export opportunities service | Domestic - Great.gov.uk account and services support        |
      | The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk | Domestic - Great.gov.uk account and services support        |


