from django.shortcuts import render, redirect
from django.urls import reverse
import hashlib
from .helper import connect


def index(request):
    if 'user' in request.session:
        return redirect(reverse('home'))
    return render(request,'index.html')

def login(request):
    if 'user' in request.session:
        return redirect(reverse('home'))

    try:
        if request.method == 'POST':
            username = request.POST.get('usn')
            password = request.POST.get('pswd')
            if username.strip() == "" or password.strip() == "":
                return render(request,'login.html', {'msg': 'Invalid Credentials'}) 
            password = hashlib.sha256(bytes(password, encoding='utf-8')).hexdigest()
            db = connect()
            data = db.find_one({"userID":username})
            if data is None or data == "":
                return redirect('/404.html')
            else:
                passw = data.get('password')
                if passw == password:
                    request.session['user'] = username
                    return redirect(reverse('home'))
                else:
                    return render(request,'login.html',context={'msg': 'Invalid Credentials'})
    except Exception as e:
        print(e)
    return render(request,'login.html')


def home(request):
    if 'user'  not in request.session:
        return redirect(reverse('index'))
    context = {}
    try:
        username = request.session.get('user')
        db = connect()
        data = db.find_one({"userID":username})
        context = {'userID': data.get('userID'), 'name': data.get('name').title() , 'points': data.get('rewardPoints')}
    except Exception as e:
        print(e)
    return render(request,'home.html', context)

def logout(request):
    del request.session['user']
    return redirect(reverse('index'))


