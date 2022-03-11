from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from account import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='tokenobtain'),
    path('Refreshtoken/', TokenRefreshView.as_view(), name='tokenrefresh'),
    path('userregister/', views.UserRegister.as_view(), name='RegisterUser'),
    path('userlist/', views.UserList.as_view(), name='userlist'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('updateprofile/<int:pk>', views.UpdateProfile.as_view(), name='userupdate'),
]
