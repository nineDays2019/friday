import os

from django.shortcuts import render
from django.http import HttpResponse
import time
from .config import cloud_dir
from . import models


# Create your views here.

def index(request):
    return render(request, 'cloud/index.html')


def upload(request):
    if request.method == "POST":
        path = cloud_dir() + request.POST['category'] + "/"  # 保存路径
        if not os.path.exists(path):
            os.makedirs(path)
        files = request.FILES.getlist('file')
        for file in files:
            name = str(round(time.time() * 1000)) + os.path.splitext(file.name)[1]
            with open(path + name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                destination.close()

            file_model = models.FileModel.objects.create(path=os.path.abspath(path + name),
                                                         category=request.POST['category'], )
            file_model.save()
        return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中

    return render(request, 'cloud/index.html')
