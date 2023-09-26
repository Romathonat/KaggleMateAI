from kmai.adapters.stubs.stub_csv_writer import StubCSVWriter
from kmai.adapters.stubs.stub_kaggle_dowloader import StubKaggleDownloader
from kmai.adapters.stubs.stub_llm_caller import StubLLMCaller
from kmai.adapters.stubs.stup_competition_scrapper import StubCompetitionScrapper
from kmai.use_cases.get_competitions import get_competitions_embedding_csv


def test_get_competitions_embedding_csv_simple():
    # we want to download the csv from kaggle, scrap each competition description, transform them as correct text, embed them to finally store them in the csv
    df = get_competitions_embedding_csv(
        StubKaggleDownloader(), StubCompetitionScrapper(), StubLLMCaller(), StubCSVWriter()
    )

    assert "desc_embedding" in df
    assert len(df) > 0
    assert all(isinstance(item, list) for item in df["desc_embedding"])
