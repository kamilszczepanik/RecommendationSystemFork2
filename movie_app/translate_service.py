import requests

# Twój klucz API
API_KEY = 'AIzaSyBJeOxJ2Up3PKpsmByNS-jDaIjVURqaoJc'

# Funkcja tłumacząca tekst
def translate_text(target_language, text):
    url = f'https://translation.googleapis.com/language/translate/v2?key={API_KEY}'
    data = {
        'q': text,
        'target': target_language,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        result = response.json()
        return result['data']['translations'][0]['translatedText']
    else:
        return text  # W razie błędu zwracamy oryginalny tekst


