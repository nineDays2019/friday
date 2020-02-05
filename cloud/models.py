from django.db import models


# Create your models here.

class FileModel(models.Model):
    time = models.fields.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    path = models.fields.FilePathField(verbose_name='本机地址')
