from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import datetime


class Resultados:
    def __init__(self, matches):
        self.matches = matches
        self.url = 'https://www.adamchoi.co.uk/teamgoals/detailed'
        self.path = 'chromedriver.exe'
        self.driver = webdriver.Chrome(self.path)
        self.resultados = []

    def getElement(self):
        self.driver.get(self.url)
        btn_all_matches = self.driver.find_element(By.XPATH, '(//label)[12]')
        btn_all_matches.click()
        select = self.driver.find_element(By.ID, 'country')
        select.click()
        select.send_keys('Brazil')
        select.click()
        self.matches = self.driver.find_elements(By.TAG_NAME, 'tr')

    def showResults(self):
        for match in self.matches:
            self.resultados.append({f'{match.text} \n'})

    def buildResults(self):
        dateTime = datetime.datetime.now()
        df = pd.DataFrame({f'Resultados do dia: {dateTime}': self.resultados})
        df.to_csv('resultados.csv', index=False)


