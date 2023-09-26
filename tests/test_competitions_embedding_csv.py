from kmai.adapters.stubs.stub_csv_writer import StubCSVWriter
from kmai.adapters.stubs.stub_kaggle_dowloader import StubKaggleDownloader
from kmai.adapters.stubs.stub_llm_caller import StubLLMCaller
from kmai.adapters.stubs.stub_competition_scrapper import StubCompetitionScrapper
from kmai.adapters.stubs.stub_csv_reader import StubCSVReader
from kmai.use_cases.get_competitions import create_competitions_embedding_csv, update_competitions_embedding

from kmai.config import settings

def test_create_competitions_embedding_csv_simple():
    # we want to download the csv from kaggle, scrap each competition description, transform them as correct text, embed them to finally store them in the csv
    df = create_competitions_embedding_csv(
        StubKaggleDownloader(), StubCompetitionScrapper(), StubLLMCaller(), StubCSVWriter()
    )

    assert "desc_embedding" in df
    assert len(df) > 0 and len(df) < settings.INITIAL_COMPETITION_NUMBER
    assert all(isinstance(item, list) for item in df["desc_embedding"])

def test_update_competitions_embedding_csv():
    df = update_competitions_embedding(StubCompetitionScrapper(), StubLLMCaller(), StubCSVReader(), StubCSVWriter())

    assert "desc_embedding" in df
    assert all(isinstance(item, list) for item in df["desc_embedding"])
