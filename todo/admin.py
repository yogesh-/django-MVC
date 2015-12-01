from django.contrib import admin
from .models import List, Item

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    pass
class ItemAdmin(admin.ModelAdmin):
	pass

admin.register(List,Item)(admin.ModelAdmin)