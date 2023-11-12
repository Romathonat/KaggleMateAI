import re

from kmai.adapters.stubs.stub_csv_handler import StubCSVHandler2
from kmai.adapters.stubs.stub_faiss import StubFAISSFromScratch
from kmai.domain.retrieve_competition import create_vector_store
from kmai.config import settings

def test_create_vector_store():
    desc = "I want to forecast the weather for the next week, based on the informations I have of the 365 last days (Temperature, Hygrometry, etc.)"

    vector_store = create_vector_store(StubCSVHandler2(), StubFAISSFromScratch())
    top_competitions = vector_store.get_similar_competitions(desc, 5)

    assert len(top_competitions) == 5
    assert "Title" in top_competitions
    assert "Description" in top_competitions
    assert "Url" in top_competitions

    assert all([url.startswith(settings.KAGGLE_URL) for url in top_competitions["Url"]])
