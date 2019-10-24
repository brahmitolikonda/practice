from utils.Browser import *
from components.train_data import *
from pages.trains import trains_input
import time


class train_database:
    def from_station(self,driver):
        trains_input().fromstation(driver)
        
    def to_station(self,driver):
        trains_input().tostation(driver)
        
    def select_Class(self,driver):
        trains_input().select_class(driver)
        time.sleep(2)
    def date_ofjourney(self,driver):
        trains_input().select_datejourney(driver)
        time.sleep(1)
        
    def no_of_pass(self,driver):
        trains_input().ticket_qnty(driver)
        time.sleep(1)
        
    def submit(self,driver):
        trains_input().submit_trains(driver)
        
    def train_details(self,driver):
        train_database().from_station(driver)
        train_database().to_station(driver)
        train_database().select_Class(driver)
        train_database().date_ofjourney(driver)
        train_database().no_of_pass(driver)
        train_database().submit(driver)