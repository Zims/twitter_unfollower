from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import secret


driver = webdriver.Chrome('.//chromedriver')  
# Specify your PATH to chromedriver, if not specified will search path.

driver.get(secret.MY_URL) #<- url of profile_USER/following
# secret.MY_URL is eaqual to https://twitter.com/USER/following/
# change to your account name instead of USER

log_in_button = driver.find_element_by_link_text("Log in")
log_in_button.click()


try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input'))
        
    )
    input_user = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input')
    input_user.send_keys(secret.USER) #<-Username or login email goes here

    input_pass = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input')
    input_pass.send_keys(secret.PASS, Keys.ENTER)
                        #|^||^||^|password here
                        # DON'T SHARE THIS!!! Share link to my github instead.
finally:
    print('logged in!!')
    driver.implicitly_wait(10) #gives an implicit wait for 10 seconds

def unfollow_one():
    # i need to get the next element. Because it clicks it again on the next cycle.
    stop_following = driver.find_element_by_xpath('//div[2]/div/div/span/span')
    stop_following.click()
    try:
        element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > div > div > div.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-1dbjc4n.r-1awozwy.r-1kihuf0.r-18u37iz.r-1pi2tsx.r-1777fci.r-1pjcn9w.r-fxte16.r-1xcajam.r-ipm5af.r-9dcw1g > div.css-1dbjc4n.r-1awozwy.r-14lw9ot.r-t23y2h.r-1jgb5lz.r-pm9dpa.r-1ye8kvj.r-1rnoaur.r-d9fdf6.r-1sxzll1.r-13qz1uu > div.css-1dbjc4n.r-18u37iz.r-13qz1uu > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-16y2uox.r-1w2pmg.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span')))
        agree = driver.find_element_by_css_selector('#react-root > div > div > div.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-1dbjc4n.r-1awozwy.r-1kihuf0.r-18u37iz.r-1pi2tsx.r-1777fci.r-1pjcn9w.r-fxte16.r-1xcajam.r-ipm5af.r-9dcw1g > div.css-1dbjc4n.r-1awozwy.r-14lw9ot.r-t23y2h.r-1jgb5lz.r-pm9dpa.r-1ye8kvj.r-1rnoaur.r-d9fdf6.r-1sxzll1.r-13qz1uu > div.css-1dbjc4n.r-18u37iz.r-13qz1uu > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-16y2uox.r-1w2pmg.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span')
        agree.click()
        driver.refresh()
    finally:
        print('done')

i = 0
# set the number of accounts to unfollow bellow. default is 5
while i < 500: 
    unfollow_one()
    time.sleep(1)
    i += 1