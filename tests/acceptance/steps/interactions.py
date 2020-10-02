from behave import *
from time import sleep

from selenium.webdriver.common.by import By

from tests.acceptance.page_models.base_page import BasePage

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

    sleep(0.7)
