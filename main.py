from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


# Opens the browser
browser = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

# Go to page url
browser.get("https://10fastfingers.com/typing-test/italian")

# Wait 5 sec because yes, shut up
time.sleep(5)

# Cookies button
cookies = browser.find_element_by_xpath("//*[@id=\"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll\"]")
cookies.click()

# ------------------------------------------------- SINGLE -------------------------------------------------------------

def singleplayer():
    # Input box, where the bot has to write
    input_box = browser.find_element_by_xpath("//*[@id=\"inputfield\"]")

    # Time variabiles for the timed while loop
    start_time = time.time()
    print("Started: " + str(start_time))
    seconds = 60

    # Just for fun
    word_list = []

    # While variabiles
    i = 1
    running = True

    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        word = browser.find_element_by_xpath("//*[@id=\"row1\"]/span[" + str(i) + "]").text

        time.sleep(0.30)

        if word != '':
            word_list.append(word)

            input_box.send_keys(word)
            input_box.send_keys(Keys.SPACE)

            i += 1
        else:
            running = False

        if elapsed_time > seconds:
            print("Finished")
            running = False

    # Just for fun part 2
    print(word_list)

# ------------------------------------------------- MULTI --------------------------------------------------------------

def multiplayer():
    multiplayer_box = browser.find_element_by_xpath("//*[@id=\"sidebar-md-lg\"]/div[1]/a[4]")
    multiplayer_box.click()

    click_here_button = browser.find_element_by_xpath("//*[@id=\"main\"]/div/div[1]/a")
    click_here_button.click()

    username_box = browser.find_element_by_xpath("//*[@id=\"username\"]")
    username_box.send_keys("marcoigorr")

    enter_button = browser.find_element_by_xpath("//*[@id=\"auth\"]/input[2]")
    enter_button.click()

    time.sleep(10)

    # Ready to type

    input_box = browser.find_element_by_xpath("//*[@id=\"game\"]/div[3]/div[2]/div[2]/div[1]/input")

    # Time variabiles for the timed while loop
    start_time = time.time()
    print("Started: " + str(start_time))
    seconds = 60

    # While variabiles
    i = 1
    running = True

    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        word = browser.find_element_by_xpath("//*[@id=\"game\"]/div[3]/div[2]/div[1]/div/span[" + str(i) + "]").text

        time.sleep(0.52)

        if word != '':
            input_box.send_keys(word)
            input_box.send_keys(Keys.SPACE)

            i += 1
        else:
            running = False

        if elapsed_time > seconds:
            print("Finished")
            running = False

# ------------------------------------------------- MAIN ---------------------------------------------------------------

multiplayer()
