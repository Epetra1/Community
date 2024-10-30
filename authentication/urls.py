from django.urls import path, include

urlpatterns = [

    path('api/', include('authentication.api.urls')),


    path('', include('authentication.views.urls')),
]