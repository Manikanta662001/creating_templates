from django.shortcuts import render

# Create your views here.
def base(request):
    d={'name':'svsvsdv','age':22}
    return render(request,'base.html',d)