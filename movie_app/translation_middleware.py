from .translate_service import translate_text
from django.core.cache import cache

class TranslationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Pobierz język wybrany przez użytkownika
        selected_language = request.session.get('language', 'en')
        request.selected_language = selected_language

        # Obsłuż żądanie i odbierz odpowiedź
        response = self.get_response(request)

        # Sprawdź, czy odpowiedź jest typu HTML i czy wymaga tłumaczenia
        if hasattr(response, 'content') and response['Content-Type'] == 'text/html; charset=utf-8':
            # Jeśli język to angielski, nie wykonuj tłumaczenia
            if selected_language == 'en':
                return response

            # Utwórz klucz cache na podstawie ścieżki URL i wybranego języka
            cache_key = f"translated_content_{request.path}_{selected_language}"
            cached_content = cache.get(cache_key)

            # Jeśli jest już przetłumaczone w cache, zwróć przetłumaczoną zawartość
            if cached_content:
                response.content = cached_content
                return response

            # Dekoduj zawartość HTML
            content = response.content.decode('utf-8')
            print("Tłumaczenie na język:", selected_language)  # Debugging: Sprawdzenie, czy middleware się uruchamia
            print("Przed tłumaczeniem:", content[:500])  # Pierwsze 500 znaków przed tłumaczeniem

            # Tłumacz stronę na wybrany język
            translated_content = translate_text(selected_language, content)
            response.content = translated_content.encode('utf-8')

            # Zapisz przetłumaczoną zawartość w cache na 1 dzień (86400 sekund)
            cache.set(cache_key, response.content, timeout=86400)

            print("Po tłumaczeniu:", response.content[:500])  # Pierwsze 500 znaków po tłumaczeniu

        return response
