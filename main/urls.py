"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import issues.views
import lesson.views
import entry.views


urlpatterns = [
    path('', issues.views.list, name='issues-list'),
    path('lesson/', lesson.views.list, name='lesson-list'),
    path('lesson/<int:pk>/<str:slug>/', lesson.views.detail, name='lesson-detail'),

    path('entry/', entry.views.list, name='entry-list'),
    path('entry/add/', entry.views.form, name='entry-add'),
    path('entry/<int:pk>/', entry.views.detail, name='entry-detail'),
    path('entry/<int:pk>/edit/', entry.views.form, name='entry-edit'),
    path('entry/<int:pk>/delete/', entry.views.delete, name='entry-delete'),
    path('entry/<int:pk>/publish/', entry.views.publish_toggle, name='entry-publish', kwargs={'is_published': True}),
    path('entry/<int:pk>/unpublish/', entry.views.publish_toggle, name='entry-unpublish', kwargs={'is_published': False}),
]
