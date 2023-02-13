from django.urls import path

from user.api.views import (RegistrationView,
                            LoginView,
                            UpdateTokenView,
                            LogoutView,
                            RestorePasswordView,
                            RestorePasswordCompleteView,
                            ChangePasswordView, ActivationView)

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='api_register'),
    path('activation/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', UpdateTokenView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('restore_password/', RestorePasswordView.as_view()),
    path('restore_complete/', RestorePasswordCompleteView.as_view()),
    path('change_password/', ChangePasswordView.as_view())
]
