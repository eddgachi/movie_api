from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', views.MoviesList.as_view()),
    path('<int:pk>/', views.MovieDetail.as_view()),
    path('actors/', views.ActorList.as_view()),
    path('actors/<int:pk>/', views.ActorDetail.as_view()),
    path('directors/', views.DirectorList.as_view()),
    path('directors/<int:pk>/', views.DirectorDetail.as_view())
]
