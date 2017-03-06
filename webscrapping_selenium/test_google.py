import os,time
from selenium import webdriver #We are importing selenium module..
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

print "start page " 

driver=webdriver.Chrome('chromedriver') #IE, firefox

driver.get("https://www.google.co.in/?gfe_rd=cr&ei=4nW9WMumBInT8geSt4iwCg&gws_rd=ssl") 

elment=driver.find_element_by_name("q")
elment.send_keys("python interview questions")
elment.send_keys(Keys.RETURN)
#time.sleep(5)
#links=driver.find_element_by_link_text("python")
links=driver.find_element_by_tag_name("a")
print links

for i in links:
	print i.get_attribute("href")


'''
elements = driver.find_element_by_link_text('8 Essential Python Interview Questions and Answers | Toptal').click()
driver.back()
time.sleep(5)
elements = driver.find_element_by_link_text('Python Interview Questions - TutorialsPoint').click()
driver.maximize_window()
time.sleep(5)
driver.set_window_position(10,10)
time.sleep(5)
'''
driver.quit()


#driver.quit()

'''
#
time.sleep(5)
print elements
driver.maximize_window()

print driver.current_url
driver.back()                                                                                                                                                                               
time.sleep(5)
driver.forward();
time.sleep(5)    
driver.set_window_position(10,10)
time.sleep(5)
driver.set_window_position(0,0)
time.sleep(5)
driver.refresh()
'''

