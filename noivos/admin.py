from django.contrib import admin
from .models import Presentes, Convidados
#http://127.0.0.1:8000/admin
admin.site.register(Presentes)
admin.site.register(Convidados)

# Register your models here.
