from .translate_service import translate_text

class TranslationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Pobierz język wybrany przez użytkownika
        selected_language = request.session.get('language', 'en')
        request.selected_language = selected_language

        # Obsłuż żądanie i odbierz odpowiedź
        response = self.get_response(request)

        # Sprawdź, czy odpowiedź jest typu HTML
        if hasattr(response, 'content') and response['Content-Type'] == 'text/html; charset=utf-8':
            content = response.content.decode('utf-8')
            print("Tłumaczenie na język:", selected_language)  # Debugging: Sprawdzenie, czy middleware się uruchamia
            print("Przed tłumaczeniem:", content[:500])  # Pierwsze 500 znaków przed tłumaczeniem

            # Tłumacz stronę na wybrany język, nawet jeśli to angielski
            translated_content = translate_text(selected_language, content)
            response.content = translated_content.encode('utf-8')

            print("Po tłumaczeniu:", response.content[:500])  # Pierwsze 500 znaków po tłumaczeniu

        return response
