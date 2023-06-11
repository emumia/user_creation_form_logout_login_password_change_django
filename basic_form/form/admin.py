from django.contrib import admin
from .models import Student,Info

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','student_id','student_name','student_email','batch','course')

admin.site.register(Student,StudentAdmin)

class InfoAdmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Email','Batch','password','re_password','textarea','checkbox','payments','django')

admin.site.register(Info,InfoAdmin)    


