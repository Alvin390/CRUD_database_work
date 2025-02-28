from django.shortcuts import render,redirect
from .models import Crud
from .forms import EntryForm
# Create your views here.
def entry_list(request):
    entry=Crud.objects.all()
    return render(request,'listingpage.html',{'entry':entry})
