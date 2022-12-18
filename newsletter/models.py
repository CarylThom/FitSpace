from django.db import models


class Newsletter(models.Model):
    """ Newsletter fields """

    full_name = models.CharField(max_length=75, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.email
