from django.contrib import admin
from .models import Appointment, Article, Doctor, Category, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality')

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Appointment)


