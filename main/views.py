from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from main.models import Survey
# from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html', {})


def survey(request):
    if not request.user.is_authenticated:
        return redirect(index)
    elif request.method == "POST":
        new_survey = Survey()
        new_survey.name = request.POST.get("name", "")
        new_survey.email = request.POST.get("email", "")
        new_survey.phone = request.POST.get("phone", "")
        new_survey.save()
        # return JsonResponse({"a": request.POST.get("name", "")})
        return render(request, 'main/survey.html', {})
    elif request.method == "GET":
        return render(request, 'main/survey.html', {})
