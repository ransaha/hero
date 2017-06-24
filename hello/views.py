from django.http import HttpResponse
from django.shortcuts import render,redirect
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
        passw = request.POST.get('password')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO users(username,name,email,password,phone,gender) values('%s','%s','%s','%s','%s','%s')  ''' % (username,name,email,passw,phone,gender))
        request.session['user'] = username
        return render(request, 'user.html', {'user': username})
    
def doubt(request):
        user = request.session['user']
        cursor = connection.cursor()
        
        if request.POST.get('doubt') :
            doubt =  request.POST.get('doubt')
            cursor.execute(''' INSERT INTO doubt(message,username) values('%s','%s')  ''' % (doubt,user))
     
        cursor.execute(''' SELECT row,message FROM doubt where id is null ''')
        row = cursor.fetchall()
        return render(request, 'doubt.html', {"user" : user,"doubt":row})
    
def doubt_discuss(request):
    idno = request.GET.get('idno')
    user = request.session['user']
    cursor = connection.cursor()
    
    if request.POST.get('discuss') :
        discuss =  request.POST.get('discuss')
        cursor.execute(''' INSERT INTO doubt(message,username,id) values('%s','%s','%s')  ''' % (discuss,user,idno))
   
    cursor.execute(''' SELECT message,row,id FROM doubt where id='%s' ''' % (idno))
    row = cursor.fetchall()
    return render(request, 'doubt_discuss.html', {"user" : user,"doubt_discuss":row,"idno":idno})
    
def delete_discuss(request):
    idn = request.GET.get('idno')
    temp = idn.split(':')
    user = request.session['user']
    cursor = connection.cursor()
    
    if (temp[1] == 0 or temp[1] == '0') :
        cursor.execute(''' DELETE FROM doubt where row='%s' or id='%s' ''' % (temp[0],temp[0]))
        return redirect('doubt')
    else:
        cursor.execute(''' DELETE FROM doubt where row='%s' and id='%s' ''' % (temp[0],temp[1]))
        return redirect('/doubt_discuss?idno=%s' % temp[1])
    
      
 
    
