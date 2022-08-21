from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    # context.driver = webdriver.Chrome(executable_path='/home/bum/Documents/data to learn/BDD/Drivers/chromedriver')
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensourse-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element("xpath",
                                         '//img[@src="/webres_5f1a894b17d853.72525894/themes/6x-demo-responsive/images/login/logo_ent.png"]').is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()
