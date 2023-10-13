from django.urls import path

from yousta.views import SignUpView



urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    



]