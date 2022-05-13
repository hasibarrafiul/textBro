from django.urls import path

from . import views

app_name = 'textBro'


urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<str:link>', views.editText, name="editText"),
    path('save/<str:link>', views.saveText, name="saveText"),
]