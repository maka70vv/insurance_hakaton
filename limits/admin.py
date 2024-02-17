from django.contrib import admin
from limits.models import Limit


class LimitsModelAdmin(admin.ModelAdmin):
    search_fields = ['limitName']


admin.site.register(Limit, LimitsModelAdmin)
