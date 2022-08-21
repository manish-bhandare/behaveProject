import time

from behave import *
from selenium import webdriver


@given('Launch chrome')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('Open HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensourse-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    # context.driver.find_element("id", "txtUsername").send_keys().clear()
    # context.driver.find_element("id", "txtPassword").send_keys().clear()
    context.driver.find_element("id", "txtUsername").send_keys(user)
    context.driver.find_element("id", "txtUsername").send_keys(pwd)


@when('Click Login button')
def step_impl(context):
    context.driver.find_element("id", "btnLogin").click()


@then('Dashboard page')
def step_impl(context):
    text = context.driver.find_element("xpath",
                                       '//span[.="The License to Use OrangeHRM Has Expired!. Please Contact OrangeHRM for an Updated License."]')
    assert text
    time.sleep(5)
    context.driver.close()
