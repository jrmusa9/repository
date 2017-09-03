# from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)

    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!, now you can log in!")
    return redirect('/')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")

    return redirect('/quotes')

def quotes(request):
    print request.session['user_id']
    print User.objects.get(id=request.session['user_id']).likes.all()
    context={
        'user':User.objects.get(id=request.session['user_id']),
        'quotes_left':Quote.objects.exclude(id__in=User.objects.get(id=request.session['user_id']).likes.all()),
        'quotes_right':User.objects.get(id=request.session['user_id']).likes.all(),
    }
    return render(request, 'login/quotes.html', context)

def remove(request, fav_id ):

    User.objects.get(id=request.session['user_id']).likes.remove(Quote.objects.get(id=fav_id))

    return redirect('/quotes')

def add(request):
    print request.session['user_id']
    print request.POST['quoted_by']
    print 'mesg length', len(request.POST['message'])

    if len(request.POST['quoted_by']) <3 or len(request.POST['message'])<10:
        messages.error(request, 'Name must be 3 char, Quote must be 10 char min.')
        return redirect('/quotes')
    else:
        Quote.objects.create(message=request.POST['message'], quoted_by=request.POST['quoted_by'], added_by_id=request.session['user_id'])



    return redirect('/quotes')

def add_favorite(request, fav_id):
    print fav_id
    print request.session['user_id']

    User.objects.get(id=request.session['user_id']).likes.add(Quote.objects.get(id=fav_id))

    return redirect('/quotes')

def user(request, user_id):
    print user_id   

    context={
        'user':User.objects.get(id= user_id),
        'user_quotes': Quote.objects.filter(added_by= user_id),
        'count': Quote.objects.filter(added_by= user_id).count()

    }


    return render(request,'login/user.html', context)


# def join(request, trip_id):

#     Trip.objects.get(id=trip_id).Booked_by.add(User.objects.get(id=request.session['user_id']))

#     return redirect('/travels')

# def destination(request, trip_id):
#     creater_id=Trip.objects.get(id=trip_id).added_by_id
#     print creater_id
#     print Trip.objects.get(id=trip_id).Booked_by.exclude(id=User.objects.get(id=creater_id).id)


#     context={
#         'trip': Trip.objects.get(id=trip_id),
#         'users': Trip.objects.get(id=trip_id).Booked_by.exclude(id=User.objects.get(id=creater_id).id).all()
#     }
#     return render(request, 'login/destination.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

