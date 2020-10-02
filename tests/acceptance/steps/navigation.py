from behave import *
from selenium import webdriver

from tests.acceptance.page_models.base_page import BasePage
from tests.acceptance.page_models.blog_page import BlogPage
from tests.acceptance.page_models.home_page import HomePage
from tests.acceptance.page_models.new_posts_page import NewPostPage

use_step_matcher('re')   # Expressoes Regulares, mapeia cada step com
# permite que nossos steps recebam argumentos do scenario que criamos em nav.feature


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
