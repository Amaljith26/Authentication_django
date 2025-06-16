from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from .views import landing_page, upload_image, view_images, protected_media

urlpatterns = [
    path('', landing_page, name='landing'),
    path('upload/', upload_image, name='upload-image'),
    path('view/', view_images, name='view-images'),
    path('login/', auth_views.LoginView.as_view(template_name='gallery/login.html'), name='login'),
    path('Logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^protected-media/(?P<path>.*)$', protected_media, name='protected-media'),
    
]
