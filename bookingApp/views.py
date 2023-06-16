from django.shortcuts import render

'''
homepage
'''
def index(request):
    return render(request, 'bookingApp/index.html')

