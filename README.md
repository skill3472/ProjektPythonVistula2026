# Projekt

Numer grupy: 3
Nazwa projektu: Analiza danych Letterboxd: Trendy na platformie oceniania filmów
Opis: Analiza danych z platformy Letterboxd w celu identyfikacji trendów dotyczących rozkładu ocen filmów, preferencji producentów, popularności gatunków oraz aktywności użytkowników.

# Grupa

| Lab | ID | Nazwisko | Imię |
|-----|----|----------|------|
| 1 | 73059 | Tym | Maksymilian |
| 1 | 72173 | Fąfara | Julia |
| 1 | 71883 | Kluska | Dawid |
| 1 | 71634 | Surganow | Aleksander |


# Wkład

| ID | Nazwisko | Imię | Opis wkładu |
|----|----------|------|-------------|
| 73059 | Tym | Maksymilian | Przygotowanie danych. |
| 72173 | Fąfara | Julia | Eksploracyjna analiza. |
| 71883 | Kluska | Dawid | Interpretacja wniosków i przygotowanie raportu. |
| 71634 | Surganow | Aleksander | Interpretacja wniosków i przygotowanie raportu. |

# Pytania badawcze

1. Jak wygląda rozkład ocen filmów i ich popularność na Letterboxd?
2. Jakie kraje dominują w produkcji filmów dostępnych w bazie?
3. Które gatunki filmowe są najpopularniejsze na platformie?
4. Jak aktywni są użytkownicy platformy pod względem pisania recenzji?

# Źródła danych

## Kaggle

Letterboxd Movie Ratings Data
(https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data)

# Zmienne

**movie_data:** `_id`, `genres`, `image_url`, `imdb_id`, `imdb_link`, `movie_id`, `movie_title`, `original_language`, `overview`, `popularity`, `production_countries`, `release_date`, `runtime`, `spoken_languages`, `tmdb_id`, `tmdb_link`, `vote_average`, `vote_count`, `year_released`

**ratings_data:** `_id`, `movie_id`, `rating_val`, `user_id`

**users_data:** `_id`, `display_name`, `num_ratings_pages`, `num_reviews`, `username`

# Cechy

`czyste_kraje`, `czyste_gatunki`

# Analiza

1. Rozkład średnich ocen filmów (z wykluczeniem filmów bez oceny)
2. Top 15 krajów z największą liczbą filmów w bazie
3. Liczba filmów w zależności od roku wydania
4. Najczęstsze gatunki filmowe w bazie
5. Aktywność użytkowników - rozkład liczby napisanych recenzji
6. Top 10 najwyżej ocenianych filmów oraz filmów z największą liczbą głosów

# Środowisko

Python version: Python 3.13
Main libraries: `kagglehub>=1.0.0`, `matplotlib>=3.10.8`, `pandas>=3.0.2`

## Instalacja

Zależności i środowisko wirtualne można zainicjować przy użyciu uv lub pip.

### uv

```bash
uv sync
```

### pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install .
```

# Zawartość

```
P2_3_Etap2/
|
|--- src/
|------ analiza.ipynb
|--- Raport.pdf
|--- pyproject.toml
|--- .gitignore
|--- .python-version
|--- README.md
|--- uv.lock
```
