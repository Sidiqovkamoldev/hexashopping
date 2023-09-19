from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForms



def user_login(request):

    if request.method=="POST":
        form=LoginForms(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,
                              username=data["username"],
                              password=data["password"])

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return HttpResponse("Muvvaqiyatli login amalga oshirildi!")

                else:
                    return HttpResponse("Profil foal holata emas!")

            else:
                return HttpResponse("Login va parola xatolik bor!")

    else:
        form=LoginForms()
        context={
            'form':form
        }

    return render(request, "account/login.html",context)