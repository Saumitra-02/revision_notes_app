"""
URL configuration for notes_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('notes_demo.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
    # path('notes/', NoteViewSet.as_view({'get': 'list', 'post': 'create'}), name='notes-list'),
    # path('notes/', NoteViewSet.as_view({'get': 'new_note'}), name='new-note'),
    # path('notes/<pk>/', NoteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='notes-detail'),
]