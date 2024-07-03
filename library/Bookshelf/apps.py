from django.apps import AppConfig

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bookshelf'

    def ready(self):
        import Bookshelf.signals
        import Bookshelf.listeners
