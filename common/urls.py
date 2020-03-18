from common.views import index, login, logout
from django.urls import path

app_name = 'common'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

