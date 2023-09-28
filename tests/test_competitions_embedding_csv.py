from unittest.mock import patch

from kmai.adapters.stubs.stub_competition_scrapper import StubCompetitionScrapper
from kmai.adapters.stubs.stub_csv_reader import StubCSVReader
from kmai.adapters.stubs.stub_csv_writer import StubCSVWriter
from kmai.adapters.stubs.stub_kaggle_dowloader import StubKaggleDownloader
from kmai.adapters.stubs.stub_llm_caller import StubLLMCaller
from kmai.config import settings
from kmai.use_cases.data_preprocessing import (
    create_competitions_embedding_csv,
    update_competion_csv,
    update_competitions_embedding,
)


@patch("kmai.config.settings.INITIAL_COMPETITION_NUMBER_TO_EMBED", new=2)
def test_create_competitions_embedding_csv():
    df = create_competitions_embedding_csv(
        StubKaggleDownloader(), StubCompetitionScrapper(), StubLLMCaller(), StubCSVWriter()
    )

    df_embeddings = df[~df["desc_embedding"].isna()]

    assert "desc_embedding" in df
    assert len(df_embeddings) == settings.INITIAL_COMPETITION_NUMBER_TO_EMBED
    assert len(df) >= settings.INITIAL_COMPETITION_NUMBER_TO_EMBED
    assert all(isinstance(item, list) for item in df.iloc[:1]["desc_embedding"])


def test_update_competitions_embedding_csv():
    df = update_competitions_embedding(StubCompetitionScrapper(), StubLLMCaller(), StubCSVReader(), StubCSVWriter())

    assert "desc_embedding" in df
    assert all(isinstance(item, str) for item in df["description"])
    assert all(isinstance(item, list) for item in df["desc_embedding"])
    assert all(isinstance(item, str) for item in df["url"])
    assert df.iloc[-1]["url"] == "https://www.kaggle.com/c/slug3"


def test_update_competitions_csv():
    df_init_comp = StubCSVReader().read_csv("Competition.csv")
    df_init_topics = StubCSVReader().read_csv("Topics.csv")
    df_after_comp, df_after_topics = update_competion_csv(StubKaggleDownloader(), StubCSVReader(), StubCSVWriter())

    assert len(df_after_comp) > len(df_init_comp)
    assert isinstance(df_after_comp["desc_embedding"].iloc[0], list)
    assert df_after_comp["desc_embedding"].iloc[-1] is None

    assert len(df_after_topics) > 0
