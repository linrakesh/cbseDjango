from django.contrib import admin
from .models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'fname','email','image')
    search_fields = ['name','fname']

admin.site.register(student,studentAdmin)