from django.urls import path
from .views import FaceVerificationAPI
 
urlpatterns = [
    path("faceapi/", FaceVerificationAPI.as_view()),
]
