from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Browser_utils:
    
    def openBrowser(self):
        driver=webdriver.Chrome(executable_path="C:/Users/Brahmi/eclipse-workspace/project2/driver/chromedriver.exe")
        driver.maximize_window()
        return driver
    
    
    def invokeApp(self,driver):
        driver.get("https://www.cleartrip.com")
        
    def closeBrowser(self,driver):
        driver.quit()
        