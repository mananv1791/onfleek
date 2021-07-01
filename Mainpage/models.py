from django.db import models

class Dress(models.Model):
    Dress_id = models.IntegerField(primary_key=True)
    Dress_Number = models.IntegerField(blank=True, null=True)
    Dress_Company = models.CharField(max_length=200, blank=True, null=True)
    Dress_Price = models.IntegerField(blank=True, null=True)
    Dress_Image = models.FileField(upload_to="images", blank=True)

    def __str__(self):
        return str(self.Dress_Number)
