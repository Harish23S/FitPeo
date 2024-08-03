import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def go_to(url, browser_type=None):
    if not browser_type:
        driver = webdriver.Edge()
    elif browser_type.lower() == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean the url and go to the url
    url = url.strip()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def assert_page_title(context, expected_title):
    actual_title = context.driver.title
    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)
    print("The page title is as expected.")


def assert_current_url(context, expected_url):
    current_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url, "The current url is not as expected." \
                                        " Actual: {}, Expected: {}".format(current_url, expected_url)

    print("The page url is as expected.")


def find_element(context, locator_attribute, locator_text):

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)


def is_element_visible(element):

    if element.is_displayed():
        return True
    else:
        return False


def assert_element_visible(element):

    if not element.is_displayed():
        raise AssertionError('The element is not displayed')


def click_item(context, locator_attribute, locator_text):
    element = context.driver.find_element(locator_attribute, locator_text)
    element.click()
    time.sleep(2)
    return True


def adjust_range(context, expected_value, locator_type, locator_text):
    item = context.driver.find_element(locator_type, locator_text)
    actions = ActionChains(context.driver)
    actions.move_to_element(item).perform()
    actions.click_and_hold(item).move_by_offset(93, 0).release().perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()

    if item.get_attribute('value') == expected_value:
        return True
    else:
        print("Value is varying")
        return False


def adjust_ranges(context, expected_value, locator_type, locator_text):
    item = context.driver.find_element(locator_type, locator_text)
    actions = ActionChains(context.driver)
    actions.move_to_element(item).perform()
    actions.click_and_hold(item).move_by_offset(39, 0).release().perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    time.sleep(2)

    if item.get_attribute('value') == expected_value:
        return True
    else:
        print("Value is varying")
        return False


def compare_the_values(context, locator_type1, locator_text1, locator_type2, locator_text2):

    item1 = context.driver.find_element(locator_type1, locator_text1)
    item2 = context.driver.find_element(locator_type2, locator_text2)

    if item1.get_attribute('value') == item2.get_attribute('value'):
        return True
    else:
        print("the Values are varying")
        return False


def set_value(context, expected_value, locator_type, locator_text):
    item = context.driver.find_element(locator_type, locator_text)
    item.click()
    act = ActionChains(context.driver)
    while expected_value != item.get_attribute('value'):
        if expected_value > item.get_attribute('value'):
            act.key_down(Keys.ARROW_UP).perform()
            if expected_value == item.get_attribute('value'):
                act.key_up(Keys.ARROW_UP).perform()
        else:
            act.key_down(Keys.ARROW_DOWN).perform()
            if expected_value == item.get_attribute('value'):
                act.key_up(Keys.ARROW_DOWN).perform()

    return True


def final_output(context, locator_type, locator_text, check_value):
    item = context.driver.find_element(locator_type, locator_text)
    text = item.text
    dollar_amount = "$"+text.strip('$')
    print(dollar_amount)
    if dollar_amount == str(check_value):
        return True
    else:
        print("the Values are varying")
        return False

