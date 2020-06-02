from django.contrib import admin
from .models import User, DailyTemperature

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name','last_name','created_by','updated_by')

admin.site.register(User, UserAdmin)

class DailyTemperatureAdmin(admin.ModelAdmin):
    list_display = ('user','temperature', 'created_by', 'updated_by')

admin.site.register(DailyTemperature, DailyTemperatureAdmin)