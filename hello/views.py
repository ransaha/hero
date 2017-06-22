from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.db import connection

def admission(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'admission.html', {"user" : user})
    else:
        return render(request, 'admission.html',{"user":'Guest'})

def contact(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'contact.html', {"user" : user})
    else:
        return render(request, 'contact.html',{"user":'Guest'})

def new(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'new.html', {"user" : user})
    else:
        return render(request, 'new.html',{"user":'Guest'})

def it(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'it.html', {"user" : user})
    else:
        return render(request, 'it.html',{"user":'Guest'})

def math(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'math.html', {"user" : user})
    else:
        return render(request, 'math.html',{"user":'Guest'})

def bank(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'bank.html', {"user" : user})
    else:
        return render(request, 'bank.html',{"user":'Guest'})

def success(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'success.html', {"user" : user})
    else:
        return render(request, 'success.html',{"user":'Guest'})

def login(request):
      if request.session.has_key('user'):
            user = request.session['user']
            return render(request, 'user.html', {"user" : user})
      else:
            user = request.POST.get('name')
            if(not user or user == 'None'):
                return render(request, 'home.html', {'user': 'Guest'})
            else:
                with connection.cursor() as cursor:
                    cursor.execute('''SELECT username FROM users WHERE email = '%s'  ''' % user)
                    row = cursor.fetchone()
                request.session['user'] = row[0]
                return render(request, 'user.html', {'user': row[0]})

def home(request):
   if request.session.has_key('user'):
      user = request.session['user']
      return render(request, 'home.html', {"user" : user})
   else:
      return render(request, 'home.html',{"user":'Guest'})

def logout(request):
   try:
      del request.session['user']
   except:
      pass
   return render(request, 'home.html', {"user":'Guest'})

def upload(request):
    mf = request.FILES['mfile']
    #fs = FileSystemStorage()
    #filename = fs.save(mf.name, mf)
    #url = fs.url(filename)
    #cmd = "mv /home/Masterji/mysite"+url+" /home/Masterji/mysite/static"
    #os.system(cmd)
    user = request.session['user']
    return render(request, 'user.html', {"user" : user})

def register(request):
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass = request.POST.get('password')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO public."users" values('%s','%s','%s','%s')  ''' % (username,name,email,password))
        request.session['user'] = username
        return render(request, 'user.html', {'user': username})
