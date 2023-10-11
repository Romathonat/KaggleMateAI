from unittest.mock import patch

from kmai.adapters.stubs.stub_competition_scrapper import StubCompetitionScrapper
from kmai.adapters.stubs.stub_csv_reader import StubCSVReader
from kmai.adapters.stubs.stub_csv_writer import StubCSVWriter
from kmai.adapters.stubs.stub_kaggle_dowloader import StubKaggleDownloader
from kmai.adapters.stubs.stub_llm_caller import StubLLMCaller
from kmai.config import settings
from kmai.use_cases.data_preprocessing import (
    update_competitions_csv,
    update_competitions_descriptions,
)



def test_update_competitions_descriptions():
    df = update_competitions_descriptions(StubCompetitionScrapper(), StubCSVReader(), StubCSVWriter())

    assert all(isinstance(item, str) for item in df["description"])
    assert all(isinstance(item, str) for item in df["url"])
    assert df.iloc[-1]["url"].startswith(settings.KAGGLE_URL)


def test_update_competitions_csv():
    df_init_comp = StubCSVReader().read_csv("Competition.csv")
    df_download_comp, _ = StubKaggleDownloader().download_data()
    df_after_comp, df_after_topics = update_competitions_csv(StubKaggleDownloader(), StubCSVReader(), StubCSVWriter())

    assert df_after_comp.iloc[0]["Title"] == df_init_comp.iloc[0]["Title"]
    assert df_download_comp.iloc[1]["Title"] not in df_after_comp["Title"]
    assert "url" in df_after_comp
    assert len(df_after_comp) > len(df_init_comp)
    assert df_after_comp["description"].iloc[-1] == ""
    assert len(df_after_topics) > 0
