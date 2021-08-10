# yatube/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
