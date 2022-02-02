from behave import *

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    link = [l for l in page.navigation if l.text == link_text]

    if len(link) > 0:
        link[0].click()
    else:
        raise RuntimeError()

