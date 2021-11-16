from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    # print(f"request is {request}")
    return render(request, "index.html")
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")