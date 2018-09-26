from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
  """
  View function that renders the index page
  """
  return HttpResponse('Welcome to Gallery')
