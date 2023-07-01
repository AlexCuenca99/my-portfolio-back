from django.test import TestCase

from .models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project_data = {
            "dev_year": 2023,
            "in_production": True,
            "title": "Example Project",
            "url": "https://example.com",
            "company": "Example Company",
            "description": "This is an example project",
            "technologies": ["PYTHON", "DJANGO"],
        }

    def test_create_project(self):
        project = Project.objects.create(**self.project_data)

        self.assertEqual(project.url, self.project_data["url"])
        self.assertEqual(project.title, self.project_data["title"])
        self.assertEqual(project.company, self.project_data["company"])
        self.assertEqual(project.dev_year, self.project_data["dev_year"])
        self.assertEqual(project.description, self.project_data["description"])
        self.assertEqual(project.in_production, self.project_data["in_production"])
        self.assertListEqual(
            list(project.technologies), self.project_data["technologies"]
        )

    def test_project_to_string(self):
        project = Project.objects.create(**self.project_data)
        self.assertEqual(
            str(project), f"{self.project_data['title']} in {self.project_data['url']}"
        )

    def test_get_by_id(self):
        project = Project.objects.create(**self.project_data)
        self.assertEqual(Project.get_by_id(1), project)
