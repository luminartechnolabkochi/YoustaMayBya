from django.urls import path

from yousta.views import SignUpView,SignInView,CategoryCreateView



urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("",SignInView.as_view(),name="signin"),




]