from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # let us to use signals

    # let say someone created a user but didnt created a profile
    # so this finc will be called evertime  a user created so profile willbe created associated with the user

    def ready(self):
        import users.signals