from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from urllib.request import urlretrieve

#You should be using Robot to send all of your key presses to the system level Alert. Including your user and PW.
#A security dialogue is not a JavaScript level dialogue box

def searchpage():
	global namelist
	search = driver.find_elements_by_class_name("profile-link")
	for result in search:
		namelist.append(result.text)

	search3 = driver.find_elements_by_xpath("//div[contains(@class, 'result item-list-people relative')]//img[contains(@src,'profile')]") #get photos
	search4 = driver.find_elements_by_xpath("//img[contains(@src,'profile')]/../../following-sibling::h4[1]")  #moves from Img embedded in<a> (1 level) embedded in <span> (2 levels), and search for next h4 #get names of these photos
	count=0
	for result in search3:
		count=count+1
		photolist.append(search4[count-1].text)
		
		imgurl=result.get_attribute('src')
		#urlretrieve(imgurl, imgurl[imgurl.rfind('/')+1:])
		urlretrieve(imgurl, search4[count-1].text+".jpg")

driver = webdriver.Firefox()

driver.get('http://homeport.rccl.com/people-finder/?query=85000731')
wait(driver, 5).until(EC.alert_is_present())
alert = driver.switch_to.alert#switch_to_alert()
#alert.authenticate('AUS\\7002079', )

alert.send_keys('AUS\\7002079')
alert.send_keys(Keys.TAB)
sleep(6)

#alert.send_keys('yourpassword')  #bug, didn't work, supply manually
alert.accept()

#alert.authenticateUsing(new UserAndPassword(username, password))


#driver.get("https://AUS%5C7002079:@homeport.rccl.com/people-finder/?query=85000731") #%5C is encoding back slash


#driver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


#e=driver.find_element_by_id('body')
#e.click

print (driver.page_source)
#driver.navigate().refresh();


sleep(10)

actions = ActionChains(driver)
actions.send_keys(Keys.ESCAPE)
actions.perform()
#print (driver.page_source)
namelist=[]
photolist=[]


nextpage=driver.find_elements_by_xpath("//li[@class='copy next']/a[1]")

while nextpage:
	nextpage[0].click()
	searchpage()
	nextpage=driver.find_elements_by_xpath("//li[@class='copy next']/a[1]")
#//div[contains(@class, "myClass")]/img/@src

#https://homeport.rccl.com/people-finder/?query=85000731&pg=2

print (namelist)
print (photolist)