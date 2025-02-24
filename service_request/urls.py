from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.uservice, name='sr'),
    path('tr', views.tr, name='tr'),
    path('cs', views.cs, name='cs'),
    path('dt/<int:id>/', views.detail, name='dt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
