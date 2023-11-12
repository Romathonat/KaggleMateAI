

from kmai.domain.retrieve_competition import create_vector_store
from kmai.adapters.faiss_helper import FAISSHelper
from kmai.adapters.csv_handler import CSVHandler 

if __name__ == "__main__":
    desc = "Our problem is to forecast the weather for tomorrow"
    # desc = "Our problem is to recommend the best food shop in the area of the user based on her preferences"
    vector_store = create_vector_store(CSVHandler(), FAISSHelper())
    top_competitions = vector_store.get_similar_competitions(desc, 5)
    vector_store.save_vector_store()

    for url in top_competitions["Url"]: 
        print(url)