from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://netpeak.ua/"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(link)
button1 = driver.find_element(By.XPATH, '//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]')
time.sleep(2)
button1.click()

button2 = driver.find_element(By.XPATH, '//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[3]/div/div[2]/ul[1]/li[3]/div/a')
time.sleep(2)
button2.click()


# button3 = driver.find_element(By.XPATH, '//*[@id="rec278626926"]/div/div/div[10]/a')
# button4 = driver.find_element(By.XPATH, '//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[2]/ul/li[1]/a')

# time.sleep(2)
# button1.click()

time.sleep(2)
button3 = driver.find_element(By.XPATH, '//*[@id="rec278626926"]/div/div/div[10]/a')
button3.click()
time.sleep(2)

#mainWindow = driver.getWindowHandles()
button4 = driver.find_element(By.XPATH, '//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[2]/ul/li[1]/a')
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
button4.click()


time.sleep(5)
login1 = driver.find_element(By.XPATH, '//input[@id="login"]')
login1.click
login = driver.find_element(By.XPATH, '//input[@id="login"]"]')

login.sendKeys("my name")
check = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[4]/div/md-checkbox/div[1]/div')
check.click()



