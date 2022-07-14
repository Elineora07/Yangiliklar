from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from account.form import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 




def account_registration(request):
    if request.user is authenticate:
        return redirect('main:index')
    request.page_title = _("Ro'yhatdan o'tish")
    request.button_title = request.page_title
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            
            user.set_password(form.cleaned_data['password'])
            
            form.save()
            
            messages.success(request, _("Ro'yhatdan muvaffaqiyatli o'tdingiz"))
            return redirect('main:index') 
    return render(request, 'account/registration.html', {
        "form": form
    })
    
def account_login(request):
    if request.user.is_authenticated:
        return redirect('main:index')
    request.page_title = request.button_title = _("Login")
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            
            if user is not None:
                login(request, user)
                messages.success(request, "Xush kelibsiz, {}".format(user.username))
                
                return redirect("main:index")
            
    request.session['login_error'] =form.cleaned_data['username']
    return redirect(reverse_lazy('main:index') + '?modal=1')




def account_logout(request):
    if not request.user.is_authenticated:
        return redirect('main:index')
       
    messages.success(request, "Kelib turing {}".format(request.user.username))
    logout(request)
    return redirect("main:index")