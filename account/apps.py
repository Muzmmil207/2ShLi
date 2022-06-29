from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

# class SuitConfig(DjangoSuitConfig):
#     layout = 'horizontal'

