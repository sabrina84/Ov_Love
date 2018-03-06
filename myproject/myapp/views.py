from datetime import timedelta, datetime
from datetime import date
from django.http import Http404
from django.shortcuts import render

from .models import UserInfo, Questions, FAQ, Calorie
from .forms import getInfo, getLoginInfo, getQues, getHW

un = "not logged in"

class info:
    name=""
    days=0
    mc=0

    def __init__(self, name, days,mc):
        self.name = name
        self.days = days
        self.mc = mc

class qa:
    qs=""
    an=""

    def __init__(self, qs, an):
        self.qs = qs
        self.an = an

class cal:
    food=""
    cal=0

    def __init__(self, food, cal):
        self.food = food
        self.cal = cal

def login(request) :
    p=""
    p = "hi "
    if request.method == "POST":
        MyForm = getLoginInfo(request.POST)
        if MyForm.is_valid():

            username = MyForm.cleaned_data['username']
            password = MyForm.cleaned_data['password']

            try:
                n = UserInfo.objects.get(username=username)
            except UserInfo.DoesNotExist:
                return render(request, 'login_fail.html', {})
            k = n.password
            if k != password:
                return render(request, 'login_fail.html', {})
            #un = username
            request.session['username'] = username
            request.session.modified = True
            p+= n.name

    else:
        MyForm = getInfo()

    return render(request, 'home_.html', {"username": username})


def signup(request) :
    p=""

    username="not loggeed in"
    per_dur=0
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = getInfo(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            name = MyLoginForm.cleaned_data['name']
            password = MyLoginForm.cleaned_data['password']
            repass = MyLoginForm.cleaned_data['repass']

            #email = MyLoginForm.cleaned_data['email']
            age = MyLoginForm.cleaned_data['age']
           # per_dur = MyLoginForm.cleaned_data['per_dur']
            start_date = MyLoginForm.cleaned_data['start_date']
            end_date = MyLoginForm.cleaned_data['end_date']
            exist_count = UserInfo.objects.filter(username=username).count()


            if exist_count>=1:

                return render(request, 'signup_fail.html', {})

            if password!=repass:
                return render(request, 'wrongpass.html', {})
            a = datetime.strftime(start_date, "%Y-%m-%d")
            new_date = datetime.strptime(a, '%Y-%m-%d').date()
            b = datetime.strftime(end_date, "%Y-%m-%d")
            new_date2 = datetime.strptime(b, '%Y-%m-%d').date()
            per_dur = (new_date2 - new_date).days
            start_date = end_date + timedelta(days=28)
            a = datetime.strftime(start_date, "%Y-%m-%d")
            new_date = datetime.strptime(a, '%Y-%m-%d').date()
            newUser = UserInfo(
               username=username, name=name,password=password,per_dur=per_dur,age=int(age),
                start_date=new_date,end_date=new_date2,missed_count=0
               )
            newUser.save()

            objects = UserInfo.objects.all()

            n = UserInfo.objects.get(username=username)
            p = "hi "+n.name
            p = "hi "+name
            request.session['username'] = username
    else:
        MyLoginForm = getInfo()

    return render(request, 'home_.html', {"username": username})



def profile(request) :
    username = "not logged in"
    try:
        username =  request.session['username']
    except:
        return render(request, 'login.html', {})

    objects = UserInfo.objects.all()
    n = UserInfo.objects.get(username=username)
    a = datetime.now().date()
    b = n.start_date
    k = (b-a).days
    if k<-15:
        a = n.start_date
        b = a + timedelta(days=n.per_dur)
        c = b + timedelta(days=28)
        n.start_date = c;
        n.end_date = b;
        d = n.missed_count + 1
        n.missed_count = d
        n.save()
        a = datetime.now().date()
        k = (c - a).days
    new = info(n.name,k,n.missed_count)

    return render(request, 'profile.html',{"username": username,"prof":new})


def profile_(request) :
    c=0
    i=0
    username = "not logged in"
    try:
        username =  request.session['username']
    except:
        return render(request, 'login.html', {})

    objects = UserInfo.objects.all()
    n = UserInfo.objects.get(username=username)
    a = datetime.now().date()
    b = n.start_date
    k = (b-a).days

    new = info(n.name,k,n.missed_count)
    if request.method == "POST":
        # Get the posted form
        hwForm = getHW(request.POST)

        if hwForm.is_valid():
            act_level = [1,1.12,1.27,1.54]
            weight = hwForm.cleaned_data['weight']
            foot = hwForm.cleaned_data['foot']
            inch = hwForm.cleaned_data['inch']
            act = hwForm.cleaned_data['act']

            al = act_level[act]
            age = UserInfo.objects.get(username=username).age
            height = (((foot*12)+inch)*2.5)/100
            #calorie eqn to be added
            c = 387 - 7.31 * age + al * (10.9 * weight + 660.7 * height)
            c = int(c)
            bmi = weight/(height*height)
            if bmi<18:
                i=1
            elif bmi>25:
                i=3
            else:
                i=2


    return render(request, 'profile_.html',{"username": username,"prof":new,"cal":c,"bmi":i})


def gotit(request) :
    username = "not logged in"
    try:
        username =  request.session['username']
    except:
        return render(request, 'login.html', {})

    objects = UserInfo.objects.all()
    n = UserInfo.objects.get(username=username)
    a = datetime.now().date()
    b = a + timedelta(days=n.per_dur)
    k = b + timedelta(days=28)
    n.start_date = k;
    n.end_date = b;
    n.missed_count=0
    n.save()
    new = info(n.name, k, n.missed_count)

    return render(request, 'profile.html',{"username": username,"prof":new})



def home(request) :
    return render(request, 'signup.html',{})

def home2(request) :
    return render(request, 'login.html',{})

def home_(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'home.html', {})
    return render(request, 'home_.html',{"username": username})

def logout(request) :
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'home.html',{})


def workout(request) :
    try:
        username = request.session['username']
    except:
        pass
    return render(request, 'workout.html',{"username": username})



def home3(request) :
    return render(request, 'home.html',{})

def start(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'home.html', {})
    return render(request, 'home_.html',{"username": username})



def faq(request) :
    username = "not logged in"

    q=[]
    for e in FAQ.objects.all():

        a = e.quest
        p = ''.join(a)

        a = e.answ
        o = ''.join(a)
        new = qa(p,o)
        q.append(new)
    try:
        username = request.session['username']
    except:
        return render(request, 'faq.html', {"q":q})
    return render(request, 'faq2.html',{"username": username,"q":q})



def symptom(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'symptom.html', {})
    return render(request, 'symptom2.html',{"username": username})

def result(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'result.html', {})
    return render(request, 'result2.html',{"username": username})

def control(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'control.html', {})
    return render(request, 'control2.html',{"username": username})




def calorie(request) :
    username = "not logged in"
    q = []
    for e in Calorie.objects.all():
        a = e.food
        p = ''.join(a)

        b = e.cal

        new = cal(p, b)
        q.append(new)
    try:
        username = request.session['username']
    except:
        return render(request, 'calorie.html', {"q":q})
    return render(request, 'calorie2.html',{"username": username,"q":q})




def question(request) :
    username = "not logged in"
    try:
        username = request.session['username']
    except:
        return render(request, 'login.html', {})
    exist_count = Questions.objects.filter(username=username).count()
    q=[]
     #if exist_count>=1:
       # ob = Questions.objects.get(username=username)
       # q = ''.join(ob)

    for e in Questions.objects.all():
        if e.username == username:
            a = e.ques
            p = ''.join(a)

            a = e.ans
            o = ''.join(a)
            new = qa(p, o)
            q.append(new)

    if request.method == "POST":

        quesForm = getQues(request.POST)

        if quesForm.is_valid():
            ques = quesForm.cleaned_data['ques']
            #n = UserInfo.objects.get(username=username)
            newQ = Questions(
                username=username,ques=ques,ans=""
            )
            newQ.save()
        else:
            MyLoginForm = getQues()
    return render(request, 'question.html',{"username": username,"q":q})

