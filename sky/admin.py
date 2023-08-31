from django.contrib import admin
from .models import News, Subscribers


admin.site.register(Subscribers)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "reporter", "category", "date_posted"]
    list_editable = ["category"]
    list_filter = ["category", "date_posted"]
    prepopulated_fields = {"slug": ("category", "title",)}
