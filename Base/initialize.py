from appium import webdriver
from time import sleep
from appium.options.ios import XCUITestOptions

def isInstalled_read(is_installed_path):
    with open(is_installed_path, 'r') as file:
        content = file.read()
    return content

def isInstalled_write(is_installed_path, content):
    content = content.replace('0', '1')
    with open(is_installed_path, 'w') as file:
        file.write(content)

def launch_app(app_bundle_id, appium_server_url, platformName, platformVersion, deviceName, udid):
    options = XCUITestOptions().load_capabilities(
         {
            'platformName': platformName,
            'platformVersion': platformVersion,
            'deviceName': deviceName,
            'bundleId': app_bundle_id,
            'udid': udid,
            'automationName': 'XCUITest',
            'noReset': True
        }
    )
    driver = webdriver.Remote(
        command_executor=appium_server_url, options=options, direct_connection=True
    )
    sleep(3)
    click_continue_button(driver)
    return driver

def is_app_installed(is_installed_path):
    content = isInstalled_read(is_installed_path)
    return content.strip() == '1'

def install_and_open_app(app_bundle_id, appium_server_url, platformName, platformVersion, deviceName, udid, app_path, is_installed_path):
    if is_app_installed(is_installed_path):
        print("App is already installed. Opening the app.")
        driver = launch_app(app_bundle_id, appium_server_url, platformName, platformVersion, deviceName, udid)
    else:
        print("App is not installed. Installing and opening the app.")
        options = XCUITestOptions().load_capabilities(
            {
                'app': app_path,
                'platformName': platformName,
                'platformVersion': platformVersion,
                'deviceName': deviceName,
                'bundleId': app_bundle_id,
                'udid': udid,
                'automationName': 'XCUITest',
                'noReset': True
            }
        )
        driver = webdriver.Remote(
            command_executor=appium_server_url, options=options, direct_connection=True
        )
        click_continue_button(driver)
        content = isInstalled_read(is_installed_path)
        isInstalled_write(is_installed_path, content)
    return driver

def is_termsOfUse_page(driver):
    element_exists = False
    button_continue = None
    try:
        button_continue = driver.find_element('name', 'Continue')
        element_exists = True
    except:
        pass
    return element_exists, button_continue

def click_continue_button(driver):
    element_exists, button_continue = is_termsOfUse_page(driver)
    if element_exists:
        button_continue.click()
        sleep(3)
