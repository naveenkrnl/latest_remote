from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.db.models import Q
from .forms import RelatedForm
from .models import Related,Subject,Topic,TopicResources,Unit,SubjectResources,UnitResources
from assignments.models import Assignment
from .forms import TopicResourceForm,SubjectResourceForm
# Create your views here.

@login_required
def bookshome(request):
    context={}
    related_objects=Subject.objects.filter(semester=request.user.semester).order_by("exam_date")
    context['subjects'] = related_objects
    if request.user.is_teacher is True:
        # related_objects=Subject.objects.filter(semester=request.user.semester).order_by("exam_date")
        # context['subjects'] = related_objects        
        return render(request,"books/teacher_home.html",context)
    #assignments
    context['assignments']=Assignment.objects.filter(semester=request.user.semester)
    
    return render(request,'books/home.html',context)
def subjectdetail(request,q):
    context={}
    subject=Subject.objects.get(slug=q)
    context['resources'] = SubjectResources.objects.filter(subject=subject).order_by("-endorsed")
    form=SubjectResourceForm(request.POST or None)
    context['form'] = form
    # n,created=SubjectUser.objects.get_or_create(user=request.user, subject=subject)
    # if n.count>=1:
    #     context['done']=1
    # else:
    context['done']=0
    if request.GET:
        temp=request.GET['q']
        return HttpResponseRedirect("/search?q={}".format(temp))
    if request.POST:
        if "add_resource" in request.POST:
            if form.is_valid():
                title=form.cleaned_data['title']
                description=form.cleaned_data['description']
                url=form.cleaned_data['url']
                choice=form.cleaned_data['choice']
                a=SubjectResources.objects.create(user=request.user,subject=subject,title=title,description=description,url=url,choice=choice)
                a.save()
        else:
            subject_id=int(request.POST['id'])
            obj=SubjectResources.objects.get(id=subject_id)
            obj.endorsed+=1
            obj.save()
            # t,created=SubjectUser.objects.get_or_create(subject=subject,user=request.user)
            # t.count+=1
            # t.save()
    context['subject']=subject
    return render(request,"books/subject.html",context)
def unitdetail(request,slug):
    context={}
    u=Unit.objects.get(slug=slug)
    context['unit']=u
    context['subject']=u.subject
    context['resources']=UnitResources.objects.filter(unit = u).order_by("-endorsed")
    form=SubjectResourceForm(request.POST or None)
    context['form'] = form
    # n,created=UnitUser.objects.get_or_create(user=request.user, unit=u)
    # if n.count>=1:
    #     context['done']=1
    # else:
    context['done']=0
    if request.GET:
        temp=request.GET['q']
        return HttpResponseRedirect("/search?q={}".format(temp))
    if request.POST:
        if "add_resource" in request.POST:
            if form.is_valid():
                title=form.cleaned_data['title']
                description=form.cleaned_data['description']
                url=form.cleaned_data['url']
                choice=form.cleaned_data['choice']
                a=UnitResources.objects.create(user=request.user,unit=u,title=title,description=description,url=url,choice=choice)
                a.save()
        else:
            unit_id=int(request.POST['id'])
            obj=UnitResources.objects.get(id=subject_id)
            obj.endorsed+=1
            obj.save()
            # t,created=UnitUser.objects.get_or_create(unit=u,user=request.user)
            # t.count+=1
            # t.save()
    return render(request,"books/unit.html",context)
def topicdetail(request,slug):
    context={}
    p=Topic.objects.get(slug=slug)
    form=TopicResourceForm(request.POST or None)
    context['form']=form
    context['subject']=p.unit_part.unit.subject
    context['topic']=p
    context['resources']=TopicResources.objects.filter(topic=p).order_by("-endorsed")
    context['done']=0
    # n,created=TopicUser.objects.get_or_create(user=request.user, topic=p)
    # if n.count>=1:

    #     context['done']=1
    # else:
    #     context['done']=0
    if request.GET:
        temp=request.GET['q']
        return HttpResponseRedirect("/search?q={}".format(temp))
    if request.POST:
        if "add_resource" in request.POST:
            if form.is_valid():
                title=form.cleaned_data['title']
                description=form.cleaned_data['description']
                url=form.cleaned_data['url']
                a=TopicResources.objects.create(user=request.user,topic=p,title=title,description=description,url=url)
                a.save()
        else:
            topic_id=int(request.POST['id'])
            obj=TopicResources.objects.get(id=topic_id)
            obj.endorsed+=1
            obj.save()
            # t,created=TopicUser.objects.get_or_create(topic=p,user=request.user)
            # t.count+=1
            # t.save()
        # return HttpResponseRedirect('#')

    return render(request,"books/topic.html",context)
def createtopicresource(request,slug):
    p=Topic.objects.get(slug=slug)
    return render()

def createrelated(request):
    context={}
    if request.user.is_authenticated:
        form = RelatedForm(request.POST or None)
        context['form']=form
        if form.is_valid():
            ok=form.cleaned_data.get('subject')
            subject1=Subject.objects.get(
                Q(subject_name__icontains=ok)
            )
            user=request.user
            r1,r2=Related.objects.get_or_create(user=user)
            r1.subject.add(subject1)
    return render(request,'books/related.html',context)

def searchview(request):
    context={}
    s=request.GET['q']
    if s is "":
        context['flag']=1
    else:
        context['flag']=0
        context['q']=s
        context['topics']=Topic.objects.filter(
            Q(topic_name__contains=s)
        )
        context['subjects']=Subject.objects.filter(
            Q(subject_name__contains=s)|
            Q(subject_code__contains=s)|
            Q(unit1_syllabus__contains=s)|
            Q(unit2_syllabus__contains=s)|
            Q(unit3_syllabus__contains=s)|
            Q(unit4_syllabus__contains=s)
        ).distinct()
    return render(request,"books/search.html",context)


