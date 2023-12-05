from django.db import models

class buy(models.Model):
      Name=models.CharField(max_length=20)
      State=models.CharField(max_length=20)
      lga=models.CharField(max_length=20)
      Home_Adress=models.CharField(max_length=20)
      product_Id=models.IntegerField()
