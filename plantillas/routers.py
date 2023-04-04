class PlantillaRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Vpfacturacion':
            return 'plantilla_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Vpfacturacion':
            return 'plantilla_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == 'Vpfacturacion' or
            obj2._meta.app_label == 'Vpfacturacion'
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label == "Vpfacturacion":
            return db == 'plantilla_db'
        return None