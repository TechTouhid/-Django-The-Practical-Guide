from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire januar january  y months",
    "february": "Eat no meat for the entire janua februar  ry months",
    "march": "Eat no meat for the entire january  march  months",
    "april": "Eat no meat for the entire january  april months",
    "may": "Eat no meat for the entire january mo may nths",
    "june": "Eat no meat for the entire january m june  onths",
    "july": "Eat no meat for the entire january m july  onths",
    "august": "Eat no meat for the entire january august   months",
    "september": "Eat no meat for the entire janu septemb  ary months",
    "october": "Eat no meat for the entire januar october  y months",
    "november": "Eat no meat for the entire janua novembe  ry months",
    "december": "Eat no meat for the entire janua decembe  ry months",

}

def index(request):
    list_items = ""
    for month in monthly_challenges:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # return HttpResponseRedirect("/challenges/" + forward_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    """
    :param request:
    :param month: this is a placeholder from urls.py
    :return:
    """
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
