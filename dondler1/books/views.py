from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from .forms import RelatedForm
from .models import Related,Subject,Topic

# Create your views here.

@login_required
def bookshome(request):
    context={}
    print(request.user.semester)
    related_objects=Subject.objects.all()
    context['subjects'] = related_objects
    return render(request,'books/home.html',context)

class TopicDetailView(DetailView):
    model=Topic
    template_name="books/topic.html"


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
