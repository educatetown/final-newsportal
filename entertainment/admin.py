from django.contrib import admin
from .models import Entertainment_News


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ['headline', 'reporter', 'published_at']
    search_fields = ['headline']
    readonly_fields = ['published_at']
    list_filter = ['headline']


admin.site.register(Entertainment_News, NewsAdmin)

