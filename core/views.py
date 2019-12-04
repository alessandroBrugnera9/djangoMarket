from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import ListView

from services.models import service


def homePage(request):
    context ={

    }
    # context[3] = service.objects.get_by_id(3) //TODO tentear colocar os melhores na primeira pagina
    # print(context[3].values("image").clean)
    # print(type(context[3].values("image")))
    if (request.user.is_authenticated):
        context["logado"] = "Logado" #se quiser adicionar outro jeito olhar video 17 começo
    return render(request, "index.html", context)
# Create your views here.



from . import forms

def basePage(request):
    context ={
    }
    if (request.user.is_authenticated):
        context["logado"] = "Logado" #se quiser adicionar outro jeito olhar video 17 começo
    return (render(request,"base.html", context))

def aboutPage(request):
    context ={
    }
    if (request.user.is_authenticated):
        context["logado"] = "Logado" #se quiser adicionar outro jeito olhar video 17 começo
    return (render(request, "about.html", context))

def contactPage(request):
    context ={
    }
    if (request.user.is_authenticated):
        context["logado"] = "Logado" #se quiser adicionar outro jeito olhar video 17 começo
    return (render(request, "contact.html", context))

def loginPage(request):
    formClass = forms.loginForm(request.POST or None)
    context = {
        "form": formClass
    }
    if (request.user.is_authenticated):
        context["logado"] = "Logado" #se quiser adicionar outro jeito olhar video 17 começo
    if formClass.is_valid():
        print(formClass.cleaned_data)

        #validacao
        username = formClass.cleaned_data.get("username")
        password = formClass.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            # context["form"] = forms.loginForm()
            redirect('/index')
        else:
            print("Error")
            ...
    print(request.user.is_authenticated)
    return (render(request, "auth/login.html", context))

user = get_user_model()
def registerPage(request):
    formClass = forms.registerForm(request.POST or None)
    context = {
        "form": formClass
    }
    if (request.user.is_authenticated):
        context["logado"] = "Logado" #se quiser adicionar outro jeito olhar video 17 começo
    if (formClass.is_valid()):
        print(formClass.cleaned_data)
        username = formClass.cleaned_data.get("username")
        email = formClass.cleaned_data.get("email")
        password = formClass.cleaned_data.get("password")
        newUser = user.objects.create_user(username,email,password)
        print(newUser)
        redirect('/index')

    return (render(request, "auth/register.html", context))

def registerServicePage(request):
    formClass = forms.registerForm(request.POST or None)
    context = {
        "form": formClass
    }
    if (request.user.is_authenticated):
        context["logado"] = "Logado" #se quiser adicionar outro jeito olhar video 17 começo
    if (formClass.is_valid()):
        print(formClass.cleaned_data)
        title = formClass.cleaned_data.get("title")
        city = formClass.cleaned_data.get("city")
        price = formClass.cleaned_data.get("price")
        priceType = formClass.cleaned_data.get("priceType")
        telephone = formClass.cleaned_data.get("telephone")
        category = formClass.cleaned_data.get("category")
        description = formClass.cleaned_data.get("description")
        redirect('/index')

    return (render(request, "auth/register.html", context))