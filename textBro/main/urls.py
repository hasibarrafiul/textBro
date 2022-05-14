from django.urls import path

from . import views

app_name = 'textBro'


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:link>/<str:password>/', views.editText, name="editText"),
    path('<str:link>/', views.editTextAskPassword, name="editTextAskPassword"),
    path('save/<str:link>/<str:password>/', views.saveText, name="saveText"),
    path('saveTab/<str:link>/<str:password>/<str:tab>', views.saveTextNewTab, name="saveTextTab"),
    path('newtab/<str:link>/<str:password>/', views.newTab, name="newTab"),
    path('verify', views.verify, name="verify"),
    path('openTab/<str:link>/<str:password>/<str:tab>', views.openTab, name="openTab"),
    path('saveTabInside/<str:link>/<str:password>/<str:tab>', views.saveTextTabInside, name="saveTabInside"),
]