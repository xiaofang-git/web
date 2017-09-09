from django.db import models

# Create your models here.


class Gupiao(models.Model):
    num = models.CharField(max_length=10)
    short_name = models.CharField(max_length=40)
    title = models.CharField(max_length=255)
    href = models.CharField(max_length=255)



#
# I = Person.objects.all()
# for i in I:
#     print(i)