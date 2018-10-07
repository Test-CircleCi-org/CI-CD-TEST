from django.urls import path

from . import views
app_name = 'partners'

urlpatterns = [

     path('registerCampusPartner/', views.registerCampusPartner, name='registerCampusPartner'),
     path('registerCampusPartner/profile/', views.registerCampusPartnerProfile, name='registerCampusPartnerProfile'),
    ]
