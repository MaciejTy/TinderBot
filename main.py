from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

FB_EMAIL = "YOUR FB MAIL"
FB_PASSWORD = "YOUR FB PASSWORD"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
driver.maximize_window()

login_button = driver.find_element(By.XPATH, value='//*[@id="t-1364086984"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

sleep(3)

fb_button = driver.find_element(By.XPATH, '//*[@id="t-1142746548"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
fb_button.click()

sleep(3)

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]

driver.switch_to.window(fb_window)
sleep(3)

cookies = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]')
cookies.click()


fb_login = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_login.send_keys(FB_EMAIL)
sleep(3)

fb_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_password.send_keys(FB_PASSWORD)
sleep(3)

login = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
login.click()

sleep(10)

driver.close()
driver.switch_to.window(base_window)

sleep(3)

allow_button = driver.find_element(By.XPATH, '//*[@id="t-1142746548"]/div/div[1]/div/div/div[3]/button[1]')
allow_button.click()
sleep(3)

not_now_button = driver.find_element(By.XPATH, '//*[@id="t-1142746548"]/div/div[1]/div/div/div[3]/button[2]')
not_now_button.click()

sleep(3)

privacy_button = driver.find_element(By.XPATH, '//*[@id="t-1364086984"]/div/div[2]/div/div/div[1]/div[1]/button')
privacy_button.click()
sleep(3)

like_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')

for n in range(100):
    try:
        like_button.click()
        sleep(1)

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.XPATH, value='//*[@id="t-1907619177"]/div/div/div[1]/div/div[3]/button')
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

