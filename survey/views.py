from django.shortcuts import render, redirect
from .models import SurveyParticipant, SurveyQuestions, Questions
from .forms import QuestionForm, CreateQuestionForm
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


def question(request):
    # surveys = SurveyQuestions.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            print(1)
            try:
                form.save()
                print(2)
                return redirect('/show_q')
            except:
                pass
    else:
        form = QuestionForm()
    return render(request, 'questions/question_index.html', {'form': form, })


def show_q(request):
    questions = SurveyQuestions.objects.all()
    return render(request, "questions/question_show.html", {'questions': questions})


def edit_q(request, id):
    question = SurveyQuestions.objects.get(id=id)
    # surveys = Survey.objects.all()

    form = QuestionForm(request.POST, instance=SurveyQuestions)
    if request.method == 'POST':
        question.survey_id = form.data['survey_id']
        question.survey_name = form.data['survey_name']
        question.save()
        return redirect('/show_q')
    return render(request, 'questions/question_edit.html', {'question': question})


def destroy_q(request, id):
    questions = SurveyQuestions.objects.get(id=id)
    questions.delete()
    return redirect("/show_q")


def create_q(request, id):
    question = SurveyQuestions.objects.get(id=id)
    print(question)
    if request.method == "POST":
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form = CreateQuestionForm()
    return render(request, 'questions/create.html', {'form': form, })


def home(request):
    quests = Questions.objects.all()
    return render(request, 'questions/home.html', {'quests': quests})


def vote(request, id):
    question = Questions.objects.get(id=id)
    print(question)
    if request.method == 'POST':
        # print(request.POST['question'])
        selected_option = request.POST['survey']
        if selected_option == 'option1':
            question.option_one_count += 1
        elif selected_option == 'option2':
            question.option_two_count += 1
        elif selected_option == 'option3':
            question.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        question.save()
        print(question)
        return redirect('/results', question.id)

    context = {
        'question': question
    }
    return render(request, 'questions/vote.html', context)


def results(request, id):
    quest = Questions.objects.get(id=id)
    context = {
        'quest': quest
    }
    return render(request, 'questions/results.html', context)
