from django.db import models


# Create your models here.

class FileModel(models.Model):
    time = models.fields.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    path = models.fields.FilePathField(verbose_name='本机地址')
    secret = models.fields.BooleanField(default=False, verbose_name='是否加密', null=False)
    category = models.fields.CharField(max_length=20, default='normal')
