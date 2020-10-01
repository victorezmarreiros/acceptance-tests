Feature: Test that pages have correct content
  Scenario: Blog page has a correct title
    Given I open the browser
    Given I am on the blog page
    Then The is a title shown on the page
    Then The title tag has content "This is the blog page"