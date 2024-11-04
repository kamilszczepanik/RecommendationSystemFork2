import requests

# Twój klucz API
API_KEY = 'AIzaSyCXAjqoTv7w2jCJO2Gb7AwAjmYRviAl3bU'

# Funkcja tłumacząca tekst

def translate_text(target_language, text):
    url = f'https://translation.googleapis.com/language/translate/v2?key={API_KEY}'

    # Dziel tekst na fragmenty po maksymalnie 5000 znaków
    chunks = [text[i:i+5000] for i in range(0, len(text), 5000)]
    translated_chunks = []

    for chunk in chunks:
        params = {
            'q': chunk,
            'target': target_language,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            result = response.json()
            translated_text = result['data']['translations'][0]['translatedText']
            translated_chunks.append(translated_text)
        else:
            print("Błąd tłumaczenia:", response.json())  # Debug: Wyświetl błąd z API
            return text  # Jeśli wystąpił błąd, zwróć oryginalny tekst

    return ''.join(translated_chunks)

