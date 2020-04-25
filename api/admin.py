from django.contrib import admin
from .models import Profile, Training, Exercise, Set

admin.site.register(Profile)
admin.site.register(Training)
admin.site.register(Exercise)
admin.site.register(Set)