from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),

    path('post/<int:post_id>/', views.post_detail, name='post-detail'),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),

    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        http_method_names=['get', 'post'],
        template_name='users/logout.html'
    ), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )