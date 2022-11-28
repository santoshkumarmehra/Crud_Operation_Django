from .models import student1

class student1DBRouter:

    # route_app_labels = {'crudoperation'}

    def db_for_read (self, model, **hints):
        if (model == student1):
    # your model name as in settings.py/DATABASES
            return 'student1'
        return None

    def db_for_write (self, model, **hints):
        if (model == student1):
        # your model name as in settings.py/DATABASES
            return 'student1'
        return None