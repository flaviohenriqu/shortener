from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserRegistrationAPIView


app_name = 'users'

urlpatterns = [
    path('', UserRegistrationAPIView.as_view(), name="create"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
