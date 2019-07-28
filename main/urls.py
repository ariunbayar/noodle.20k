from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import entry.views
import image.views
import issues.views
import lesson.views
import secure.views


urlpatterns = [
    path('', issues.views.list, name='issues-list'),
    path('lesson/', lesson.views.list, name='lesson-list'),
    path('lesson-<int:pk>/<str:slug>/', lesson.views.detail, name='lesson-detail'),

    path('admin/entry/', entry.views.list, name='entry-list'),
    path('admin/entry/add/', entry.views.form, name='entry-add'),
    path('admin/entry/<int:pk>/', entry.views.detail, name='entry-detail'),
    path('admin/entry/<int:pk>/edit/', entry.views.form, name='entry-edit'),
    path('admin/entry/<int:pk>/delete/', entry.views.delete, name='entry-delete'),
    path('admin/entry/<int:pk>/publish/', entry.views.publish_toggle, name='entry-publish', kwargs={'is_published': True}),
    path('admin/entry/<int:pk>/unpublish/', entry.views.publish_toggle, name='entry-unpublish', kwargs={'is_published': False}),

    path('admin/image/', image.views.list, name='image-list'),
    path('admin/image/upload/', image.views.upload, name='image-upload'),
    path('admin/image/delete/<int:pk>/', image.views.delete, name='image-delete'),

    path('login/', secure.views.login, name='login'),
    path('logout/', secure.views.logout, name='logout'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
