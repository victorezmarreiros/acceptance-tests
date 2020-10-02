from behave import *

from tests.acceptance.page_models.base_page import BasePage
from tests.acceptance.page_models.blog_page import BlogPage

use_step_matcher('re')


@Then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@Then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@Then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()
