from django.apps import AppConfig


class APIConfig(AppConfig):
    # default_auto_field = "django.db.models.BigAutoField"
    name = "collections_app_api"

    def ready(self):
        # to prevent duplicate signal registration
        import collections_app_api.signals