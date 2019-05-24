from django.contrib import admin

# from . import forms
from . import models


class CaseAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.Case._meta.fields]


admin.site.register(models.Case, CaseAdmin)


class CourtAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.Court._meta.fields]


admin.site.register(models.Court, CourtAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.Client._meta.fields]


admin.site.register(models.Client, ClientAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.Country._meta.fields]


admin.site.register(models.Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.State._meta.fields]


admin.site.register(models.State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.City._meta.fields]


admin.site.register(models.City, CityAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.Profile._meta.fields]


admin.site.register(models.Profile, ProfileAdmin)
