from django.urls import path
from .views import signUp,log


urlpatterns = [

path('signup/',signUp,name='Signup'),
path('log/',log,name='loginpage')

]