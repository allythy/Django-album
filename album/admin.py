from django.contrib import admin
from . import models
# Register your models here.
from album.models import Foto


admin.site.register(Foto)
