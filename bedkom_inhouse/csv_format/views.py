from urllib import request
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import bedrift_data
from .forms import filForm



def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def upload(request):
  form =filForm()
  context={"form": form}
  return render(request, "upload.html", context)


def statistikk(request):
  mydata = bedrift_data.objects.all()
  template = loader.get_template('statistikk.html')
  context = {
    'bedriftdata': mydata,
  }
  return HttpResponse(template.render(context, request))

