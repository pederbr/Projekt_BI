from urllib import request
from django.db import reset_queries
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import UploadFileForm, handle_uploaded_file


def upload(request):
  if request.method == "POST":
    uploaded_file=request.FILES["docfile"]
    print(uploaded_file.name)
    print(uploaded_file.size)
  return render(request, "upload.html")



def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def to_upload(request):
  template = loader.get_template('upload.html')
  return HttpResponse(template.render())


from .models import bedrift_data

def statistikk(request):
  mydata = bedrift_data.objects.all()
  template = loader.get_template('statistikk.html')
  context = {
    'bedriftdata': mydata,
  }
  return HttpResponse(template.render(context, request))

