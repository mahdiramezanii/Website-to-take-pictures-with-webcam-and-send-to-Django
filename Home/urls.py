from django.urls import path
from .views import upload_image

app_name="Home"
urlpatterns=[

    path("",upload_image,name="home")
]