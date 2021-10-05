from django.apps import AppConfig


class InvConfig(AppConfig):
    name = 'inv'

    def ready(self):
        import inv.signals