from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello, World!")
def about_page_view(request):
    return render(request,"about.html")
 