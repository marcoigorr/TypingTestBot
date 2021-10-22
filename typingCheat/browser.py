from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def getBrowser():
    try:
        # Opens the browser
        browser = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

        # Go to page url
        browser.get("https://10fastfingers.com/typing-test/italian")

        # Wait 5 sec because yes, shut up
        time.sleep(2.5)

        # Cookies button
        cookies = browser.find_element_by_xpath("//*[@id=\"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll\"]")
        cookies.click()

        return browser

    except DeprecationWarning:
        pass
