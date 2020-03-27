from common.views import index, RegisterView, CreateUserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.urls import path
from allauth.account.views import login, logout

app_name = 'common'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile_create/', CreateUserProfile.as_view(), name='profile_create'),
]


# path('login/', LoginView.as_view(), name='login'),
# path('logout/', LogoutView.as_view(), name='logout'),
