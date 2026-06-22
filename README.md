# Projekt

**Numer grupy:** 3

**Nazwa projektu:** Spersonalizowany system rekomendacji filmowych na podstawie danych użytkowników platformy Letterboxd

**Opis:** Głównym celem projektu było przeprowadzenie procesu fine-tuningu dużego modelu językowego w taki sposób, aby potrafił on trafnie przewidzieć ocenę punktową, jaką konkretny użytkownik przyznałby danemu filmowi, bazując wyłącznie na jego krótkim opisie fabularnym. 

Etapy projektu: 
* Analiza danych z platformy Letterboxd w celu identyfikacji trendów dotyczących rozkładu ocen filmów, dominujących krajów produkcji, popularności gatunków oraz aktywności użytkowników. 
* Wybór modelu HuggingFace Transformers.
* Fine-tuning modelu LLM i interpretacja wyników.

# Grupa

| Lab | ID | Nazwisko | Imię |
|-----|----|----------|------|
| 1 | 73059 | Tym | Maksymilian |
| 1 | 72173 | Fąfara | Julia |
| 1 | 71883 | Kluska | Dawid |
| 1 | 71634 | Surganow | Aleksander |


# Źródła danych

## Kaggle

Letterboxd Movie Ratings Data
(https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data)

# Zmienne

**movie_data:** `_id`, `genres`, `image_url`, `imdb_id`, `imdb_link`, `movie_id`, `movie_title`, `original_language`, `overview`, `popularity`, `production_countries`, `release_date`, `runtime`, `spoken_languages`, `tmdb_id`, `tmdb_link`, `vote_average`, `vote_count`, `year_released`

**ratings_data:** `_id`, `movie_id`, `rating_val`, `user_id`

**users_data:** `_id`, `display_name`, `num_ratings_pages`, `num_reviews`, `username`


## Uruchomienie projektu i odtworzenie wyników

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

### Pobranie danych
W projekcie wykorzystany został duży zbiór danych, który nie jest załączony do repozytorium ze względu na rozmiar. Po uruchomieniu komórek w notatniku biblioteka kagglehub automatycznie pobierze zbiór bezpośrednio z platformy Kaggle i załaduje pliki CSV do środowiska.

### Odtworzenie wyników
Aby odtworzyć wyniki, należy otworzyć notatniki znajdujące się w folderze src i uruchomić wszystkie znajdujące się w nich komórki. Plik `analiza.ipynb` zawiera Eksploracyjną Analizę Danych (drugi etap projektu), a plik `finetuning.ipynb` zawiera trening modelu LLM (czwarty etap projektu).

**Ważne uwagi dotyczące odtwarzalności:**
* W kodzie zastosowano stałe ziarno losowości podczas podziału na zbiór testowy i treningowy, co gwarantuje identyczny rozkład danych przy każdym uruchomieniu.
* Do szybkiego treningu zalecane jest użycie karty graficznej. Trening na samym procesorze jest możliwy, ale znacznie wydłuży czas wykonania. Sposób instalacji biblioteki torch różni się w zależności od posiadanego sprzętu. Aby model wykorzystywał akcelerację sprzętową, należy zainstalować bibliotekę dopasowaną do własnej karty graficznej.

# Zawartość

```
P5_3_LetterBoxd_72173/
|
|--- src/
|------ analiza.ipynb
|------ finetuning.ipynb
|--- Raport.pdf
|--- pyproject.toml
|--- .gitignore
|--- .python-version
|--- README.md
|--- uv.lock
```

# Wykorzystanie narzędzi AI
Podczas realizacji projektu wykorzystano modele językowe (Claude, Gemini) w charakterze wsparcia technicznego:
* Pomoc przy debugowaniu kodu
* Pomoc przy rozwiązywaniu problemów środowiskowych
* Korekta dokumentacji