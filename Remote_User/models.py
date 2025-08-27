from django.db import models

# Create your models here.
from django.db.models import CASCADE

class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class crop_prediction(models.Model):

    RID= models.CharField(max_length=3000)
    N= models.CharField(max_length=3000)
    P= models.CharField(max_length=3000)
    K= models.CharField(max_length=3000)
    temperature= models.CharField(max_length=3000)
    humidity= models.CharField(max_length=3000)
    ph= models.CharField(max_length=3000)
    rainfall= models.CharField(max_length=3000)
    Recommended_Zone= models.CharField(max_length=3000)
    Crop_Name= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



