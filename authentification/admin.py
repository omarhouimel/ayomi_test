from django.contrib import admin

# Register your models here.
from authentification.models import User

admin.site.register(User)