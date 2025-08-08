from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    room_type = models.CharField(max_length=50, choices=[
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('SUITE', 'Suite'),
        ('MEETING', 'Meeting Room'),
    ])
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    features = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.room_type})"


class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_name} - {self.room.name} ({self.start_date} to {self.end_date})"

    class Meta:
        ordering = ['-start_date']
        unique_together = ('room', 'start_date', 'end_date')



class RoomAvailability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('room', 'date')

    def __str__(self):
        return f"{self.room.name} - {self.date} - {'Available' if self.is_available else 'Booked'}"


