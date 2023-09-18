from django.contrib import admin
from .models import Profile, Medical, Treatment, Doctor

# Create a list of models to register
models_list = [Profile, Medical, Treatment, Doctor]

# Register each model in the list
for model in models_list:
    admin.site.register(model)