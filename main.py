import kagglehub
import pandas as pd
from pathlib import Path

path: Path = Path(kagglehub.dataset_download("samlearner/letterboxd-movie-ratings-data"))

movie_data = pd.read_csv(path / "movie_data.csv", on_bad_lines='skip', engine='python')
ratings_data = pd.read_csv(path / "ratings_export.csv", on_bad_lines='skip', engine='python')
users_data = pd.read_csv(path / "users_export.csv", on_bad_lines='skip', engine='python')

print("Dataframes loaded!")
print(f"movie_data: {movie_data.shape}")
print(f"ratings_data: {ratings_data.shape}")
print(f"users_data: {users_data.shape}")