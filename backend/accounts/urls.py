from django.urls import path
from .views import UserCreateView, protected_view, unprotected_view, ProtectedView, ObtainToken, create_session_view, logout_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', UserCreateView.as_view(), name="create-user"),
    path('protected-view/', protected_view, name="protected-view"),
    path('unprotected-view/', unprotected_view, name="unprotected-view"),
    path('protected-cbv/', ProtectedView.as_view(), name="protected-cbv"),
    path('obtain-token/', ObtainToken.as_view(), name="obtain-token"),
    path('login/', create_session_view, name="login"),
    path('logout/', logout_view, name="logout"),

    # JWT Views
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]