import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

# Scenarios

scenarios('../features/cucumbers.feature')


# Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element("xpath", 'search_form_input_homepage')
    search_input.send_keys(phrase + Keys.RETURN)
# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element("id", 'links')
    assert len(links_div.find_elements("xpath", '//div')) > 0
    # Check search phrase
    search_input = browser.find_element('id', 'search_form_input')
    assert search_input.get_attribute('value') == phrase


@given("the google home page is displayed")
def google_search(browser):
    browser.get("https://google.com")
    browser.find_element("xpath","//div[text()='Accept all']").click()


@when(parsers.parse('the user searches for "{phrase}" on google'))
def google_search(browser, phrase):
    browser.find_element("xpath", "//input[@title='Search']").send_keys(phrase)
    # pytest.set_trace()
    # browser.find_element("xpath", "(//input[@name='btnK'])[1]").click()