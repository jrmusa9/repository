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
    messages.success(request, "Successfully registered!")
    return render(request, 'login/travels.html')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")

    return redirect('/travels')

def travels(request):
    # print request.session['user_id']
    context={
        'user':User.objects.get(id=request.session['user_id']),
        'trips': User.objects.get(id=request.session['user_id']).booking.all(),
        'all_trips': Trip.objects.exclude(id=request.session['user_id'])
    }
    return render(request, 'login/travels.html', context)

def add(request):
    return render(request, 'login/add.html')

def add_trip(request):
    print 'add_trip'
    print len(request.POST['destination'])
    if len(request.POST['destination'])<1:
        messages.error(request, "Type a destination")
        return redirect('/adding')
    else:
        Trip.objects.create(
            destination = request.POST['destination'],
            description = request.POST['description'],
            start_at = request.POST['start'],
            end_at = request.POST['end'],
            added_by = User.objects.get(id=request.session['user_id']),
        )

        Trip.objects.get(destination=request.POST['destination']).Booked_by.add(User.objects.get(id=request.session['user_id']))



    return redirect('/travels')


def join(request, trip_id):

    Trip.objects.get(id=trip_id).Booked_by.add(User.objects.get(id=request.session['user_id']))

    return redirect('/travels')

def destination(request, trip_id):
    creater_id=Trip.objects.get(id=trip_id).added_by_id
    print creater_id
    print Trip.objects.get(id=trip_id).Booked_by.exclude(id=User.objects.get(id=creater_id).id)


    context={
        'trip': Trip.objects.get(id=trip_id),
        'users': Trip.objects.get(id=trip_id).Booked_by.exclude(id=User.objects.get(id=creater_id).id).all()
    }
    return render(request, 'login/destination.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

