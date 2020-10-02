from behave import *

from tests.acceptance.page_models.base_page import BasePage


use_step_matcher('re')


@Then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@Then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content
