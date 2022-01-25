from behave import *
from selenium import webdriver

use_step_matcher('re')


@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()

