from django.contrib import admin
from . import models


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'client', 'created')
    fields = ('user', 'client', 'created')
    ordering = ('-created',)
    readonly_fields = ('created',)


admin.site.register(models.Token, TokenAdmin)
