from django.urls import path

from . import views

app_name = 'textBro'


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:link>/<str:password>/', views.editText, name="editText"),
    path('<str:link>/', views.editTextAskPassword, name="editTextAskPassword"),
    path('save/<str:link>/<str:password>/', views.saveText, name="saveText"),
    path('verify', views.verify, name="verify"),
]