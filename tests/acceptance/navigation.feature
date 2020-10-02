Feature: Test navigation between pages
  We can have a longer description
  That can span a few lines

  Scenario: Homepage can go to the Blog
    Given I am on the homepage
    When I click on "Go to blog" link
    Then I am on the blog page

  Scenario: Blog can go to Homepage
    Given I am on the blog page
    When I click on "Go to home" link
    Then I am on the homepage