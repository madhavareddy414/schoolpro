from django import forms


class StudentForm(forms.Form):
        sname = forms.CharField(max_length=30,label='Student Name')
        sclass = forms.CharField(max_length=30,label='Class')
        saddr = forms.CharField(max_length=30,label='Address')
        semail = forms.EmailField(max_length=30,label='Email')
class SForm(forms.Form):
    sname= forms.CharField(max_length=30,label='Student Name')