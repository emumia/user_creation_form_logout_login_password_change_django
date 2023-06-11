from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,SetPasswordForm
from . forms import usercf
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash

# Create your views here.

def usercform(request):
    if request.method == "POST":
        frm = usercf(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = usercf()
    return render(request, 'usercform.html', {'form':frm})


def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upass = frm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/form1/success')
    else:
        frm = AuthenticationForm()
    return render(request, 'login.html', {'form':frm})

#Successfully login
def slogin(request):
	return render(request,'success.html')

#logout
def logout_form(request):
	logout(request)
	return HttpResponseRedirect('/form1/login')

# change password with old  password

def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = PasswordChangeForm(user=request.user, data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/form1/success/')
        else:
            frm = PasswordChangeForm(user=request.user)
        return render(request, 'passc.html', {'form':frm})
    else:
        return HttpResponseRedirect('/form1/login/')
    
# change password without old  password

def without_old_password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = SetPasswordForm(user=request.user, data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/form1/success/')
        else:
            frm = SetPasswordForm(user=request.user)
        return render(request, 'withoutpassc.html', {'form':frm})
    else:
        return HttpResponseRedirect('/form1/login/')


