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
def EditUser (request,id=None):
    one_rec=Crud.objects.get(pk=id)
    form=EntryForm(request.POST or None, request.FILES or   None,instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})
def DeleteUser(request,id=None):
    one_rec=Crud.objects.get(pk=id)
    if request.method=='POST':
        one_rec.delete()
        return redirect('/')
    return render(request, 'delete.html')
def ViewUser(request,id=None):
    mydict={}
    one_rec=Crud.get(pk=id)
    mydict['entry']=one_rec
    return render(request,'view.html',mydict)

