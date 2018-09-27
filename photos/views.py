from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def index(request):
  """
  View function that renders the index page
  """
  photos = Image.get_all_images()
  return render(request,'index.html',{"photos":photos})

def image(request,image_id):
    """
    View function that gets the images and displays them on the template.
    """
    image = Image.get_image(image_id)
    return render(request,'index.html',{"image":image})

def search_results(request):
  
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
