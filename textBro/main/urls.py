from django.urls import path

from . import views

app_name = 'textBro'


urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<str:link>/<str:password>/', views.editText, name="editText"),
    path('edit/<str:link>/', views.editTextAskPassword, name="editTextAskPassword"),
    path('save/<str:link>/<str:password>/', views.saveText, name="saveText"),
    path('verify', views.verify, name="verify"),
]