
from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    #path('api/', include(router.urls)),
    path('',views.input_sentiment, name = 'cxform' ),

]
