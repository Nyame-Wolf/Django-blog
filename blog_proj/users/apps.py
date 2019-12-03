from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #to import our signals following recommendation by django docs
    def ready(self):
        import users.signals
