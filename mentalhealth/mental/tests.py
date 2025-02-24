from django.test import TestCase
from .models import StudentExperience



class StudentExperienceModelTest(TestCase):
    
    def setUp(self):
        self.experience = StudentExperience.objects.create(
            username='TestUser',
            content='This is a test experience.'
        )

    def test_experience_creation(self):
        self.assertEqual(self.experience.username, 'TestUser')
        self.assertEqual(self.experience.content, 'This is a test experience.')
        self.assertIsNotNone(self.experience.date_submitted)
