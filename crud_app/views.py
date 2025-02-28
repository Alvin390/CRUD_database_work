from django.shortcuts import render,redirect
from .models import Crud
from .forms import EntryForm
# Create your views here.
def entry_list(request):
    entry=Crud.objects.all()
    return render(request,'listingpage.html',{'entry':entry})
def AddUser(request):
    mydict={}
    form=EntryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form']=form
    return render(request,'add.html',mydict)
