from django.urls import path

from yousta.views import SignUpView,SignInView



urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin")




]