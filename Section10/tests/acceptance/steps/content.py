from behave import *
from tests.acceptance.locators.homepage import HomePageLocators
from tests.acceptance.page_model.homepage import HomePage

use_step_matcher('re')


@then("There is a title shown on the page")
def step_impl(context):
    page = HomePage(context.browser)
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = HomePage(context.browser)

    assert page.title.text == content
