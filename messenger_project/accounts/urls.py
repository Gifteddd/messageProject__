from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeView

from .views import *

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('update/password/', PasswordChangeView.as_view(
        template_name='registration/changePassword.html',
        success_url='/'
    ), name='changePassword'),
]