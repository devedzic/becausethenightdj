import sys
import django
django.setup()

from django.apps import apps

for _class in apps.get_models():
    globals()[_class.__name__] = _class

