import os
import random
from django.db import models

def getFilenameExt(filepath):
    baseName = os.path.basename(filepath)
    name, ext = os.path.splitext(baseName)

    return (name,ext)

def uploadImagePath(instance, filename):
    newFilename = random.randint(1,213123123)
    name, ext = getFilenameExt(filename)
    finalFilename = f'{newFilename}{ext}'
    return f"services/{newFilename}/{finalFilename}"


class ProductManager(models.Manager):
    def get_by_id(self, id):
        return self.get_queryset().filter(id=id)
# Create your models here.
class service(models.Model):

    title = models.CharField(max_length=50)

    city = models.CharField(max_length=30)
    state = models.CharField(max_length=25)
    startTime = models.TimeField()
    endTime = models.TimeField()

    price = models.DecimalField(decimal_places=2, max_digits=6)
    priceType = models.CharField(max_length=50)
    telephone = models.CharField(max_length=11)

    minimunAge = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=30) #TODO fazer por SELECT
    image = models.ImageField(upload_to=uploadImagePath, null=True, blank=True)

    description = models.TextField()

    objects = ProductManager()


    def getAbsoluteUrl(self):
        return "/services/{pk}".format(pk=self.pk)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
