from django.db import models

from multiselectfield import MultiSelectField
from model_utils.models import TimeStampedModel

from .choices import SKILLS_CHOICES


class Experience(TimeStampedModel):
    role = models.CharField("Job role", max_length=100)
    end_date = models.PositiveSmallIntegerField("End date")
    start_date = models.PositiveSmallIntegerField("Start date")
    role_description = models.TextField("Role description", max_length=125)
    skills = MultiSelectField(
        "Role skills",
        choices=SKILLS_CHOICES,
        max_length=30,
        max_choices=4,
        blank=True,
    )

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.role} since {self.start_date} to {self.end_date}"
