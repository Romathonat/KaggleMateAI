from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from kmai.ports.icompetition_scrapper import ICompetitionScrapper

class CompetitionScrapper(ICompetitionScrapper):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("ignore-certificate-errors")
        # self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def __del__(self):
        self.driver.quit()

    def get_competition_text(self, url: str) -> str:
        print(url)
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            # EC.presence_of_element_located((By.ID, "background"))
            EC.presence_of_element_located((By.CLASS_NAME, "sc-fOVJBw"))
        )
        # soup = BeautifulSoup(self.driver.page_source, 'html.parser').find("div", {"id": "background"}).find_parent("div")
        soup = BeautifulSoup(self.driver.page_source, 'html.parser').find("div", class_="sc-fOVJBw")
        return soup.get_text()

