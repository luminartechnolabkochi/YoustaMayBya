from django.urls import path

from yousta.views import SignUpView,SignInView,CategoryCreateView,remove_category,ClothCreateView



urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cloths/add",ClothCreateView.as_view(),name="cloth-add")




]