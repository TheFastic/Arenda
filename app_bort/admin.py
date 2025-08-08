from django.contrib import admin
from app_bort.models import Room, Booking, RoomAvailability

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'room', 'start_date', 'end_date', 'is_confirmed', 'is_cancelled')
    list_filter = ('is_confirmed', 'is_cancelled', 'room')
    search_fields = ('user_name', 'email')

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(RoomAvailability)
