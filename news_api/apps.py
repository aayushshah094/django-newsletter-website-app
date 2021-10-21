from django.apps import AppConfig


class NewsApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_api'

    def ready(self):
        import news_api.signals