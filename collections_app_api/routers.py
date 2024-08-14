class CollectionsDatabaseRouter:
    """
    A router to control all database operations on models in the
    application that should go to the second database.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'collections_app_api':
            return 'collections'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'collections_app_api':
            return 'collections'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'collections_app_api' or \
           obj2._meta.app_label == 'collections_app_api':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'collections_app_api':
            return db == 'collections'
        return db == 'default'
