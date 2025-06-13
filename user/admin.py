from passage.models import Passage
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')


@admin.register(Passage)
class PassageAdmin(admin.ModelAdmin):
    list_display = (
    'id_vessel', 'origin', 'destination', 'value', 'capacity', 'travel_date', 'departure_time', 'arrival_date',
    'arrival_time')

    # Filtros
    search_fields = ['origin__name', 'destination__name', 'id_vessel__name_vessel']
    list_filter = ['travel_date', 'id_vessel']