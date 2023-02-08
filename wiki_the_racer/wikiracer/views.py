from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_form(request):
    if request.method == 'POST':
        # do something with the data
        return HttpResponse('Thanks for submitting the form!')
    else:
        return render(request, 'index.html')