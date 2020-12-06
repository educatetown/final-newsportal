from django.contrib import admin
from .models import Itself_News


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ['headline', 'reporter', 'featured', 'published_at']
    list_editable = ['featured', ]
    search_fields = ['headline']
    readonly_fields = ['published_at']
    list_filter = ['headline']


admin.site.register(Itself_News, NewsAdmin)

