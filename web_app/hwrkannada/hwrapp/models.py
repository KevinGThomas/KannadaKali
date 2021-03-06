from django.db import models

# Create your models here.


class DocumentImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.ImageField(upload_to='documents/')
    pub_date = models.DateTimeField(auto_now=True)


# Create your models here.
class KanDB(models.Model):
    kannada=models.CharField(max_length=50)
    eng=models.CharField(max_length=50)
    mis=models.CharField(max_length=50)
    freq=models.IntegerField()
    comp=models.IntegerField()
    aud=models.FileField(upload_to='audio')
    saud=models.FileField(upload_to='snail_audio')
    img=models.ImageField(upload_to='image')