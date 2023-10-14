from django.urls import path

from yousta.views import SignUpView,SignInView,CategoryCreateView,remove_category\
,ClothCreateView,ClothListView,ClothUpdateView,remove_clothview



urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cloths/add",ClothCreateView.as_view(),name="cloth-add"),
    path("cloths/all",ClothListView.as_view(),name="cloth-list"),
    path("cloths/<int:pk>/change",ClothUpdateView.as_view(),name="cloth-change"),
    path("cloths/<int:pk>/remove",remove_clothview,name="cloth-remove")





]