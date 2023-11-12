from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from kmai.ports.icompetition_scrapper import ICompetitionScrapper


class sibling_content_loaded:
    def __init__(self, sibling_id):
        self.sibling_id = sibling_id
        self.prev_content = None

    def __call__(self, driver):
        sibling = driver.find_element(
            By.XPATH, f'//*[@id="{self.sibling_id}"]/following-sibling::div[1]'
        )
        curr_content = sibling.get_attribute("innerHTML")
        if self.prev_content == curr_content:
            return True
        self.prev_content = curr_content
        return False


class CompetitionScrapper(ICompetitionScrapper):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("ignore-certificate-errors")
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def __del__(self):
        self.driver.quit()

    def get_competition_text(self, url: str) -> str:
        print(url)
        self.driver.get(url)
        WebDriverWait(self.driver, 10, poll_frequency=2).until(
            sibling_content_loaded("abstract")
        )

        # soup = BeautifulSoup(self.driver.page_source, 'html.parser').find("div", {"id": "background"}).find_parent("div")
        soup = (
            BeautifulSoup(self.driver.page_source, "html.parser")
            .find("div", id="abstract")
            .find_next_sibling("div")
        )
        return soup.get_text()
