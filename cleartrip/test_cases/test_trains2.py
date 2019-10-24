from utils.Browser import *
from pages.verify_homepage import *
from pages.navigate_page import *
from pages.trains import trains_input
from components.train_data import train_database




def test_trains():
    
    driver=Browser_utils().openBrowser()
    Browser_utils().invokeApp(driver)
    verifyPage().verifyHome(driver)          #verifyHome of cleartrip       
    navigate().navigate_trainspage(driver)   #navigate_trainspage()               
    verifyPage().verifyTrainpage(driver)    #verifyTrainpage() 
    train_database().train_details(driver)     #searchTrains()
    verifyPage().verifyProgram(driver)       #verifytrainlist()
    Browser_utils().closeBrowser(driver)

    
def test_trains2():
    
    driver=Browser_utils().openBrowser()
    Browser_utils().invokeApp(driver)
    verifyPage().verifyHome(driver)          #verifyHome of cleartrip       
    navigate().navigate_trainspage(driver)   #navigate_trainspage()               
    verifyPage().verifyTrainpage(driver)    #verifyTrainpage() 
    train_database().train_details(driver)     #searchTrains()
    verifyPage().verifyProgram(driver)       #verifytrainlist()
    Browser_utils().closeBrowser(driver)
