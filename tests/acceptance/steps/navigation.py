from behave import *
from selenium import webdriver

use_step_matcher('re')   # Expressoes Regulares, mapeia cada step com
# permite que nossos steps recebam argumentos do scenario que criamos em nav.feature


@given('I open the browser')
def step_impl(context):
    context.browser = webdriver.Chrome()


@given('I am on the homepage')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000')


@given('I am on the blog page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url
