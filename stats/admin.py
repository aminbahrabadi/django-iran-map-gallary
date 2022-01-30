from django.contrib import admin

from .models import State, Image


class InlineImages(admin.TabularInline):
    model = Image


class StateAdmin(admin.ModelAdmin):
    inlines = [InlineImages, ]


admin.site.register(State, StateAdmin)
