from django.db import models


class Newsletter(models.Model):
    """A model to save the subscribe/newsletter form"""

    email = models.EmailField(max_length=254, unique=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
