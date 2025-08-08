from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from app_bort.models import Room, Booking
from app_bort.forms import BookingForm, RoomForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    bookings = Booking.objects.filter(room=room, end_date__gte=date.today())
    return render(request, 'room_detail.html', {
        'room': room,
        'bookings': bookings
    })


def create_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room

            # Перевірка конфлікту дат
            conflict = Booking.objects.filter(
                room=room,
                start_date__lt=booking.end_date,
                end_date__gt=booking.start_date,
                is_cancelled=False
            ).exists()

            if conflict:
                messages.error(request, "На цю дата вже заброньована номер.")
            else:
                booking.save()

                send_mail(
                    subject='Підтвердження бронювання',
                    message=f"Ваше бронювання кімнати '{room.name}' з {booking.start_date} по {booking.end_date} зареєстровано.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[booking.email],
                    fail_silently=True
                )

                messages.success(request, "Бронювання успішно створено!")
                return redirect('room_list')
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {
        'form': form,
        'room': room
    })


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.is_cancelled = True
    booking.save()
    messages.success(request, "Бронювання скасовано.")
    return redirect('room_list')


def create_booking_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    
    return render(request, 'create_booking_room.html', {'form': form})


def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')  
    return render(request, 'delete_room.html', {'room': room})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('my_bookings')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('my_bookings')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('room_list')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user_name=request.user)  
    return render(request, 'my_bookings.html', {'bookings': bookings})