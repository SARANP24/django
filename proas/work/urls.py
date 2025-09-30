from django.urls import path
from . import views

app_name = 'work'
urlpatterns = [
    path('home/', views.show2, name='home'),
    path('send_mail/',views.show_mail,name='Show_mail'),
    path('textai/',views.text_ai,name='text_ai')
    
]