from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    Enter_First_name = forms.CharField(error_messages={'required':'Must fill your full name'})
    Last_name = forms.CharField(required=False)
    email= forms.EmailField(label='Enter your Email',validators=[validators.MaxLengthValidator(35)])
    re_email= forms.EmailField(label='Re_enter your Email',validators=[validators.MaxLengthValidator(35)])
    batch = forms.IntegerField(help_text='Must be fill the filed',min_value=1)
    #phone_number = forms.IntegerField(widget=forms.HiddenInput())
    password = forms.CharField(widget=forms.PasswordInput(),min_length=8,max_length=15)
    re_password = forms.CharField(widget=forms.PasswordInput(),min_length=8,max_length=15)
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rpw':5,'cols':20}))
    checkbox = forms.CharField(widget=forms.CheckboxInput())
    payments = forms.DecimalField(min_value=2500,max_value=5000,max_digits=6,decimal_places=2)
    django = forms.BooleanField()

    def clean(self):
        cleaned_data = super().clean
        password_match = self.cleaned_data['password']
        re_password_match =self.cleaned_data['re_password']
        email_match =self.cleaned_data['email']
        re_email_match =self.cleaned_data['re_email']
        if password_match != re_password_match or email_match != re_email_match:
            raise forms.ValidationError("Password or Email Doesn't match")
        
        #and email_match == re_email_match

        
