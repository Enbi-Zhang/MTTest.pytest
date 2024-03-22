def quit_driver(driver, app_bundle_id):
    driver.terminate_app(app_bundle_id)
    print("Close app.")
    if driver is not None:
        driver.quit()
        print("Close driver.")

