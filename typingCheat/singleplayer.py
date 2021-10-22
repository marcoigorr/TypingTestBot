from selenium.webdriver.common.keys import Keys

import random
import time
# ------------------------------------------------- SINGLE -------------------------------------------------------------

def start(browser):
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

        time.sleep(random.uniform(0.58, 1))

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