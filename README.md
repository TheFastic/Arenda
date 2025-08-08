# Kordenal

## Owerviews

This project is a web application on **Django** for managing room reservations.
Allows users to register, log in, view available rooms, book them, and the administrator to add and delete rooms.



## Main features

- User registration and authorization
- View the list of available rooms
- View room details
- Book rooms for selected dates
- View your reservations
- Add and delete rooms (admin)

## Usage
- Register or log in
- View available rooms
- Select a room and book it
- View your reservations in your personal account
- Administrator can add and remove rooms via /admin

## Technologies
 - Python 

 - Django 

 - SQLite (default)

 - HTML5, CSS3 (Bootstrap for styling)

## Installation

## 1. Cloning the repository
```bash
git clone https://github.com/username/booking-project.git
cd booking-project
```
## 2. Creating a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
source venv/bin/activate 
```
## 3. Installing dependencies
```bash
pip install -r requirements.txt
```
## 4. Database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
## 5. Creating a superuser
```bash
python manage.py createsuperuser
Enter your username, email, and password.
```
## 6. Starting the server
```bash
python manage.py runserver
```