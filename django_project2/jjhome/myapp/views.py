from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')
def reptile(request):
    return render(request,'reptiles.html')
def ant(request):
    return render(request,'ants.html')
def spider(request):
    return render(request,'spiders.html')
def insect(request):
    return render(request,'insects.html')
def arthropod(request):
    return render(request,'arthropods.html')
def caresheet(request):
    return render(request,'caresheets.html')
