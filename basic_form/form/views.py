from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
from . models import Info

# Create your views here.

def show_form(request):
    if request.method == "POST":
        frm = StudentRegistration(request.POST)
        if frm.is_valid():
            #print(frm)
            #print("execuite POST ")
            #print(frm.cleaned_data)
            #print("First Name: ", frm.cleaned_data ['Enter_First_name'])
            #print("Last_name:",frm.cleaned_data['Last_name'])
            #print("email: ", frm.cleaned_data ['email'])
            #print("re_email: ", frm.cleaned_data ['re_email'])
            #print("batch:",frm.cleaned_data['batch'])
            #print("password:",frm.cleaned_data['password'])
            #print("re_password:",frm.cleaned_data['re_password'])
            #print("textarea:",frm.cleaned_data['textarea'])
            #print("django:",frm.cleaned_data['django'])

            fname=frm.cleaned_data ['Enter_First_name']
            lanme=frm.cleaned_data['Last_name']
            eml=frm.cleaned_data ['email']
            re_eml=frm.cleaned_data ['re_email']
            btc=frm.cleaned_data['batch']
            pas=frm.cleaned_data['password']
            r_pass=frm.cleaned_data['re_password']
            txt = frm.cleaned_data['textarea']
            chk = frm.cleaned_data['checkbox']
            pay = frm.cleaned_data['payments']
            dj=frm.cleaned_data['django']
            djangotwo = Info(First_name=fname,Last_name=lanme,Email=eml,Re_Email=re_eml,Batch=btc,password=pas,re_password=r_pass,textarea=txt,checkbox=chk,payments=pay,django=dj)
            djangotwo.save()

            return HttpResponseRedirect('/successfully/')
        

        
    else:
        frm = StudentRegistration(auto_id=True,label_suffix='=', initial={'email':'imran@gmail.com'})
        #frm.order_fields(field_order=['email','Last_name','First_name','batch'])
        print("execute GET")

    return render(request,'form.html',{'form':frm})

def success(request):
    return render(request,'courses/submit.html')
