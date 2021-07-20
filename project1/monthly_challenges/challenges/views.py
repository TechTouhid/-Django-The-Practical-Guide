from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None

}


def index(request):
    # list_items = ""
    # for month in monthly_challenges:
    #     capitalize_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "challenges/index.html", {
        "months": list(monthly_challenges.keys())
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,  # send the text variable into the html file
            "month_name": month,
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404("404.html")