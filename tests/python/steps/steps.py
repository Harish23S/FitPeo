from behave import given, when, then
from BDDCommon.CommonSteps.webstepscommon import *
from BDDCommon.CommonConfigs import locatorsconfig
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig


@given('I go to the site "{site}"')
def go_to_url(context, site):
    url = urlconfig.URLCONFIG.get(site)
    print("Navigating to the site: {}".format(url))
    context.driver = webcommon.go_to(url)


@then('"{item}" should be visible')
def verify_nav_bars_visible(context, item):

    exists = check_true_from_locator(item)

    if exists:
        locator_info = locatorsconfig.LOCATORS.get(item)
        locator_type = locator_info['type']
        locator_text = locator_info['locator']
        nav_element = webcommon.find_element(context, locator_type, locator_text)
        webcommon.assert_element_visible(nav_element)


@then('click the "{item_name}"')
def clicking_the_item(context, item_name):
    exists = check_true_from_locator(item_name)

    if exists:
        locator_info = locatorsconfig.LOCATORS.get(item_name)
        locator_type = locator_info['type']
        locator_text = locator_info['locator']
        result = webcommon.click_item(context, locator_type, locator_text)

        if result:
            print("The {} has been clicked".format(item_name))
        else:
            print("not able to find the {}".format(item_name))


@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context, expected_url)


@then('Set the "{item}" value to "{expected_value}"')
def adjust_value(context, expected_value, item):
    exists = check_true_from_locator(item)

    if exists:
        locator_info = locatorsconfig.LOCATORS.get(item)
        locator_type = locator_info['type']
        locator_text = locator_info['locator']
        if item == 'Slider':
            result = webcommon.adjust_range(context, expected_value, locator_type, locator_text)
        else:
            result = webcommon.set_value(context, expected_value, locator_type, locator_text)
        assert result, "Value not able to set"
        print("The value has been set")


@then('Set the "{item}" value "{expected_value}"')
def adjust_value(context, expected_value, item):
    exists = check_true_from_locator(item)

    if exists:
        locator_info = locatorsconfig.LOCATORS.get(item)
        locator_type = locator_info['type']
        locator_text = locator_info['locator']
        result = webcommon.adjust_ranges(context, expected_value, locator_type, locator_text)
        assert result, "Value not able to set"
        print("The value has been set")


def check_true_from_locator(item_name):
    expected_items = ['Revenue Calculator', 'Slider section', 'Slider', 'final value', 'inputValue', 'CPT1', 'CPT2', 'CPT3', 'CPT4']

    if item_name not in expected_items:
        raise Exception("The passed in nav_bar type is not one of expected."
                        "Actual: {}, Expected in: {}".format(item_name, expected_items))
    else:
        return True


@then('Compare with "{value1}" and "{value2}"')
def compare(context, value1, value2):

    exist1 = check_true_from_locator(value1)
    exist2 = check_true_from_locator(value2)

    if exist1 and exist2:
        locator_info1 = locatorsconfig.LOCATORS.get(value1)
        locator_info2 = locatorsconfig.LOCATORS.get(value2)
        locator_type1 = locator_info1['type']
        locator_text1 = locator_info1['locator']
        locator_type2 = locator_info2['type']
        locator_text2 = locator_info2['locator']

        result = webcommon.compare_the_values(context, locator_type1, locator_text1, locator_type2, locator_text2)
        assert result, "The values are varying please check"
        print("The Values are same")


@then('Compare the "{finalValue}" with "{checkValue}"')
def compare_the_final(context, finalValue, checkValue):
    exist = check_true_from_locator(finalValue)

    if exist:
        locator_info = locatorsconfig.LOCATORS.get(finalValue)
        locator_type = locator_info['type']
        locator_text = locator_info['locator']
        webcommon.final_output(context, locator_type, locator_text, checkValue)
