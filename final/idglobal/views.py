from django.shortcuts import render
from django.db import IntegrityError
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django import forms
from django.urls import reverse

from .models import Mailing_List

## Form Template for email
class NewUserForm(ModelForm):
    ## body = forms.CharField(widget=forms.Textarea, label="")
    class Meta:
        model = Mailing_List
        fields = ['email']

## Main home page. If POSt - submits form and saves the result.Passes in form
def index (request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
    
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

    return render(request, "idglobal/index.html", {
        "form": NewUserForm()
        })   

## Each of the individual pages are included below - only passing in the form
def reimagining (request):
    return render(request, "idglobal/reimagining.html", {
        "form": NewUserForm()
        })  

def global_children (request):
    return render(request, "idglobal/global_children.html", {
        "form": NewUserForm()
        })  

def us_china (request):
    return render(request, "idglobal/us_china.html", {
        "form": NewUserForm()
        })  

def environmental_stew (request):
    return render(request, "idglobal/environmental_stew.html", {
        "form": NewUserForm()
        })  

def gtr (request):
    return render(request, "idglobal/gtr.html", {
        "form": NewUserForm()
        })  

def curriculum (request):
    return render(request, "idglobal/curriculum.html", {
        "form": NewUserForm()
        })  

def sig_ped (request):
    return render(request, "idglobal/sig_ped.html", {
        "form": NewUserForm()
        })  

def books (request):
    return render(request, "idglobal/books.html", {
        "form": NewUserForm()
        })  

def definition (request):
    return render(request, "idglobal/definition.html", {
        "form": NewUserForm()
        })  