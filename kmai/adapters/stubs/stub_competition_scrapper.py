from kmai.ports.icompetition_scrapper import ICompetitionScrapper


class StubCompetitionScrapper(ICompetitionScrapper):
    def get_competition_text(self, url: str) -> str:
        return "This is a text description from a competition"
