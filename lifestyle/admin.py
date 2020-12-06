from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lifestyle_News
# u/p   >>np/np             np2/np2


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ['headline', 'reporter', 'published_at']
    search_fields = ['headline']
    readonly_fields = ['published_at']
    list_filter = ['headline']


admin.site.register(Lifestyle_News, NewsAdmin)

