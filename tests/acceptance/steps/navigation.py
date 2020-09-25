from behave import *
from selenium import webdriver

use_step_matcher('re')   # permite que nossos steps recebam argumentos do scenario que criamos


@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome("")
    browser.get('http://127.0.0.1:5000')
