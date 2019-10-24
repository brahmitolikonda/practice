from utils.Browser import *
from selenium.webdriver.support.select import Select
import time

class trains_input:
    def fromstation(self,driver):
        driver.find_element_by_id("from_station").send_keys("Hyderabad Decan (HYB)")
        
    def tostation(self,driver):
        driver.find_element_by_id("to_station").send_keys("Nellore (NLR)")
    def select_class(self,driver):
        Select(driver.find_element_by_id("trainClass")).select_by_index(8)
        
    def select_datejourney(self,driver):
        driver.find_element_by_xpath("//a[@class='cal_openLink']//img").click()
        time.sleep(2)
        driver.find_element_by_xpath("//td[@class='weekend']//a[contains(text(),'26')]").click()
        
    def ticket_qnty(self,driver):
        Select(driver.find_element_by_id("train_adults")).select_by_index(3)
    
    
    def submit_trains(self,driver):
        driver.find_element_by_id("trainFormButton").click()