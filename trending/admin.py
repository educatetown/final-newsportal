from django.contrib import admin
from .models import Trending_News
# u/p   >>np/np             np2/np2


class TrendingAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ['headline', 'reporter', 'published_at']
    search_fields = ['headline']
    readonly_fields = ['published_at']
    list_filter = ['headline']


admin.site.register(Trending_News, TrendingAdmin)

