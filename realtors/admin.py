from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('hire_date',)
    search_fields = ('name', 'email')
    list_per_page = 2

admin.site.register(Realtor, RealtorAdmin)