from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_models.blog_page import BlogPage

use_step_matcher('re')


@given('I wait for the posts to load')
def step_impl(context):                                                # WebDriverWait(<Driver>, <Max Wait in seconds>)
    try:
        WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located(BlogPageLocators.POSTS_SECTION)     #.until(expected_conditions.<condition>(element))
        )
    except:
        raise Exception()
