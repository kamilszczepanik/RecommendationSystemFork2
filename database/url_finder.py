import pandas as pd
import requests

def fetch_movie_poster_url(title, api_key):
    """Zwraca URL plakatu filmu dla danego tytułu."""
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {'api_key': api_key, 'query': title}
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

def add_poster_urls_to_csv(input_csv, output_csv, api_key):
    """Dodaje URL-e plakatów do DataFrame na podstawie tytułów filmów."""
    df = pd.read_csv(input_csv)
    df['poster_url'] = df['title'].apply(lambda x: fetch_movie_poster_url(x, api_key))
    df.to_csv(output_csv, index=False)

api_key = '34a56f9fc92ef214f16d1e7111b2147f'
input_csv = 'movies_from_database.csv'  
output_csv = 'movies_with_url.csv' 

add_poster_urls_to_csv(input_csv, output_csv, api_key)
