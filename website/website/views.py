from django.http import HttpResponse
from django.shortcuts import render
from .models import SPARQL_Model


def index(request):
    results = SPARQL_Model().get_document_info()
    return render(request, "index.html", {"results": results})
