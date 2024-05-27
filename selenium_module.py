import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumHelper:
    def _init_(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.driver_path = self.config['driver_path']
        self.base_url = self.config['base_url']
        self.wait_time = self.config['wait_time']
        self.driver = None

    def setup_driver(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def find_element(self, by, value):
        return WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_element_located((by, value)))

    def teardown_driver(self):
        if self.driver:
            self.driver.quit()