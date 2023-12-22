from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

from .models import bedrift_data

def statistikk(request):
  mydata = bedrift_data.objects.all()
  template = loader.get_template('statistikk.html')
  context = {
    'bedriftdata': mydata,
  }
  return HttpResponse(template.render(context, request))