from django.contrib import admin
from models import SQLLog, ModelLog


class SQLLogAdmin(admin.ModelAdmin):
    list_display = ("url", "raw_sql", "execution_time", )

admin.site.register(SQLLog, SQLLogAdmin)


class ModelsLogAdmin(admin.ModelAdmin):
    list_display = ("model", "model_pk", "operation_type", "date", )

admin.site.register(ModelLog, ModelsLogAdmin)
