from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import UploadFileForm, handle_uploaded_file


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


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

def upload(request):
  mydata = bedrift_data.objects.all()
  template = loader.get_template('upload.html')
  context = {
    'bedriftdata': mydata,
  }
  return HttpResponse(template.render(context, request))