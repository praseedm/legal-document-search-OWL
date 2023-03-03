from django.http import HttpResponse
from django.shortcuts import render
from .models import SPARQL_Model


def index1(request):
    results = SPARQL_Model().get_statuses()
    return render(request, "index.html", {"results": results})
