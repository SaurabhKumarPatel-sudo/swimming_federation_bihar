from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('home/', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('records/', views.records, name='records'),
    path('rules/', views.rules, name='rules'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),

    # New URLs for registration and authentication
    path('register/', views.registration_choice, name='registration_choice'),
    path('register/athlete/', views.athlete_registration, name='athlete_registration'),
    path('register/coach/', views.coach_registration, name='coach_registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('discipline/swimming/', views.discipline_swimming, name='discipline_swimming'),
    path('discipline/masters-swimming/', views.discipline_masters_swimming, name='discipline_masters_swimming'),
    path('discipline/synchronized-swimming/', views.discipline_synchronized_swimming, name='discipline_synchronized_swimming'),
    path('discipline/diving/', views.discipline_diving, name='discipline_diving'),
    path('discipline/high-diving/', views.discipline_high_diving, name='discipline_high_diving'),
    path('discipline/water-polo/', views.discipline_water_polo, name='discipline_water_polo'),
]
