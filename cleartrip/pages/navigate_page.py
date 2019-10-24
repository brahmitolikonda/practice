from utils.Browser import *




class navigate:
    def navigate_trainspage(self,driver):
        driver.find_element_by_xpath("//a[contains(text(),'Trains')]").click() 