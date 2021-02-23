from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountsView
from rest_framework_simplejwt import views as jwt_views


route = DefaultRouter()
route.register(r'account', AccountsView)

urlpatterns = [
    path('', include(route.urls)),
    path('api/login', jwt_views.TokenObtainPairView.as_view(), name='login')
]