from django.contrib import admin
from models import SQLLog


class SQLLogAdmin(admin.ModelAdmin):
    list_display = ("url", "raw_sql", "execution_time", )

admin.site.register(SQLLog, SQLLogAdmin)
