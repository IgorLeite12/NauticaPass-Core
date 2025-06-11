from django.contrib import admin
from vessel.models import Vessel

@admin.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_vessel', 'name_owner', 'capacity', 'navigation_type')
    search_fields = ('name_owner',)