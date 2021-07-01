from django.apps import AppConfig


class KorepetycjeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'korepetycje'
    def ready(self):
        import korepetycje.signals

