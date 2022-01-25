from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    cep = models.CharField(max_length=255, blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)
    neighborhood = models.CharField(max_length=255, blank=False, null=False)
    street = models.CharField(max_length=255, blank=False,null=False)

    def __str__(self):
        return self.city

class MyModel(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=False, null=False)
    address = models.ForeignKey(Address, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name