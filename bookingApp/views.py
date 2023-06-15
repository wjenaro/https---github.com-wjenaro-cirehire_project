from django.shortcuts import render

'''
homepage
'''
def index(request):
    return render(request, 'bookingApp/index.html')
'''
login page
'''
def login(request):
    return render(request, 'bookingApp/login.html')
'''
Signup
'''
def signup(request):
    return render(request, 'bookingApp/signup.html')
