from django.contrib import admin
from .models import News
# u/p   >>np/np             np2/np2


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ['headline', 'reporter', 'featured', 'published_at']
    list_editable = ['featured']
    search_fields = ['headline']
    readonly_fields = ['published_at', 'updated_at']
    list_filter = ['headline']


admin.site.register(News, NewsAdmin)

