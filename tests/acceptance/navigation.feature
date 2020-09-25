Feature: Test navigation between pages
  We can have a longer description
  That can span a few lines

  Scenario: Homepage can go to the Blog
    Given I open the browser
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page

  Scenario: Blog can go to Homepage
    Given I open the browser
    Given I am on the blog page
    When I click on the link with id "home-link"
    Then I am on the homepage