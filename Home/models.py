from django.db import models

class Image_Model(models.Model):

    image=models.ImageField(upload_to="media/imag")
