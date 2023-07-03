import os
from django.db import models

from multiselectfield import MultiSelectField
from model_utils.models import TimeStampedModel


PYT = "PYTHON"
NEX = "NEXTJS"
DJA = "DJANGO"
REA = "REACTJS"
PSQ = "POSTGRESQL"
AWS = "AMAZONWEBSERVICES"
DRF = "DJANGORESTFRAMEWORK"

TECHS_CHOICES = (
    (PYT, "Python"),
    (NEX, "Next JS"),
    (REA, "React JS"),
    (PSQ, "PostgreSQL"),
    (AWS, "Amazon Web Services"),
    (DJA, "Django Web Framework"),
    (DRF, "Django Rest Framework"),
)


def screenshot_file_name(self, filename):
    extension = filename.split(".")[-1]
    filename = "screenshot_{}.{}".format(self.id, extension)
    return os.path.join("portfolio/media/projects/photos/screenshots", filename)


class Project(TimeStampedModel):
    url = models.URLField("Website", max_length=200)
    dev_year = models.PositiveSmallIntegerField("Year")
    company = models.CharField("Company", max_length=100)
    title = models.CharField("Project title", max_length=30)
    description = models.TextField("Description", max_length=100)
    in_production = models.BooleanField("Is in production", default=False)
    screenshot = models.ImageField(
        "Screenshot", upload_to=screenshot_file_name, blank=True, null=True
    )
    technologies = MultiSelectField(
        "Technologies",
        choices=TECHS_CHOICES,
        max_length=20,
        max_choices=6,
        blank=True,
    )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["dev_year"]

    @classmethod
    def get_by_id(cls, uid):
        return Project.objects.get(pk=uid)

    def __str__(self):
        return f"{self.title} in {self.url}"
