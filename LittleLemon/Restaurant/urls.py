from django.urls import path
from .views import MenuItemView,SingleMenuItemView,msg
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', MenuItemView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token),
    
]
