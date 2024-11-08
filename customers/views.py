from django.shortcuts import render

from customers.forms import CustomerForm


# Create your views here.
def index(request):
    return render(request,template_name='index.html')

def about(request):
    return render(request, template_name='about.html')

def contact(request):
    form = CustomerForm()
    return render(request, template_name='contact.html',context={'form':form})