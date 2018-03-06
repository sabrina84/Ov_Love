from django import forms

class getInfo(forms.Form):
    name  = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    repass = forms.CharField(widget=forms.PasswordInput())
    #email = forms.EmailInput()
    age = forms.IntegerField()
   # per_dur = forms.CharField(max_length=50)
    start_date = forms.DateField()
    end_date = forms.DateField()

class getLoginInfo(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class getQues(forms.Form):
    ques = forms.CharField()


class getHW(forms.Form):
    weight = forms.IntegerField()
    foot = forms.IntegerField()
    inch = forms.IntegerField()
    act = forms.IntegerField()