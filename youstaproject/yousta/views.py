from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from yousta.forms import RegistrationForm,LoginForm,CategoryCreateForm,ClothAddForm,ClothVarientForm,OfferForm
from yousta.models import User,Category,Cloths,ClothVarients,Offers



class SignUpView(CreateView):

    template_name="yousta/register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)

    
class SignInView(FormView):
    template_name="yousta/login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("signin")
            else:
                messages.error(request,"invalid creadential")
                return render(request,self.template_name,{"form":form})


class CategoryCreateView(CreateView,ListView):

    template_name="yousta/category_add.html"
    form_class=CategoryCreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("add-category")
    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)
    def get_queryset(self):
        return Category.objects.filter(is_active=True)


def remove_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=False)
    messages.success(request,"category removed")
    return redirect("add-category")



class ClothCreateView(CreateView):

    template_name="yousta/cloth_add.html"
    model=Cloths
    form_class=ClothAddForm
    success_url=reverse_lazy("cloth-add")

    def form_valid(self,form):
        messages.success(self.request,"cloth hasbeen added")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"cloth adding failed ")
        return super().form_invalid(form)
    

class ClothListView(ListView):
    template_name="yousta/cloth_list.html"
    model=Cloths
    context_object_name="cloths"


class ClothUpdateView(UpdateView):
    template_name="yousta/cloth_edit.html"
    model=Cloths
    form_class=ClothAddForm
    success_url=reverse_lazy("cloth-list")
    def form_valid(self, form):
        messages.success(self.request,"cloth updated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"cloth updating failed")
        return super().form_invalid(form)


def remove_clothview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Cloths.objects.filter(id=id).delete()
    return redirect("cloth-list")

# localhost:8000/clothvarient/1/add
# localhost:8000/cloths/1/varients/add


class ClothVarientCreateView(CreateView):
    template_name="yousta/clothvarient_add.html"
    form_class=ClothVarientForm
    model=ClothVarients
    success_url=reverse_lazy("cloth-list")

    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Cloths.objects.get(id=id)
        form.instance.cloth=obj
        messages.success(self.request,"varient has been added")
    
        return super().form_valid(form)
    

class ClothDetailView(DetailView):
    template_name="yousta/cloth_detail.html"
    model=Cloths
    context_object_name="cloth"



class ClothVarientUpdateView(UpdateView):
    template_name="yousta/varient_edit.html"
    form_class=ClothVarientForm
    model=ClothVarients
    success_url=reverse_lazy("cloth-list")
    def form_valid(self, form):
        messages.success(self.request,"cloth varient successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"cloth varient updating failed")
        return super().form_invalid(form)
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        cloth_varient_object=ClothVarients.objects.get(id=id)
        cloth_id=cloth_varient_object.cloth.id
        return reverse("cloth-detail",kwargs={"pk":cloth_id})


def remove_varient(request,*args,**kwargs):
    id=kwargs.get("pk")
    ClothVarients.objects.filter(id=id).delete()
    return redirect("cloth-list")


# localhost:8000/varients/<int:pk>/offers/add

class OfferCreateView(CreateView):
    template_name="yousta/offer_add.html"
    form_class=OfferForm
    model=Offers
    success_url=reverse_lazy("cloth-list")
    
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=ClothVarients.objects.get(id=id)
        form.instance.clothvarient=obj

        messages.success(self.request,"offer has been added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed")
        return super().form_invalid(form)
    
    def get_success_url(self):
        # localhost:cloths/<int:pk>/
       id=self.kwargs.get("pk")
       cloth_varient_object=ClothVarients.objects.get(id=id)#clothvarientobject
       cloth_id=cloth_varient_object.cloth.id


       return reverse("cloth-detail",kwargs={"pk":cloth_id})


def offer_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    offer_object=Offers.objects.get(id=id)
    cloth_id=offer_object.clothvarient.cloth.id
    offer_object.delete()
    return redirect("cloth-detail",pk=cloth_id)


def sign_out_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



   
   
