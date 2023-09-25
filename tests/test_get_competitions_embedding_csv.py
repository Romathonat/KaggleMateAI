def test_get_competitions_embedding_csv_simple():
    # we want to download the csv from kaggle, scrap each competition description, transform them as correct text, embed them to finally store them in the csv
    df = get_competitions_embedding_csv(StubKaggleDownloader(), StubCompetitionScrapper(), StubLLM(), StubCSVWriter())

    assert "embedding" in df
    assert len(df) > 0
    assert all(isinstance(item, list) for item in df["embedding"])
