from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
  """
  View function that renders the index page
  """
  return render(request,'index.html')
