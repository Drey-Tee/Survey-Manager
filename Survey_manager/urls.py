"""Survey_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from survey import views as survey_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', survey_views.frontend),
    # path('surveys/<slug:slug>/', survey_views.frontend),
    # path('surveyparticipants/<slug:slug>/', survey_views.frontend),
    # path('survey', survey_views.survey),
    # path('show',survey_views.show),
    # path('edit/<int:id>', survey_views.edit),
    # path('delete/<int:id>', survey_views.destroy),
    path('question', survey_views.question),
    path('show_q',survey_views.show_q),
    path('edit_q/<int:id>', survey_views.edit_q),
    path('delete_q/<int:id>', survey_views.destroy_q),
    path('create_q/<int:id>', survey_views.create_q, name = 'create'),
    path('home', survey_views.home),
    path('vote/<int:id>', survey_views.vote, name='vote'),
    path('results/<int:id>', survey_views.results, name='results'),


]

