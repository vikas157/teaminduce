from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.



def home(request):
    return render(request, 'home.html')



def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        from django.contrib.auth.models import User
        user = User.objects.create_user(username=username, password=password, email=email)

        user.save()
        print('user created')
        return redirect('lob')
    else:

        return render(request, 'register.html')


def lob(request):
    return render(request, 'paymentgateway.html')



def members(request):
    results = User.objects.all()
    return render(request, 'members.html', {"data":results})