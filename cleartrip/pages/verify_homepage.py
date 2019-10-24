from utils.Browser import *
from selenium.webdriver.common.keys import Keys



class verifyPage:
    def verifyHome(self,driver):
        
        if driver.find_element_by_xpath("//h1[contains(text(),'Search flights')]").is_displayed():
            print("you are in flights page")
        else:
            print("you are not in flight page")
    
    def verifyTrainpage(self,driver):
        if driver.find_element_by_xpath("//*[@id='rail_search']/h1").is_displayed():
            print("You are in trains page")
        else:
            print("you are not in trains page")
    
    def verifyProgram(self,driver):
        if driver.find_element_by_id("close").is_displayed():
            print("program run Successfully")
        else:
            print("program not successfull")