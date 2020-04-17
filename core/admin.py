from django.contrib import admin

from core.models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    fields = ('full_url', )
    list_display = ('short_url', 'access_counter', 'full_url')

    def has_add_permission(self, request, obj=None):
        return False