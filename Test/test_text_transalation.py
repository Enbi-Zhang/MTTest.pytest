import pytest
from time import sleep
from Base.initialize import install_and_open_app
from Base.quit_driver import quit_driver

@pytest.fixture
def driver(request):
    configuration_list = []
    with open('/Users/mttest2/PycharmProjects/pythonProject1_pytest/Base/configuration.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        parts = line.split('\t')
        after_tab = parts[1].strip()
        configuration_list.append(after_tab)

    app_bundle_id = configuration_list[0]
    appium_server_url = configuration_list[1]
    platformName = configuration_list[2]
    platformVersion = configuration_list[3]
    deviceName = configuration_list[4]
    udid = configuration_list[5]
    app_path = configuration_list[7]
    is_installed_path = configuration_list[6]

    driver = install_and_open_app(app_bundle_id, appium_server_url, platformName, platformVersion, deviceName, udid, app_path, is_installed_path)
    yield driver
    quit_driver(driver, app_bundle_id)

def test_text_translation(driver):
    print("Running text translation test case.")

    button_text_translation = driver.find_element('name', 'Text translation')
    button_text_translation.click()
    sleep(2)

    input_text = 'Hello, Translator!'
    text_input_box = driver.find_element('name', 'Enter English to translate')
    text_input_box.click()
    text_input_box.send_keys(input_text)
    sleep(2)

    button_send = driver.find_element('name', 'Send')
    button_send.click()
    sleep(2)

    translation_TTS_button = driver.find_element('name', 'PlaybackArrowFilled')

    if translation_TTS_button is not None:
        print("Can translate content by text mode.")
        print("Passed")
    else:
        print("Can not translate content by text mode.")
        print("Failed")
