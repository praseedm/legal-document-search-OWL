from django.http import HttpResponse
from django.shortcuts import render
from .models import SPARQL_Model


def index(request):
    results = SPARQL_Model().get_document_info()
    return render(request, "index.html", {"results": results})


def parties_info(request):
    results = SPARQL_Model().get_parties_info()
    return render(request, "parties_info.html", {"results": results})


def remunerations_info(request):
    results = SPARQL_Model().get_remuneratoin_info()
    return render(request, "remuneration_info.html", {"results": results})


def active_documents(request):
    results = SPARQL_Model().filter_document_bystatus(status="active")
    return render(request, "active_docs.html", {"results": results})


def pending_documents(request):
    results = SPARQL_Model().filter_document_bystatus(status="pending")
    return render(request, "active_docs.html", {"results": results})
