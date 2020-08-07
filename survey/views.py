from django.shortcuts import render, redirect
from .models import SurveyParticipant, Surveys, Questions, Responses
from .forms import SurveyForm, CreateQuestionForm
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect


# # Create your views here.
# def frontend(request):
#     """Vue.js will take care of everything else."""
#     surveys = Survey.objects.all()
#     surveyparticipants = SurveyParticipant.objects.all()
#
#     data = {
#         'surveys': surveys,
#         'surveyparticipants': surveyparticipants,
#     }
#
#     return render(request, 'survey/templates.html', data)


def survey(request):
    # surveys = SurveyQuestions.objects.all()
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            print(1)
            try:
                form.save()
                print(2)
                return redirect('/show')
            except:
                pass
    else:
        form = SurveyForm()
    return render(request, 'questions/question_index.html', {'form': form, })


def show(request):
    surveys = Surveys.objects.all()
    return render(request, "questions/question_show.html", {'surveys': surveys})


def edit(request, id):
    surveys = Surveys.objects.get(id=id)
    print(surveys)
    # surveys = Survey.objects.all()

    form = SurveyForm(request.POST, instance=Surveys)
    if request.method == 'POST':
        # surveys.survey_id = form.data['survey_id']
        surveys.survey_name = form.data['survey_name']
        surveys.save()
        print(surveys)
        return redirect('/show')
    return render(request, 'questions/question_edit.html', {'surveys': surveys})


def destroy(request, id):
    surveys = Surveys.objects.get(id=id)
    surveys.delete()
    return redirect("/show")


def create(request):
    surveys = Surveys.objects.all()
    question = Questions.objects.all()
    print(question)
    if request.method == "POST":
        form = CreateQuestionForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form = CreateQuestionForm()
        print(2)
    return render(request, 'questions/create.html', {'form': form, 'surveys': surveys, 'question':question })


def home(request):
    # question = Questions.objects.get(id=id)
    surveys = Surveys.objects.all()
    questions = Questions.objects.all()
    print(questions)
    return render(request, 'questions/home.html', {'questions': questions, 'surveys':surveys})


# def vote(request, id):
#     responses = Responses.objects.get(id=id)
#     print(responses)
#     if request.method == 'POST':
#         print(request.POST['responses'])
#
#         #get the selected option
#         responses.response = request.POST['survey']
#         responses.id = request.POST['q_id']
#         responses.user_name = request.POST['uname']
#         responses.survey_id_id = request.POST['s_id']
#         responses.save()
#         print(responses)
#         return redirect('/results', question.id)
#
#     context = {
#         'question': question
#     }
#     return render(request, 'questions/vote.html', context)


def results(request):
    print(request.POST)
    responses = Responses.objects.all()
    # print(responses)
    if request.method == 'POST':
        r = Responses(question_id=request.POST['q_id'], response=request.POST['survey'], user_name=request.POST['uname'], survey_id_id=request.POST['s_id'])

        r.save()

    return render(request, 'questions/results.html',{'responses':responses})


