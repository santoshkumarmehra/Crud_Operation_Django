from .models import student2

class student2DBRouter:

    # route_app_labels = {'crudoperation'}

    def db_for_read (self, model, **hints):
        if (model == student2):
    # your model name as in settings.py/DATABASES
            return 'student2'
        return None

    def db_for_write (self, model, **hints):
        if (model == student2):
        # your model name as in settings.py/DATABASES
            return 'student2'
            
        return None