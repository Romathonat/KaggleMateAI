import re

from kmai.adapters.stubs.stub_csv_reader import StubCSVReader
from kmai.adapters.stubs.stub_csv_writer import StubCSVWriter
from kmai.adapters.stubs.stub_faiss import StubFAISSFromScratch
from kmai.use_cases.retrieve_competition import create_vector_store
from kmai.config import settings

def test_create_vector_store_from_scratch():
    desc = "I want to forecast the weather for the next week, based on the informations I have of the 365 last days (Temperature, Hygrometry, etc.)"

    vector_store = create_vector_store(StubCSVReader(), StubCSVWriter(), StubFAISSFromScratch())
    top_competitions = vector_store.get_similar_competitions(desc, 5)

    assert len(top_competitions) == 5
    assert "Title" in top_competitions
    assert "Description" in top_competitions
    assert "Url" in top_competitions

    assert all([url.startswith(settings.KAGGLE_URL) for url in top_competitions["Url"]])

# def test_create_vector_store_from_existing_data():
#     vector_store = create_vector_store(StubCSVReader(), StubCSVWriter(), StubFAISSExistingData())
#     top_competitions = vector_store.get_similar_competitions("description", 3)

#     assert len(top_competitions) == 5
#     assert "Title" in top_competitions
#     assert "Description" in top_competitions
#     assert "Url" in top_competitions

#     pattern = r"^https://www\.kaggle\.com/c/[\w-]+$"
#     assert all([url.startswith(settings.KAGGLE_URL) for url in top_competitions["Url"]])