import json
from django.urls import reverse
from django.test import TestCase, Client

from rest_framework import status

from ..models import Project
from ..serializers import ProjectModelSerializer


client = Client()


class GetAllProjectsTest(TestCase):
    """Test module for GET all projects API"""

    def setUp(self):
        Project.objects.create(
            dev_year=2023,
            in_production=True,
            title="Example Project",
            url="https://example.com",
            company="Example Company",
            technologies=["PYTHON", "DJANGO"],
            description="This is an example project",
        )
        Project.objects.create(
            dev_year=2021,
            in_production=False,
            title="Example Project",
            technologies=["PYTHON"],
            url="https://example.com1",
            company="Example Company1",
            description="This is an example project1",
        )

    def test_get_all_projects(self):
        response = client.get(reverse("project-list"))

        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)

        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProjectTest(TestCase):
    """Test module for GET single project API"""

    def setUp(self) -> None:
        self.project_1 = Project.objects.create(
            dev_year=2023,
            in_production=True,
            title="Example Project",
            url="https://example.com",
            company="Example Company",
            technologies=["PYTHON", "DJANGO"],
            description="This is an example project",
        )

    def test_get_valid_single_project(self):
        response = client.get(
            reverse("project-detail", kwargs={"pk": self.project_1.pk})
        )
        project = Project.objects.get(pk=self.project_1.pk)
        serializer = ProjectModelSerializer(project)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_not_found_single_project(self):
        response = client.get(reverse("project-detail", kwargs={"pk": 12}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateSingleProjectTest(TestCase):
    """Test module for POST a new project API"""

    def setUp(self) -> None:
        self.valid_payload = {
            "dev_year": 2023,
            "in_production": True,
            "title": "Example Project",
            "url": "https://example.com",
            "company": "Example Company",
            "description": "This is an example project",
            "technologies": ["PYTHON", "DJANGO"],
        }

    def test_forbidden_create_project(self):
        response = client.post(
            reverse("project-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UpdateSingleProjectTest(TestCase):
    """Test module for PATCH a project API"""

    def setUp(self) -> None:
        self.project_1 = Project.objects.create(
            dev_year=2023,
            in_production=True,
            title="Example Project",
            url="https://example.com",
            company="Example Company",
            technologies=["PYTHON", "DJANGO"],
            description="This is an example project",
        )

        self.valid_payload = {
            "dev_year": 2024,
            "in_production": False,
        }

    def test_forbidden_patch_project(self):
        response = client.patch(
            reverse("project-detail", kwargs={"pk": self.project_1.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeleteSingleProjectTest(TestCase):
    """Test module for DELETE a project API"""

    def setUp(self) -> None:
        self.project_1 = Project.objects.create(
            dev_year=2023,
            in_production=True,
            title="Example Project",
            url="https://example.com",
            company="Example Company",
            technologies=["PYTHON", "DJANGO"],
            description="This is an example project",
        )

    def test_forbidden_delete_project(self):
        reponse = client.delete(
            reverse("project-detail", kwargs={"pk": self.project_1.pk})
        )
        self.assertEqual(reponse.status_code, status.HTTP_403_FORBIDDEN)
