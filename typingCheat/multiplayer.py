from selenium.webdriver.common.keys import Keys

import random
import time
# ------------------------------------------------- MULTI --------------------------------------------------------------

def start(browser):
    try:
        multiplayer_box = browser.find_element_by_xpath("//*[@id=\"sidebar-md-lg\"]/div[1]/a[4]")
        multiplayer_box.click()

        time.sleep(1)
        click_here_button = browser.find_element_by_xpath("//*[@id=\"main\"]/div/div[1]/a")
        click_here_button.click()

        time.sleep(1)
        username_box = browser.find_element_by_xpath("//*[@id=\"username\"]")
        username_box.send_keys("marcoigorr")

        time.sleep(1)
        enter_button = browser.find_element_by_xpath("//*[@id=\"auth\"]/input[2]")
        enter_button.click()

        # ---------------------- Ready to type

        # count down to start
        countDown = browser.find_element_by_xpath("/html/head/title").text

        # This is where to spam
        input_box = browser.find_element_by_xpath("//*[@id=\"game\"]/div[3]/div[2]/div[2]/div[1]/input")

        def isRunning():
            if countDown == '':
                # Time variabiles for the timed while loop
                start_time = time.time()
                print("Started: " + str(start_time))
                seconds = 60

                return True
            else:
                return isRunning()

        # While variabiles
        i = 1
        running = True

        while isRunning():
            current_time = time.time()
            elapsed_time = current_time - start_time

            # Wait between words
            time.sleep(random.uniform(0.35, 0.6))

            # Random number for random error
            random_number = random.randint(1, 20)

            # Get the word
            word = browser.find_element_by_xpath("//*[@id=\"game\"]/div[3]/div[2]/div[1]/div/span[" + str(i) + "]").text

            if random_number != 5: # Random error
                if word != '':
                    input_box.send_keys(word)
                    input_box.send_keys(Keys.SPACE)

                    i += 1
                else:
                    running = False
            else:
                word += "f"

                input_box.send_keys(word)
                input_box.send_keys(Keys.SPACE)

            # If 60 sec passed, then stop
            if elapsed_time > seconds:
                print("Finished")
                running = False

    # Annoying error
    except DeprecationWarning:
        pass