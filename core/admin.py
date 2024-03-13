from django.contrib import admin

from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'avatar',)  # указываем названия полей как в модели
    list_editable = ('avatar', 'first_name')

# Register your models here.
