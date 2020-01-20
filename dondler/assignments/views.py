from django.shortcuts import render
from .models import Assignment, SubmitAssignment
from .forms import SubmitForm,CreateAssignmentForm
from django.core.files.storage import FileSystemStorage
from django.db.models import Q


# Create your views here.
def submit_assignment(request,id):
    context={}
    assignment=Assignment.objects.get(id=id)
    context['assignment']=assignment
    context['subject']=assignment.subject
    i=SubmitAssignment.objects.filter(
        Q(assignment=assignment)&
        Q(user=request.user)
    ).count()
    if (i>=1):
        context['flag']=1
    form=SubmitForm(request.POST or None,request.FILES or None)
    context['form']=form
    if request.POST:
        if form.is_valid():
            print(request.POST)
            print(request.FILES)
            description=form.cleaned_data.get("description")
            link=form.cleaned_data.get("link")
            files=form.cleaned_data.get("files")
            a=SubmitAssignment.objects.create(assignment=assignment,user=request.user,description=description,link=link,files=files)
            a.save()    
    return render(request,"assignments/submit.html",context)
    
def create_assignment(request):
    context={}
    if request.user.is_teacher is True:
        form=CreateAssignmentForm(request.POST or None)
        context['form']=form
        if request.POST:
            print(request.POST)
        return render(request,"assignments/create.html",context)