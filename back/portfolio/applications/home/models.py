from django.db import models

from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    current_job = models.CharField("Current job", max_length=75)
    creator_name = models.CharField("Creator name", max_length=50)
    self_description = models.TextField("Self escription", max_length=125)
    short_self_description = models.TextField("Short self description", max_length=60)

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"

    def __str__(self):
        return f"{self.creator_name}"
