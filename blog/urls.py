from django.urls import path
from blog import views

urlpatterns = [
    path('bloglist/', views.BlogListView.as_view(), name='bloglist'),
    path('blogcreate/', views.BlogView.as_view(), name='blogcreate'),
    path('updateprofile/<int:pk>/', views.UpdateProfileView.as_view(), name='updateprofile'),
    path('updateblog/<int:pk>/', views.UpdateBlogView.as_view(), name='updateblog'),
    path('likeblog/<int:pk>/', views.BlogLikeView.as_view(), name='updateblog'),

    
]
