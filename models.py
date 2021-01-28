from django.db import models

# Create your models here.
class Alphabet(models.Model):
    alphabets=models.CharField(max_length=255, null=True, blank=True)


class Alphanumeric(models.Model):
    alphanumeric=models.CharField(max_length=255)

class Numeric(models.Model):
    numeric=models.CharField(max_length=255)
