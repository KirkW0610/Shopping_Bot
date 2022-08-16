from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Bot Check point #1

# Goes to DualSense 5 controller, replace with PS5 link
driver.get("https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815")
driver.maximize_window()
print(driver.title)


add_to_cart = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button")
add_to_cart.send_keys(Keys.ENTER)

checkout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]")))
checkout.send_keys(Keys.RETURN)

# Bot Check point #2 put time.sleep
time.sleep(5)

# Bot will input both email and password, then login. PLEASE PLACE INFO IN BLANK QUOTATION MARKS!!!
email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sign-in-email")))
email.send_keys("{email address}")

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[2]/div/div[1]/label/div[2]/div/input")))
password.send_keys("{password}")

signin_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[5]/button ")))
signin_confirm.click()


delivery_cont = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button")))
delivery_cont.send_keys(Keys.RETURN)

delivery_cont_two = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button")))
delivery_cont_two.click()

time.sleep(2)

cvv_info = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "cvv-confirm")))
cvv_info.send_keys("{cvv}")

review_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button")))
review_button.click()


place_order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,
    "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button")))
place_order.click()

# CONGRATS YOU'VE PLACED YOUR ORDER!!!
time.sleep(10)

# close tab
driver.close()
