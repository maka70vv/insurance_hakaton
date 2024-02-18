from django.contrib import admin

from hr.models import Workers, Jobs


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'inn', 'salary')
    search_fields = ('full_name', 'inn', 'job', 'user')
    list_filter = ('salary', 'job', 'employmentDate', 'active')


admin.site.register(Jobs)
