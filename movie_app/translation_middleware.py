from .translate_service import translate_text

class TranslationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Sprawdź wybrany język w sesji lub ustaw domyślny na angielski
        selected_language = request.session.get('language', 'en')
        request.selected_language = selected_language

        # Obsłuż żądanie
        response = self.get_response(request)

        # Tłumaczenie odpowiedzi HTML
        if hasattr(response, 'content') and response['Content-Type'] == 'text/html; charset=utf-8':
            content = response.content.decode('utf-8')
            translated_content = translate_text(selected_language, content)
            response.content = translated_content.encode('utf-8')

        return response
