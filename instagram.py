import time
from selenium import webdriver

#Specify the path to the chrome webdriver
driver = webdriver.Chrome("./chromedriver")


def dismiss_modal():
    try:
        driver.find_element_by_class_name("aOOlW.HoLwm").click()
    except:
        pass

def login(username, password):
    driver.get("https://www.instagram.com")
    driver.find_element_by_link_text("Log in").click()
    time.sleep(1)
    user_input = driver.find_element_by_name("username")
    user_input.send_keys(username)
    pass_input = driver.find_element_by_name("password")
    pass_input.send_keys(password)
    time.sleep(1)
    driver.find_element_by_class_name("_0mzm-.sqdOP.L3NKy").click()
    time.sleep(4)
    driver.find_element_by_class_name("aOOlW.HoLwm").click()
    time.sleep(1)

def search(whattosearch):
    search_input = driver.find_element_by_class_name("XTCLo.x3qfX")
    search_input.send_keys(whattosearch)
    time.sleep(1)
    driver.find_element_by_class_name("yCE8d").click()
    time.sleep(1)
    i = 0
    while(True):
        i += 1000
        images = driver.find_elements_by_class_name("v1Nh3.kIKUG._bz0w")
        for image in images:
            clickable = image.find_element_by_xpath('./following::a')
            clickable.click()
            time.sleep(2)
            button = driver.find_element_by_class_name("dCJp8.afkep._0mzm-")
            try:
                button.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9.u-__7')
                button.click()
            except:
                pass
            driver.find_element_by_class_name("ckWGn").click()
        driver.execute_script("window.scrollTo(0, {});".format(i))


login("username", "password")
search("#OneCoolHashtag")

 #                 Igw0E     IwRSH      eGOV_         _4EzTm