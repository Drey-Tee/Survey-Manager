from django.shortcuts import render
from .models import Survey, SurveyParticipant


# Create your views here.
def frontend(request):
    """Vue.js will take care of everything else."""
    surveys = Survey.objects.all()
    surveyparticipants = SurveyParticipant.objects.all()

    data = {
        'surveys': surveys,
        'surveyparticipants': surveyparticipants,
    }

    return render(request, 'survey/templates.html', data)

from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Survey
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

# Create your views here.
def survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = SurveyForm()
    return render(request,'survey/index.html',{'form':form})

def show(request):
    surveys = Survey.objects.all()
    return render(request,"survey/show.html",{'surveys':surveys})

def edit(request, id):
    surveys = Survey.objects.get(id=id)
    # surveys = get_object_or_404(Survey, sp_id=sp_id)

    return render(request,'survey/edit.html', {'surveys':surveys})

def update(request,id):
    surveys = Survey.objects.get(id=id)

    form = SurveyForm(request.POST, instance=surveys)
    print(form)
    if form.is_valid():
        form.save()
        print('kkkk')
        return redirect("/show")
        # return HttpResponseRedirect("/show")
    # else:
    return render(request, 'survey/edit.html', {'surveys': surveys})


def destroy(request, id):
    surveys = Survey.objects.get(id=id)
    surveys.delete()
    return redirect("/show")

