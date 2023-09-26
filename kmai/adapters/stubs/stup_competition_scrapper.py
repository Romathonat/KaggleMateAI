import pandas as pd

from kmai.ports.competition_scrapper import CompetitionScrapper


class StubCompetitionScrapper(CompetitionScrapper):
    def get_competition_text(self, url: str) -> str:
        return "This is a text description from a competition"
