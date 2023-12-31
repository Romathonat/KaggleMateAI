from kmai.adapters.stubs.stub_competition_scrapper import (
    StubCompetitionScrapper,
    StubCompetitionScrapperErrorSelenium,
)
from kmai.adapters.stubs.stub_csv_handler import StubCSVHandler
from kmai.adapters.stubs.stub_kaggle_dowloader import StubKaggleDownloader
from kmai.config import settings
from kmai.domain.data_preprocessing import (
    update_competitions_csv,
    update_competitions_descriptions,
)


def test_update_competitions_descriptions():
    df = update_competitions_descriptions(StubCompetitionScrapper(), StubCSVHandler())

    assert all(isinstance(item, str) for item in df["description"])
    assert all(isinstance(item, str) for item in df["url"])
    assert "date_to_datastore" in df
    assert df.iloc[-1]["url"].startswith(settings.KAGGLE_URL)


def test_update_competitions_descriptions_bad_URL():
    df = update_competitions_descriptions(
        StubCompetitionScrapperErrorSelenium(), StubCSVHandler()
    )
    assert any(isinstance(item, str) for item in df["description"])
    assert all(isinstance(item, str) for item in df["url"])
    assert "date_to_datastore" in df
    assert df.iloc[-1]["url"].startswith(settings.KAGGLE_URL)


def test_update_competitions_csv():
    df_init_comp = StubCSVHandler().read_csv("Competition.csv")
    df_download_comp, _ = StubKaggleDownloader().download_data()
    df_after_comp, df_after_topics = update_competitions_csv(
        StubKaggleDownloader(), StubCSVHandler()
    )

    assert df_after_comp.iloc[0]["Title"] == df_init_comp.iloc[0]["Title"]
    assert df_download_comp.iloc[1]["Title"] not in df_after_comp["Title"]
    assert "url" in df_after_comp
    assert len(df_after_comp) > len(df_init_comp)
    assert df_after_comp["description"].iloc[-1] == ""
    assert len(df_after_topics) > 0
    assert "date_to_datastore" in df_after_comp
