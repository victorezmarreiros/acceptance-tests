from behave import *

from tests.acceptance.page_models.base_page import BasePage
from tests.acceptance.page_models.new_posts_page import NewPostPage

use_step_matcher('re')

# Utilizando Regular Expressions para mapear os passos.
# Além de mapear, podemos utilizar expressões para definir variáveis que serão argumentos para os steps
#  () - Grupo/Agrupar
#  .* - Qualquer sequência de caracteres --> blog_link

# -> "(.*)" - em navigation.feature, no step 'when', o que estiver dentro das " " será a nossa RE
# -> "(.*)" --> "blog_link"
# Nossa expressão regular será passada como arg para a funcão step_impl() , junto com context.browser
# O próprio Python interpreta a nossa RE como o segundo parametro que deve ser passado para a função, o 'link_id'.


@when('I click on "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [link for link in links if link.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()
