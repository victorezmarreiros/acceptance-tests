from behave import *

use_step_matcher('re')

# Utilizando Regular Expressions para mapear os passos.
# Além de mapear, podemos utilizar expressões para definir variáveis que serão argumentos para os steps
#  () - Grupo/Agrupar
#  .* - Qualquer sequência de caracteres --> blog_link

# -> "(.*)" - em navigation.feature, no step 'when', o que estiver dentro das " " será a nossa RE
# -> "(.*)" --> "blog_link"
# Nossa expressão regular será passada como arg para a funcão step_impl() , junto com context.browser
# O próprio Python interpreta a nossa RE como o segundo parametro que deve ser passado para a função, o 'link_id'.


@when('I click on the link with id "(.*)"')  #
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()
