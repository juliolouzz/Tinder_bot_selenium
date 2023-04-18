import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# These two lines under only work if chrome is not open --> to login into your Google account and use your cookies, etc.
options.add_argument(r'--user-data-dir=C:\Users\Julio PC\AppData\Local\Google\Chrome\User Data')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://tinder.com/app/recs")

sleep(5)
dislike = driver.find_element(By.XPATH,
                              '//*[@id="c964396036"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')

like = driver.find_element(By.XPATH,
                           '//*[@id="c964396036"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')

bot_on = True


# use this function to keep disliking forever!!!
# def not_like():
#     while bot_on:
#         try:
#             sleep(1)
#             dislike.click()
#         except NoSuchElementException:
#             sleep(5)
#             continue


def i_like():
    while bot_on:
        try:
            sleep(1)
            like.click()
        except ElementClickInterceptedException:
            # You got a match
            try:
                sleep(2)
                match_close_btn = driver.find_element(By.XPATH,
                                                      '//*[@id="c1294767237"]/main/div/div[1]/div/div[4]/button')
                match_close_btn.click()
                sleep(2)
                continue
            except NoSuchElementException:
                # they ask you to see your likes
                try:
                    sleep(2)
                    maybe_later_like_btn = driver.find_element(By.XPATH,
                                                               '//*[@id="c-763985040"]/main/div/div/div[3]/button[2]')
                    maybe_later_like_btn.click()
                    sleep(2)
                    continue
                except NoSuchElementException:
                    try:
                        # out of likes today
                        sleep(2)
                        close_offer_btn = driver.find_element(By.XPATH,
                                                              '//*[@id="c-763985040"]/main/div/div[3]/button[2]')
                        close_offer_btn.click()
                        driver.quit()
                        break
                    except StaleElementReferenceException:
                        # out of likes today
                        sleep(2)
                        close_offer_btn = driver.find_element(By.XPATH,
                                                              '//*[@id="c-763985040"]/main/div/div[3]/button[2]')
                        close_offer_btn.click()
                        driver.quit()
                        break


i_like()
