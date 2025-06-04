from django.contrib import admin
from .models import Passage


@admin.register(Passage)
class PassageAdmin(admin.ModelAdmin):
    list_display = (
    'id_vessel', 'origin', 'destination', 'value', 'capacity', 'travel_date', 'departure_time', 'arrival_date',
    'arrival_time')

    # Filtros
    search_fields = ['origin__name', 'destination__name', 'id_vessel__name_vessel']
    list_filter = ['travel_date', 'id_vessel']